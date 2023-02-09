from sqlalchemy import Column, Integer, ForeignKey
from main import db


class Rent(db.Model):
    __tablename__ = "rents"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
