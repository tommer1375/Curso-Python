import re

def check_email(email):
    email_pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    email_match = re.match(email_pattern, email)
    return bool(email_match)

def check_dni(dni):
    dni_pattern=r"\d{8}[A-Z]$"
    dni_match = re.match(dni_pattern, dni)
    return (bool(dni_match)) 

def check_password(password):
    pass_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    pass_match= re.match(pass_pattern,password)
    return (bool(pass_match))