from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import Blueprint, abort, request, jsonify
from main import db
from models.users import User
from models.pets import Pet
from views.pet_schema import pet_schema, pets_schema
from views.user_schema import user_schema, users_schema


index = Blueprint("index", __name__)


@index.get("/")
def get_users():
    return jsonify(message="Welcome to Rent-a-Pet")
