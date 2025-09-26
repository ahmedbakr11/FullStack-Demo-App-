from flask import request
from flask_restx import Resource, fields
from Backend.app import create_app
from .extentions import api
from .models import User

app = create_app()


##serializer (converts python object data into JSON)
user_model=api.model("User",
    {
    "id":fields.Integer(),
    "username":fields.String(),
    "email":fields.String(),
    }
)


@api.route('/hello')                 
class helloresource(Resource):
    def get(self):
        return{"message":"hello"}



@api.route('/database-test')
class CRUDresource(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        user = User.query.all()
        return(user)



    @api.expect(user_model)
    @api.marshal_with(user_model)
    def post(self):
        data = request.json
        new_user = User(
            username = data.get("username"),
            email = data.get("email")
        )
        new_user.save()






if __name__ == "__main__":
    app.run()