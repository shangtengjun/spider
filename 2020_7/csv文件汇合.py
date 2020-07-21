import csv
import yagmail
filenames = ['2019-12-%02d-销售数据.csv' % (i + 1) for i in range(31)]

with open('12月销售数据汇总.csv', 'w', newline='') as file:
  csv_writer = csv.writer(file)

  for filename in filenames:
    with open(filename, newline='') as file:
      csv_reader = csv.reader(file)
      #处理出现多个列表头，只保存第一个的
      if filename == filenames[0]:
        rows = csv_reader
      else:
        rows = list(csv_reader)[1:]
      csv_writer.writerows(rows)


with open('12月销售计算数据汇总.csv', 'w', newline='') as file:
  csv_writer = csv.writer(file)

  with open('12月销售数据汇总.csv', newline='') as file:
    csv_reader = csv.reader(file)
    #enumerate() 函数获取索引和每行数据内容，当索引是 0 时表示是第一行数据，即为表头，剩下来的就都是表格数据了
    for index, row in enumerate(csv_reader):
      if index == 0:  # 第一个是表头
        csv_writer.writerow(row + ['购买转化率', '客单价'])  # 添加两个新表头
      else:
        visitors = int(row[2])  # 访客数
        buyers = int(row[3])  # 买家数
        gmv = int(row[4])  # 交易额
        #处理分母为0的情况
        sale_rate = buyers / visitors if visitors else 0  # 购买转化率
        pct = gmv / buyers if buyers else 0  # 客单价
        csv_writer.writerow(row + [sale_rate, pct])  # 添加购买转化率和客单价

'''使用python邮箱发送'''
user = 'xxxxxx@qq.com'  # 发件人邮箱
#授权码不是我们的密码，是需要单独获取的。这里以 QQ 邮箱为例进行讲解。在 QQ 邮箱的设置-账号页面有 POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV 服务 这么一个选项，我们需要开启第一个 POP3/SMTP 服务。
password = 'xxxxxxxxxxxxxxxx'  # 授权码
#我们在搜索引擎中搜索 QQ 邮箱 smtp 服务器地址 即可得到。如果使用的其他邮箱，搜索对应的邮箱 smtp 服务器地址即可。比如，163 邮箱 smtp 服务器地址。
host = 'smtp.qq.com'  # smtp 服务器地址
to = ['xxxxxx@qq.com']  # 收件人邮箱列表
subject = '12月销售计算数据汇总'  # 邮件主题
contents = ['统计了 12 月的销售数据，请查收~', 'D:\\excel\\12月销售计算数据汇总.csv']  # 邮件正文

yag = yagmail.SMTP(user=user, password=password, host=host)
yag.send(to=to, subject=subject, contents=contents)