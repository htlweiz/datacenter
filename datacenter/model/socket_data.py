"""Socket Database."""

from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Socket(Base):
    """Socket Database."""

    tablename = 'sockets'

    id = Column(Integer, primary_key=True)
    socket_name = Column(String)
    first_connection_id = Column(Integer, ForeignKey('connections.id'))
    second_connection_id = Column(Integer, ForeignKey('connections.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))

    def __repr__(self):
        """Generate nice representation for Socket."""
        return "Socket:%s" % self.socket_name
