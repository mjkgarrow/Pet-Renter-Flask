# from sqlalchemy import Column, Integer, ForeignKey
from main import db


class Rent(db.Model):
    __tablename__ = "rents"
    id = db.Column(db.Integer(), primary_key=True)
    owner_id = db.Column(db.Integer(),
                         db.ForeignKey("users.id"),
                         nullable=False)
    pet_id = db.Column(db.Integer(), db.ForeignKey("pets.id"), nullable=False)
