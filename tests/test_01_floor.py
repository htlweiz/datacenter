"""Test the Floor module."""

from datacenter.model.floor import Floor
from utilities import create_test_session

try:
    import datacenter
except ImportError:
    pass


def test_00(capsys):
    """Test module import."""
    assert datacenter
    assert datacenter.model

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""


def test_01_floor(capsys):
    """Test Floor."""
    session = create_test_session()
    floor = datacenter.model.Floor()
    floor.value = "Floor"
    session.add(floor)
    session.commit()

    assert repr(floor) == "Floor:Floor"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
