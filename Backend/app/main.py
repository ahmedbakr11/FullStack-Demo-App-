from flask import Flask
from flask_restx import Api, Resource
from Backend.config import Devconfig


app=Flask(__name__)
app.config.from_object(Devconfig)
api=Api(app, doc='/docs')



@api.route('/hello')
class helloresource(Resource):
    def get(self):
        return{"message":"hello"}
    




if __name__=='__main__':
    app.run()