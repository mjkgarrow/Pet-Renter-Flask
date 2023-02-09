from marshmallow import fields
from main import ma


class PetSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "name", "type", "owner", "reviews")
    owner = fields.Nested("UserSchema", only=("username",))
    reviews = fields.List(fields.Nested("ReviewSchema",
                                        only=("review_message", "renter")))


pet_schema = PetSchema()
pets_schema = PetSchema(many=True)
