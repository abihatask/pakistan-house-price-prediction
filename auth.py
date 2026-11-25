import re


def validate_signup(username, email, password, confirm):
    if len(username) < 3:
        return "Username must be at least 3 characters."
    if not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email):
        return "Enter a valid email."
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if password != confirm:
        return "Passwords do not match."
    return None