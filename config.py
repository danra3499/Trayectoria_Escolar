class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Jimena11'
    MYSQL_DB = 't_e'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
