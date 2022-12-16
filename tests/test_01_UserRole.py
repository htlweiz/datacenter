"""Test the UserRole Class"""

from datacenter.model.UserRole import UserRole
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


def test_01_UserRole(capsys):
    """Test FooBar."""
    session = create_test_session()
    userRole = datacenter.model.UserRole()
    userRole.value = "UserRole"
    session.add(userRole)
    session.commit()

    assert repr(userRole) == "UserRole:UserRole"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
