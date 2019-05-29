class Config(object):
    SECRET_KEY = 'mysecret'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass 

class TestConfig(Config):
    pass 
