"""Demotable FooBar."""

import sqlalchemy
from .user import User
from .base import Base


class UserRole(Base):
    """UserRole Table Class."""
    __tablename__ = "UserRole"
    userrole_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(User.ID))
    role_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(User.ID))

    def __repr__(self):
        """Generate nice representation!"""
        return "UserRole:%s" % self.value
