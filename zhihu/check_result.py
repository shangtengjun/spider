import json

with open('zhihu_iphone.jsonl') as f:
    for line in f.read().split('\n'):
        try:
            data = json.loads(line)
        except json.decoder.JSONDecodeError:
            pass
        if data.get('title'):
            print(data['title'])

with open('zhihu_iphone.jsonl') as f:
    count = 0
    huawei_count = 0
    for line in f.read().split('\n'):
        try:
            data = json.loads(line)
        except json.decoder.JSONDecodeError:
            pass
        if data.get('content'):
            count += 1
            huawei_count += data['content'].count('华为')

print('知乎 iPhone 话题下最热门问题的', count, '个回答中，「华为」两个字共出现了', huawei_count, '次')