def validate_text(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")

    return value.strip()


def validate_id(value, field_name="ID"):
    value = validate_text(value, field_name)

    if not value.isdigit() or int(value) <= 0:
        raise ValueError(f"{field_name} must be a positive number.")

    return value


def validate_year(year):
    if not isinstance(year, int) or not 1000 <= year <= 9999:
        raise ValueError("Year must be a valid four-digit year.")

    return year