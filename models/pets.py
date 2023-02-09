from sqlalchemy import ForeignKey, Column, Integer, String
from main import db


class Pet(db.Model):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    rents = db.relationship("Rent",
                            backref="pet",
                            cascade="all, delete")
    reviews = db.relationship("Review",
                              backref="pet",
                              cascade="all, delete")
