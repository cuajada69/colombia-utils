# colombia-utils

[![CI](https://github.com/cuajada69/colombia-utils/actions/workflows/ci.yml/badge.svg)](https://github.com/cuajada69/colombia-utils/actions/workflows/ci.yml) · **English** · [Español](README.es.md)

Small, dependency-free Python helpers for things every Colombian app ends up needing: **public holidays, business days and NIT check digits**.

For developers building invoicing, scheduling, payroll or e-commerce software for Colombia who are tired of hard-coding next year's holidays or copying the DIAN check-digit formula from a forum.

## Features

- **Public holidays for any year from 1984**, computed from the law instead of a hard-coded list: fixed dates, holidays moved to Monday by Ley 51 de 1983 ("Ley Emiliani") and the ones that depend on Easter. Names in Spanish.
- **Business days**: `is_business_day()` and `business_days(start, end)` (Monday to Friday, skipping holidays).
- **NIT check digit** (dígito de verificación) with the official DIAN weights.
- Pure standard library, Python 3.10+, fully tested.

## Install

Not on PyPI yet (see the [roadmap](ROADMAP.md)). Install from GitHub:

```bash
pip install git+https://github.com/cuajada69/colombia-utils
```

## Usage

```python
from datetime import date
from colombia_utils import holidays, is_holiday, business_days, nit_check_digit

holidays(2027)[:3]
# [(date(2027, 1, 1), 'Año Nuevo'), (date(2027, 1, 11), 'Reyes Magos'), (date(2027, 3, 22), 'San José')]

is_holiday(date(2027, 1, 11))                          # True: Reyes Magos moved to Monday
business_days(date(2027, 3, 1), date(2027, 3, 31))     # 20: both ends included
nit_check_digit("800.197.268")                         # 4
```

| Function | Returns |
|---|---|
| `holidays(year)` | Sorted list of `(date, name)`. Two holidays can share a date (June 30, 2025). Raises `ValueError` before 1984. |
| `is_holiday(d)` | `True` if `d` is a public holiday. |
| `is_business_day(d)` | `True` for Monday to Friday that is not a holiday. |
| `business_days(start, end)` | Business days from `start` to `end`, both included. |
| `easter(year)` | Easter Sunday (Gregorian). |
| `nit_check_digit(nit)` | Check digit of a NIT given without it. Accepts dots and spaces; rejects anything else. |

## How holidays are computed

| Rule | Holidays |
|---|---|
| Fixed date | Año Nuevo, Día del Trabajo, Independencia (Jul 20), Batalla de Boyacá (Aug 7), Inmaculada Concepción, Navidad |
| Moved to the next Monday (Ley 51 de 1983) | Reyes Magos, San José, San Pedro y San Pablo, Asunción, Día de la Raza, Todos los Santos, Independencia de Cartagena |
| Relative to Easter | Jueves and Viernes Santo; Ascensión, Corpus Christi and Sagrado Corazón (already on Monday) |

The tests check the result against the official 2025 and 2026 calendars.

## Development

```bash
pip install -e . pytest
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md). Planned work (validators, peso formatting, DANE codes, CLI, PyPI release) is in [ROADMAP.md](ROADMAP.md).

## License

MIT
