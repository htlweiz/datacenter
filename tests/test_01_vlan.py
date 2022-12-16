"""Test the VLAN Module"""

from datacenter.model.vlan import VLAN
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


def test_01_vlan(capsys):
    """Test Vlan."""
    session = create_test_session()
    vlan = datacenter.model.VLAN()
    vlan.Vlan_Name = "Vlan"
    session.add(vlan)
    session.commit()

    assert repr(vlan) == "Vlan Name:Vlan"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
