import sqlalchemy
from .base import Base

class Address(Base):
    """Create the Address table"""
    __tablename__ = "Address"
    Id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    UserId = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    City = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=False)
    Street = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=False)
    Housenumber = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    Zipcode = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __repr__(self):
        """Generate nice representation!"""
        return "Address:%s" % self.value