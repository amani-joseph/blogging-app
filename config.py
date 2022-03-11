import os
class Config:
    """
    General configurations parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')   
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<<user>>:<<Password>>@localhost/<<db_name>>'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # UPLOADED_PHOTOS_DEST = 'app/static/photos'  
    #   email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587 
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SUBJECT_PREFIX = '<<xxxxx>>'
    # SENDER_EMAIL = '<<your sending email>>'

    # simple mde  configurations
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://< your heroku url here>'
    pass
    
  
    
class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<<user>>:<<Password>>@localhost/<<db_name>>'
    pass
    
class DevConfig(Config):

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<<user>>:<<Password>>@localhost/<<db_name>>'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}