"""Test the exam_env module.

all import and structural testing is done in this module.
"""

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
    address.value = "Address"
    session.add(address)
    session.commit()

    assert repr(address) == "Address:Address"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
