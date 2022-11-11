import string


def is_valid_email_address(s):
    s = s.lower()
    parts = s.split('@')
    if len(parts) != 2:
        return False
    allowed = set(string.ascii_lowercase + string.digits + '.-_')
    for part in parts:
        if not set(part) <= allowed:
            return False
    return True


