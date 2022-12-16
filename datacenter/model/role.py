"""role datamodel."""

import sqlalchemy
from .base import Base

class Role(Base):
    """role model class."""
    __tablename__ = "role"
    roleID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    roleName = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        """Generate nice representation!"""
        return "role:%s, %s" % self.roleName, self.description
