def meal_time(hour: int) -> str:
    """Return a simple message based on the hour of the day."""
    if not isinstance(hour, int):
        raise TypeError("hour must be an integer")

    if not 0 <= hour <= 23:
        raise ValueError("hour must be between 0 and 23")

    if hour == 7:
        return "Breakfast time! Start your day with a nourishing meal."
    if hour == 10:
        return "Snack time! Take a short break and recharge."
    if hour == 12:
        return "Lunch time! Don't forget to have a balanced meal."
    if hour == 15:
        return "Snack time! A little break can help you recharge."
    if hour == 19:
        return "Dinner time! Time to refuel and relax."

    return "No scheduled meal right now. Keep going, and remember to take care of yourself!"
