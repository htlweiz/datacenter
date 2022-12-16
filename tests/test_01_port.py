"""Test the Port Module"""

from datacenter.model.port import Port
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


def test_01_port(capsys):
    """Test Port."""
    session = create_test_session()
    port = datacenter.model.Port()
    port.IPAddress = "Port"
    session.add(port)
    session.commit()

    assert repr(port) == "IPAddress:Port"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""