import pymysql

# ==== 获取数据库中的数据 ====
# 打开数据库连接 IP  用户  密码  数据库名称  编码
db = pymysql.connect("localhost", "root", "root", "db1", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "select * from user where id = 1"

# 执行SQL语句
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()

cate_names = [i[1] for i in results]

# 关闭数据库连接
db.close()
