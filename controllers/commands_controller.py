from flask import Blueprint, jsonify
from main import db
# from main import bcrypt
from models.users import User
from models.pets import Pet
from models.rents import Rent
from models.reviews import Review


erase = Blueprint("erase", __name__, url_prefix="/erase")


@erase.get("/")
def reset_server():
    db.drop_all()

    db.create_all()

    user1 = User(username="Matt",
                 password="12345")

    user2 = User(username="Dani",
                 password="12345")

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    pet1 = Pet(name="Frida",
               type="dog",
               owner=user1)

    pet2 = Pet(name="Henry",
               type="dog",
               owner=user2)

    db.session.add(pet1)
    db.session.add(pet2)
    db.session.commit()

    rent1 = Rent(renter=user1,
                 pet=pet2)
    rent2 = Rent(renter=user2,
                 pet=pet1)

    db.session.add(rent1)
    db.session.add(rent2)
    db.session.commit()

    review1 = Review(review_message="What a perfect pup!",
                     renter=user2,
                     pet=pet1)

    db.session.add(review1)
    db.session.commit()

    return jsonify(message="Tables dropped, created and seeded")
