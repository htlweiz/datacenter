"""Test the Device Module"""

from datacenter.model.device import Device
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


def test_01_device(capsys):
    """Test Device."""
    session = create_test_session()
    device = datacenter.model.Device()
    device.DeviceName = "DeviceName"
    session.add(device)
    session.commit()

    assert repr(device) == "DeviceName:DeviceName"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
