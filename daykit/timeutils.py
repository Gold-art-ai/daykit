from datetime import datetime


def format_duration(seconds: int) -> str:
    """Convert seconds into a human-readable duration."""
    if not isinstance(seconds, int):
        raise TypeError("seconds must be an integer")

    if seconds < 0:
        raise ValueError("seconds cannot be negative")

    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []

    if hours:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds or not parts:
        parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

    return " ".join(parts)


def is_weekend(date: datetime | None = None) -> bool:
    """Return True if the supplied date/time falls on Saturday or Sunday."""
    if date is None:
        date = datetime.now()

    return date.weekday() >= 5
