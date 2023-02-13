# from sqlalchemy import ForeignKey, Column, Integer, String
from main import db


class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)
    owner_id = db.Column(db.Integer(),
                         db.ForeignKey("users.id"),
                         nullable=False)
    rents = db.relationship("Rent",
                            backref="pet",
                            cascade="all, delete")
    reviews = db.relationship("Review",
                              backref="pet",
                              cascade="all, delete")
