from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import Blueprint, abort, request, jsonify
from main import db
from models.users import User
from models.pets import Pet
from views.pet_schema import pet_schema, pets_schema
from views.user_schema import user_schema, users_schema
from views.review_schema import review_schema, reviews_schema
from views.rent_schema import rent_schema, rents_schema


pets = Blueprint("pets", __name__, url_prefix="/pets")


@pets.get("/")
def get_pets():
    pets_list = Pet.query.all()
    return jsonify(pets_schema.dump(pets_list))
