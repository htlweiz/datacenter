"""Table Role."""

import sqlalchemy
from .base import Base

class Role():
    __tablename__ = "role"
    ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    RoleName = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    Description = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
  

    def __repr__(self):
        """Generate nice representation!"""
        return "RoleName:%s" % self.RoleName
