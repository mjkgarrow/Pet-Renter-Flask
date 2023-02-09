from sqlalchemy import Column, Integer, String
from main import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    pets = db.relationship("Pet",
                           backref="owner",
                           cascade="all, delete")
    rents = db.relationship("Rent",
                            backref="renter",
                            cascade="all, delete")
    reviews = db.relationship("Review",
                              backref="renter",
                              cascade="all, delete")
