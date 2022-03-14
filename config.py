import os
class Config:
    """
    General configurations parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'  
    #   email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Welcome to amani.blog !!'
    SENDER_EMAIL = 'amani.blogging@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pfzrwwfmjgjfli:2a7e164de6b4bf8f71ba1e595da04d3a1bb86c011dacff66954f77e0d3a1de6a@ec2-3-231-254-204.compute-1.amazonaws.com:5432/d6tfdgpcmra51f'
    pass
    
  
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/blog'
    pass
    
class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}