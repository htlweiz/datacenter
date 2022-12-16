"""Test the UserRole Class"""

from datacenter.model.user import User
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


def test_01_user(capsys):
    """Test Firstname."""
    session = create_test_session()
    first_name = datacenter.model.User()
    first_name.Firstname = "first_name"
    session.add(first_name)
    session.commit()

    assert repr(first_name) == "Firstname:Firstname"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
