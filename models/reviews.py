# from sqlalchemy import Column, Integer, ForeignKey, String
from main import db


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer(), primary_key=True)
    review_message = db.Column(db.String(), nullable=False)
    owner_id = db.Column(db.Integer(),
                         db.ForeignKey("users.id"),
                         nullable=False)
    pet_id = db.Column(db.Integer(), db.ForeignKey("pets.id"), nullable=False)
