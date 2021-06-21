import os


class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'  
    DEBUG = True    

    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog_test'

   
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
