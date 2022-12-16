"""Table User."""

import sqlalchemy
from .base import Base


class User(Base):
    """Orm class User."""
    __tablename__ = "user"
    ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    Firstname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Surename = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Username = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        """Representation!"""
        return "Firstname:%s" % self.Firstname
