class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    # Jimena11
    # secret
    MYSQL_PASSWORD = ''
    MYSQL_DB = 't_e'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
