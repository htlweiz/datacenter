"""Table Port."""

import sqlalchemy
from .base import Base
from .device import Device
from .vlan import VLAN


class Port(Base):
    """Orm class Port."""
    __tablename__ = "port"
    ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    IPAddress = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    MACAddress = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    DeviceId = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("device.ID"),
                                nullable=False)
    VlanID = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("vlan.ID"),
                                nullable=False)

    def __repr__(self):
        """Representation!"""
        return "IPAddress:%s" % self.IPAddress
