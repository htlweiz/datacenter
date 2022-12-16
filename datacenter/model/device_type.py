"""Demotable DeviceType."""

import sqlalchemy
from .base import Base

class DeviceType(Base):
    """Demo orm class DeviceType."""
    __tablename__ = "device_type"
    device_type_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    device_functionality = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        """Generate nice representation!"""
        return "DeviceType:%s" % self.device_functionality
