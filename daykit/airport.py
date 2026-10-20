from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class FlightSignal:
    label: str
    css_class: str
    sort_order: int


def movement_signal(direction: str, scheduled_time: datetime, checked_in: bool) -> FlightSignal:
    """Return a simple operational signal for an airport movement."""
    if direction not in {"arrival", "departure"}:
        raise ValueError("direction must be arrival or departure")

    now = datetime.now(tz=scheduled_time.tzinfo)
    minutes_until = int((scheduled_time - now).total_seconds() // 60)

    if direction == "departure" and not checked_in and minutes_until <= 45:
        return FlightSignal("Crew check-in needed", "danger", 0)
    if minutes_until < 0:
        return FlightSignal("Landed" if direction == "arrival" else "Departed", "muted", 3)
    if minutes_until <= 60:
        return FlightSignal("Boarding window", "warning", 1)
    return FlightSignal("On schedule", "success", 2)


def attendant_load(assignments_count: int, max_assignments: int = 4) -> str:
    """Describe how busy an attendant is for the current roster."""
    if assignments_count < 0:
        raise ValueError("assignments_count cannot be negative")
    if max_assignments <= 0:
        raise ValueError("max_assignments must be positive")

    ratio = assignments_count / max_assignments
    if ratio >= 1:
        return "Full roster"
    if ratio >= 0.5:
        return "Active roster"
    return "Light roster"
