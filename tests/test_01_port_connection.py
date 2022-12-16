"""Test the PortConnection Module"""

from datacenter.model.port_connection import PortConnection
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


def test_01_port_connection(capsys):
    """Test PortConnection."""
    session = create_test_session()
    port_connection = datacenter.model.PortConnection()
    port_connection.PortID = "PortID"
    session.add(port_connection)
    session.commit()

    assert repr(port_connection) == "PortConnection:PortID"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
