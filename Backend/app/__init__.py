from flask import Flask
from .extentions import db, migrate, api
from Backend.config import Devconfig


def create_app():
    
    app=Flask(__name__)                     ## creats flask app
    app.config.from_object(Devconfig)       ## inherites the configuration class from the config file
    
    #initialize Api, database, and migrations to app (inherited form extensions)
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    return(app)

