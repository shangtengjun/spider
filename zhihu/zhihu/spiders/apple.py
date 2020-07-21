import scrapy
import json  # 两种请求都是 json 格式的返回
from zhihu.items import Answer, Question

QUESTION_IDS_SEEN = set()  # 用来保存已经爬过的问题 id
QUESTION_LIMIT = 500       # 限制最多爬取 500 条

# 答案链接，中间用{}空出来的地方是问题 id
ANSWER_URL = (
    'https://www.zhihu.com/api/v4/questions/{}/answers?include='
    'data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed'
    '%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Cco'
    'llapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditabl'
    'e_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreat'
    'ed_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2'
    'Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%'
    '2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5'
    'D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%'
    '2A%5D.topics&limit=10&offset=0&platform=ios&sort_by=default'
)



class AppleSpider(scrapy.Spider):
    name = 'apple'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/topics/19550292/feeds/top_activity?limit=10']

    # 解析列表页
    def parse(self, response):
        # 拿到 Question 数据并记录下这一页的 id
        list_data = json.loads (response.text)
        question_ids = []
        for data in list_data['data']:
            target = data['target']
            # 如果 type 不是 answer 就跳过（表示是一篇文章）
            if target['type'] != 'answer':
                continue
            question = Question ( )
            question['title'] = target['question']['title']
            question['link'] = target['question']['url']
            question['question_id'] = target['question']['id']
            # 给出一条 Question 结果
            yield question
            question_ids.append (question['question_id'])

        # 根据上面的 ids 爬内容页，使用 self.parse_question
        for question_id in question_ids:
            QUESTION_IDS_SEEN.add (question_id)
            yield response.follow (ANSWER_URL.format (question_id), self.parse_question)

        # 爬下一页，使用 self.parse
        if len (QUESTION_IDS_SEEN) > QUESTION_LIMIT:
            # 如果爬到限制的 500 题，就返回
            return
        yield response.follow (list_data['paging']['next'], self.parse)

    # 解析问题页
    def parse_question(self, response):
        answer_data = json.loads (response.text)
        for data in answer_data['data']:
            answer = Answer ( )
            answer['author'] = data['author']['name']
            answer['vote_count'] = data['voteup_count']
            answer['content'] = data['content']
            answer['question_id'] = data['question']['id']
            yield answer