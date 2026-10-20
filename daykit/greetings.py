def _validate_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    name = name.strip()
    if not name:
        raise ValueError("name cannot be empty")

    return name


def good_morning(name: str) -> str:
    """Return a friendly morning greeting."""
    return f"Good morning, {_validate_name(name)}!"


def good_afternoon(name: str) -> str:
    """Return a friendly afternoon greeting."""
    return f"Good afternoon, {_validate_name(name)}!"


def good_evening(name: str) -> str:
    """Return a friendly evening greeting."""
    return f"Good evening, {_validate_name(name)}!"


def get_greeting(name: str, hour: int) -> str:
    """Return a greeting based on a 24-hour clock value."""
    _validate_name(name)

    if not isinstance(hour, int):
        raise TypeError("hour must be an integer")

    if not 0 <= hour <= 23:
        raise ValueError("hour must be between 0 and 23")

    if hour < 12:
        return good_morning(name)
    if hour < 18:
        return good_afternoon(name)
    return good_evening(name)
