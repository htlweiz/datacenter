"""Test the Building Module"""

from datacenter.model.building import Building
from utilities import create_test_session

try:
    import datacenter
except ImportError:
    pass


def test_01_building(capsys):
    """Test Building."""
    session = create_test_session()
    building = datacenter.model.Building()
    building.name = "Building"
    session.add(building)
    session.commit()

    assert repr(building) == "Building:Building"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""