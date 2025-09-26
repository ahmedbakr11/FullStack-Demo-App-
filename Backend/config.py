from decouple import config
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Devconfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "dev.db")

class Prodconfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=config('DB_URL_PROD')
    SQLALCHEMY_ECHO=True

class testconfig(Config):
    pass
