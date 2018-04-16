import os

# this key is used to encrypt tokens.
# If the random key is used and the server restart, all the previous log in tokens will and invalidated
# SECRET_KEY = os.urandom(24)
SECRET_KEY = '123'

#dialect+driver://username:password@host:port/database
#todo: replace the following by the real database config
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '192.168.232.146'
PORT = 3306
DATABASE = 'ultrax'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                       PORT, DATABASE)