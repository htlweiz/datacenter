"""Table Connection."""

import sqlalchemy
from .base import Base
from .port import Port


class Connection(Base):
    """Orm class Connection."""
    __tablename__ = "connection"
    ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    FirstPortID = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("port.ID"),
                                nullable=False)
    SecondPortID = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("port.ID"),
                                nullable=False)
    DataTransferRate = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    Cable_Type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    PoE = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    

    def __repr__(self):
        """Generate nice representation!"""
        return "Connection:%s" % self.ID
