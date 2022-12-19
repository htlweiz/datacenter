import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base
from .building import Building

@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_building_orm(db_session):
    building = Building(name="Test Building")
    db_session.add(building)
    db_session.commit()
    result = db_session.query(Building).first()
    assert result == building

def test_building_repr(db_session):
    building = Building(name="Test Building")
    assert str(building) == "Building:Test Building"
