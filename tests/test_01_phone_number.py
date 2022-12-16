"""Test the exam_env module.

all import and structural testing is done in this module.
"""

from datacenter.model.phone_number import PhoneNumber
from datacenter.model.user import User
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


def test_01_phone_number(capsys):
    """Test PhoneNumber."""
    session = create_test_session()
    user = datacenter.model.User(first_name="Max",
                                 sure_name="Musterman",
                                 username="mm12",
                                 password="12345678")
    session.add(user)
    session.commit()
    phone_number = datacenter.model.PhoneNumber(phone_number=06648332918, user_id=user.ID)
    session.add(phone_number)
    session.commit()

    assert repr(phone_number) == "Phone number: 06648332918"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""