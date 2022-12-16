from .base import Base
from .user import User
import sqlalchemy

class PhoneNumber(Base):
    __tablename__ = "PhoneNumber"
    phone_number_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    phone_number = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(User.ID))

    def __repr__(self) -> str:
        return "Phone number:%s" % self.phone_number