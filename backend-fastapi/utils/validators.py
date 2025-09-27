from bcrypt import hashpw, gensalt
import re


def validate_and_hash_password(obj, key, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        if value.lower() == obj.username.lower():
            raise ValueError("Password cannot be the same as username")

        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"
        if not re.match(regex, value):
            raise ValueError(
                "Password must contain at least 1 uppercase, 1 lowercase, "
                "1 number"
            )

        hashed_password = hashpw(value.encode("utf-8"), gensalt())
        return hashed_password.decode("utf-8")


def validate_email(obj, key, value):
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex, value):
        raise ValueError(f"Invalid email address: {value}")
    return value

def validate_price(value):
    if value > 0:
        return value
    raise ValueError(f"Invalid price, price can't be {value}")

def validate_role(value):
     CHOICE = ["MEMBER", "ADMIN", ""]
     if value in CHOICE:
          return value
     return "MEMBER"