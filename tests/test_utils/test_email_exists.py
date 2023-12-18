import pytest
from utils.email.valid_email import verify_email_exists

invalid_email_params = pytest.mark.parametrize('email', [
    ('email_invalido@exemplo')
])

valid_email_params = pytest.mark.parametrize('email', [
    ('pedro.rodriguesdecarvalho080@gmail.com')
])

@invalid_email_params
def test_email_invalid_exist(email: str):
    with pytest.raises(Exception):
        verify_email_exists(email)

@valid_email_params
def test_email_valid_exist(email: str):
    assert verify_email_exists(email) is True