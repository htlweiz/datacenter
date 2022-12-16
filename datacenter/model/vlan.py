"""Table VLAN."""

import sqlalchemy
from .base import Base


class VLAN(Base):
    """Orm class VLAN."""
    __tablename__ = "vlan"
    ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    Vlan_Name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Vlan_ID = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __repr__(self):
        """Representation!"""
        return "Vlan Name:%s" % self.Vlan_Name
