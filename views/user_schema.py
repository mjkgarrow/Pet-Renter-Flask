from marshmallow import fields
from main import ma


class UserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "username", "password", "pets")
    pets = fields.List(fields.Nested("PetSchema", only=("name", "type")))


user_schema = UserSchema()
users_schema = UserSchema(many=True)
