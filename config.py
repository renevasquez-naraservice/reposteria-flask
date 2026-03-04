
class Config:
    SECRET_KEY ='clave_secreta_123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/db_local_reposteria'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    REMEMBER_COOKIE_DURATION = 3600