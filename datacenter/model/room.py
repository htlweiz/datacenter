import sqlalchemy
from .base import Base
from .floor import Floor

class Room(Base):
    __tablename__ = "Room"
    room_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    room_name = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    floor_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(Floor.floorID))

    def __repr__(self):
        """Generate nice representation!"""
        return "Room:%s" % self.room_name

