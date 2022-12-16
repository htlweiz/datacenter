"""Table Network Usage."""

from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from base import Base


class NetworkUsage(Base):
    """Network usage class."""
    __tablename__ = 'network_usage'

    network_usage_id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    traffic = Column(Integer, nullable=False)
    performance = Column(Integer, nullable=False)
    connection_id = Column(Integer, ForeignKey('connection.ID'))

    def __repr__(self):
        """Generate nice representation!"""
        return "NetworkUsage: {}mb/s\n {}\n time:{}".f(
                        self.traffic, self.performance, self.timestamp)
