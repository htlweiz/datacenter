"""Table Port Connection."""

import sqlalchemy
from .base import Base
from .port import Port
from .connection import Connection


class PortConnection():
    __tablename__ = "PortConnection"
    ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    PortID = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("port.ID"),
                                nullable=False)
    ConnectionID = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("connection.ID"),
                                nullable=False)

    def __repr__(self):
        """Generate nice representation!"""
        return "PortConnection:%s" % self.PortID
