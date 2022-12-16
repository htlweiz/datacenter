"""Test the exam_env module.
all import and structural testing is done in this module.
"""

from datacenter.model.email import Email
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

def test_01_email(capsys):
    """Test FooBar."""
    session = create_test_session()
    email = datacenter.model.Email()
    m_device_type.device_functionality = "Teacher stuff."
    session.add(m_device_type)
    session.commit()

    assert repr(m_device_type) == "DeviceType:Teacher stuff."

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""