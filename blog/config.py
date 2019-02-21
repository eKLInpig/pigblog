

# 服务器
WSIP = '127.0.0.1'
WSPORT = 8000

# 数据库
schema ='mysql+pymysql'
username = 'pig'
password = '123'
host = '192.168.25.134'
port = 3306
database = 'pigblog'
params = 'charset=utf8'

SQLURL =  "{}://{}:{}@{}:{}/{}?{}".format(
    schema, username, password, host, port, database, params
)

SQLDEBUG = True

# 常量
AUTH_EXPIRE = 8 * 60 * 60
AUTH_SECRET = "eKLIn"