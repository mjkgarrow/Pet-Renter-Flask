from sqlalchemy import Column, Integer, ForeignKey, String
from main import db


class Review(db.Model):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    review_message = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
