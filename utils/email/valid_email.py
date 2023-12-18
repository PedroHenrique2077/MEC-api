import re
import requests
from validate_email import validate_email

def verify_email_is_valid(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if not (re.search(regex,email)):  
        raise Exception('Email not valid')

    """ endpoint = 'https://www.verifyemailaddress.org/email-validation/result/'
    data = {
        'email': email
    }

    response = requests.post(endpoint, data)
    """

    return True

def verify_email_exists(email):

    is_valid = validate_email(
    email_address=email,
    check_format=True,
    check_blacklist=True,
    check_dns=True,
    dns_timeout=10,
    check_smtp=True,
    smtp_timeout=10,
    smtp_helo_host='my.host.name',
    smtp_from_address='my@from.addr.ess',
    smtp_skip_tls=False,
    smtp_tls_context=None,
    smtp_debug=False)

    if(is_valid == True):
        return is_valid
    else:
        raise Exception("Email does not exist")