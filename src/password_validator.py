def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    if " " in password:
        return False

    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not has_upper or not has_digit:
        return False

    return True
