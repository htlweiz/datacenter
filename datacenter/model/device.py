"""Table Device."""

import sqlalchemy
from .base import Base
from .device_type import DeviceType


class Device(Base):
    """Orm class Device."""
    __tablename__ = "device"
    ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    DeviceName = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    DeviceTypeId = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("device_type.device_type_id"), nullable=False)

    def __repr__(self):
        """Representation!"""
        return "DeviceName:%s" % self.DeviceName
