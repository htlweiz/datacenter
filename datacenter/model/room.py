import sqlalchemy
from .base import Base
from .floor import Floor

class Room():
    __tablename__ = "Room"
    room_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    room_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    floor_id = sqlalchemy.Column(sqlalchemy.Integer, foreign_key=True)

