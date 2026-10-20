def percentage(part: float, whole: float) -> float:
    """Return part as a percentage of whole."""
    if not isinstance(part, (int, float)):
        raise TypeError("part must be a number")

    if not isinstance(whole, (int, float)):
        raise TypeError("whole must be a number")

    if whole == 0:
        raise ValueError("whole cannot be zero")

    return (part / whole) * 100


def pomodoro_sessions(minutes: int, session_length: int = 25) -> int:
    """Return the number of full Pomodoro sessions in a study period."""
    if not isinstance(minutes, int):
        raise TypeError("minutes must be an integer")

    if not isinstance(session_length, int):
        raise TypeError("session_length must be an integer")

    if minutes < 0:
        raise ValueError("minutes cannot be negative")

    if session_length <= 0:
        raise ValueError("session_length must be greater than zero")

    return minutes // session_length
