"""Test the role datamodel."""

from datacenter.model.role import Role
from utilities import create_test_session

try:
    import datacenter
except ImportError:
    pass

def test_01_role(capsys):
    """test the role."""

    session = create_test_session()
    role = datacenter.model.Role()
    role.roleName = "Role1"
    role.description = "BLIBLUBLADADADA"
    session.add(role)
    session.commit()

    assert repr(role) == "Role:Role, BLIBLUBLADADADA"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""