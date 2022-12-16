import sqlalchemy
from .user import User
from .base import Base

class Email(Base):
    """Demo orm class Email."""
    __tablename__ = "email"
    email_id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    email_address = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    userid = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey(User.ID))
    main_email = sqlalchemy.Column(sqlalchemy.BOOLEAN, nullable=False)
