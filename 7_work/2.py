import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","teng358.","test" ,charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#建表
'''
# 使用预处理语句创建表
sql = """
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8
"""
# 执行SQL语句
cursor.execute(sql)
'''
#插入多行
'''
# 定义要执行的sql语句
sql = 'insert into user1(name,age) values(%s,%s);'
data = [
    ('july', '14'),
    ('june', '25'),
    ('marin', '36')
]
# 拼接并执行sql语句
cursor.executemany(sql, data)

# 涉及写操作要注意提交
db.commit( )
'''
#插入单行
'''
sql = 'insert into user1(name,age) values (%s,%s);'
name = 'kobe'
pwd = '24'
cursor.execute(sql, [name, pwd])
db.commit( )

# 获取最新的那一条数据的ID
last_id = cursor.lastrowid
print("最后一条数据的ID是:", last_id)
'''
#删除单行
'''
# 定义将要执行的SQL语句
sql = "delete from user1 where name=%s;"
name = "june"
# 拼接并执行SQL语句
cursor.execute(sql, [name])
# 涉及写操作注意要提交
db.commit()
'''

#更改数据
'''
# 定义将要执行的SQL语句
sql = "update user1 set age=%s where name=%s;"
# 拼接并执行SQL语句
cursor.execute (sql, ["18", "july"])

# 涉及写操作注意要提交
db.commit ( )
'''

#查询数据
'''
# 定义将要执行的sql语句
sql = 'select name,age from user1;'
# 拼接并执行sql语句
cursor.execute(sql)

# 取到查询结果
ret1 = cursor.fetchone( )  # 取一条
ret2 = cursor.fetchmany(3)  # 取三条
ret3 = cursor.fetchone( )  # 取一条


print(ret1)
print(ret2)
print(ret3)
'''







# 关闭光标对象
cursor.close()
# 关闭数据库连接
db.close()

