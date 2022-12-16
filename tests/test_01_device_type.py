"""Test the exam_env module.

all import and structural testing is done in this module.
"""

from datacenter.model.device_type import DeviceType
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


def test_01_device_type(capsys):
    """Test FooBar."""
    session = create_test_session()
    m_device_type = datacenter.model.DeviceType()
    m_device_type.device_functionality = "Teacher stuff."
    session.add(m_device_type)
    session.commit()

    assert repr(m_device_type) == "DeviceType:Teacher stuff."

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
