"""Test the Role Module"""

from datacenter.model.role import Role
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


def test_01_role(capsys):
    """Test Role."""
    session = create_test_session()
    role = datacenter.model.Role()
    role.RoleName = "Name"
    session.add(role)
    session.commit()

    assert repr(role) == "RoleName:Name"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
