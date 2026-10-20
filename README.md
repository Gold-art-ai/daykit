# DayKit

A lightweight, dependency-free Python toolkit for everyday routines, time utilities, and simple productivity helpers.

## Features

- **Time-aware greetings** that change with the hour of the day
- **Meal-time messages** for breakfast, lunch, and dinner
- **Human-readable durations**, such as seconds to "2 min 5 s"
- **Weekend detection** for any date
- **Percentage calculations** with input validation
- **Airport helpers** for flight and attendant status (`daykit.airport`)
- Fully type-hinted, with no third-party dependencies

## Installation

> **Note:** `daykit` is currently published on [TestPyPI](https://test.pypi.org/project/daykit/). Install it with:

```bash
pip install -i https://test.pypi.org/simple/ daykit
```

Requires Python 3.9 or newer.

## Quick Start

```python
from daykit import (
    good_morning,
    meal_time,
    get_greeting,
    format_duration,
    is_weekend,
    percentage,
)

print(good_morning("Ishara"))       # a morning greeting for Name
print(meal_time(12))                # the meal message for 12:00
print(get_greeting("Ishara", 18))   # a greeting suited to 18:00
print(format_duration(125))         # 125 seconds in readable form
print(is_weekend())                 # True or False for today
print(percentage(45, 60))           # 45 as a percentage of 60 -> 75.0
```

## API Overview

| Function | Description |
|---|---|
| `good_morning(name)` | Morning greeting for `name` |
| `good_afternoon(name)` | Afternoon greeting for `name` |
| `good_evening(name)` | Evening greeting for `name` |
| `get_greeting(name, hour)` | Picks the right greeting for the given hour (0-23) |
| `meal_time(hour)` | Returns a meal-time message for the given hour |
| `format_duration(seconds)` | Converts seconds into a human-readable string |
| `is_weekend(date=None)` | `True` if the date (default: today) is Saturday or Sunday |
| `percentage(part, whole)` | Returns `part` as a percentage of `whole` |

Invalid input, such as an hour outside 0-23 or a `whole` of zero, raises a `ValueError`.

## Development

```bash
git clone https://github.com/GITHUB_USERNAME/daykit.git
cd daykit
python -m venv .venv
```

Activate the environment:

| Windows | macOS / Linux |
|---|---|
| `.venv\Scripts\activate` | `source .venv/bin/activate` |

Then install in editable mode and run the tests:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
pytest
```

## Building the Package

```bash
python -m pip install build
python -m build
```

The wheel and source archive are written to `dist/`.

## Demo: Airport Flow (Django)

The repository also contains a small Django project that uses `daykit.airport`. It is for demonstration only and is not installed with the package.

| Part | Purpose |
|---|---|
| `airportflow` | The Django project |
| `crewlog` | The app for airport movement records |
| `daykit.airport` | The package module the app builds on |

It includes CRUD screens, related tables, model inheritance, a many-to-many relationship through `CrewAssignment`, static CSS, and plain JavaScript.

### Run the demo

From the repository root, with a virtual environment activated:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_airport
python manage.py runserver
```

Open <http://127.0.0.1:8000/>.

### Admin and roles

```bash
python manage.py createsuperuser
python manage.py setup_airport_roles
```

Log in at <http://127.0.0.1:8000/admin/> with the superuser, then add staff users to one of these groups:

| Group | Access |
|---|---|
| Airport Manager | Full access to airport records |
| Flight Dispatcher | Manage flights, gates, and crew assignments |
| Crew Supervisor | Manage attendants and crew assignments |
| Read Only Operations | View records without editing |

Other useful commands: `python manage.py test` and `python manage.py makemigrations`.

## License

MIT License. See [LICENSE](LICENSE).