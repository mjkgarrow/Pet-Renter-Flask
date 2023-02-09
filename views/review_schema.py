from marshmallow import fields
from main import ma


class ReviewSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id",
                  "review_message",
                  "pet",
                  "renter")
    pet = fields.Nested("PetSchema", only=("name",))
    renter = fields.Nested("UserSchema", only=("username",))


review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)
