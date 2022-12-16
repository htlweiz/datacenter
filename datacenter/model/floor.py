"""Table Floor."""

import sqlalchemy
from .building import Building


class Floor:
    __tablename__ = "floor"
    floorID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    floor_name = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    building_ID = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('building.building_id'))

    def __repr__(self):
        """Generate nice representation!"""
        return "Floor:%s" % self.floor_name
