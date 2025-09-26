from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api

api = Api(doc='/docs')

db=SQLAlchemy()
migrate=Migrate()
