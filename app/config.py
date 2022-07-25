class Config():
    DEBUG = True
    
    RESTX_JSON = {'ensure_ascii': False}
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
