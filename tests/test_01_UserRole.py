"""Test the UserRole Module"""

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
    """Test UserRole."""
    session = create_test_session()
    userRole = datacenter.model.UserRole()
    userRole.userrole_id = "UserRole"
    session.add(userRole)
    session.commit()

    assert repr(userRole) == "UserRole:UserRole"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
