from sqlalchemy import Integer, ForeignKey, Column, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from .user import User
from .base import Base

class Address(Base):
    """Create the Address table"""
    __tablename__ = "Address"
    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey(User.ID), nullable=False)
    City = Column(VARCHAR(255), nullable=False)
    Street = Column(VARCHAR(255), nullable=False)
    Housenumber = Column(Integer, nullable=False)
    Zipcode = Column(Integer, nullable=False)
    # this breaks the tests!
    # user = relationship("User", back_populates="Address")

    def __repr__(self):
        """Generate nice representation!"""
        return "Address:%s" % self.value