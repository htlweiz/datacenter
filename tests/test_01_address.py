"""Test the Address Module"""

from datacenter.model.address import Address
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


def test_01_address(capsys):
    """Test Address."""
    session = create_test_session()
    address = datacenter.model.Address()
    address.City = "City"
    session.add(address)
    session.commit()

    assert repr(address) == "Address:City"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
