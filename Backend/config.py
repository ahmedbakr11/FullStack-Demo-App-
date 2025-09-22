from decouple import config



class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Devconfig(Config):
    DEBUG=True
    DB_URL=config('DB_URL')

class Prodconfig(Config):
    DEBUG=False
    DB_URL=config('DB_URL_PROD')
    SQLALCHEMY_ECHO=True

class testconfig(Config):
    pass
