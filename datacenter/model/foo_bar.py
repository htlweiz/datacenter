"""Demotable FooBar."""

import sqlalchemy
from .base import Base


class FooBar(Base):
    """Demo orm class FooBar."""
    __tablename__ = "foobar"
    foobar_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    value = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        """Generate nice representation!"""
        return "FooBar:%s" % self.value
