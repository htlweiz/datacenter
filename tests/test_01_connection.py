"""Test the Connection Module"""

from datacenter.model.connection import Connection
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


def test_01_connection(capsys):
    """Test Connection."""
    session = create_test_session()
    connection = datacenter.model.Connection()
    connection.ID = "Connection."
    session.add(connection)
    session.commit()

    assert repr(connection) == "Connection:Connection"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
