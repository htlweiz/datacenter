"""Demotable building."""

import sqlalchemy
from .base import Base

class Building(Base):
    """Orm class for building"""
    __tablename__ = "building"
    building_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)

    def __repr__(self):
        """Generate nice representation!"""
        return "Building:%s" % self.name
