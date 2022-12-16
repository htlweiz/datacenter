"""Table UserRole."""

import sqlalchemy
from .base import Base
from .user import User
from .role import Role


class UserRole(Base):
    """UserRole Table Class."""
    __tablename__ = "UserRole"
    userrole_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.ID"))
    role_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("role.ID"))

    def __repr__(self):
        """Generate nice representation!"""
        return "UserRole:%s" % self.userrole_id
