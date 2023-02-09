from marshmallow import fields
from main import ma


class RentSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "pet", "renter")
    pet = fields.List(fields.Nested("PetSchema", only=("name",)))
    renter = fields.List(fields.Nested("UserSchema", only=("username",)))


rent_schema = RentSchema()
rents_schema = RentSchema(many=True)
