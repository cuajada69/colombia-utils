"""Colombian public holidays (Ley 51 de 1983) and business days."""

from datetime import date, timedelta
from functools import lru_cache


def easter(year: int) -> date:
    """Easter Sunday of the Gregorian calendar (anonymous Gregorian algorithm)."""
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month, day = divmod(h + l - 7 * m + 114, 31)
    return date(year, month, day + 1)


# Holidays that always fall on their own date
_FIXED = [
    (1, 1, "Año Nuevo"),
    (5, 1, "Día del Trabajo"),
    (7, 20, "Día de la Independencia"),
    (8, 7, "Batalla de Boyacá"),
    (12, 8, "Inmaculada Concepción"),
    (12, 25, "Navidad"),
]

# Ley 51 de 1983 ("Ley Emiliani"): moved to the following Monday
_MOVED = [
    (1, 6, "Reyes Magos"),
    (3, 19, "San José"),
    (6, 29, "San Pedro y San Pablo"),
    (8, 15, "Asunción de la Virgen"),
    (10, 12, "Día de la Raza"),
    (11, 1, "Todos los Santos"),
    (11, 11, "Independencia de Cartagena"),
]

# Days after Easter Sunday; the last three already land on the Monday the law moves them to
_FROM_EASTER = [
    (-3, "Jueves Santo"),
    (-2, "Viernes Santo"),
    (43, "Ascensión del Señor"),
    (64, "Corpus Christi"),
    (71, "Sagrado Corazón"),
]


def _next_monday(d: date) -> date:
    return d + timedelta(days=-d.weekday() % 7)


def holidays(year: int) -> list[tuple[date, str]]:
    """Colombian public holidays of ``year`` as sorted ``(date, name)`` pairs.

    Two holidays can share a date (both are listed). Raises ``ValueError``
    before 1984, when the current holiday law took effect.
    """
    if year < 1984:
        raise ValueError(f"holidays are only defined from 1984 (Ley 51 de 1983), got {year}")
    sunday = easter(year)
    days = [(date(year, m, d), name) for m, d, name in _FIXED]
    days += [(_next_monday(date(year, m, d)), name) for m, d, name in _MOVED]
    days += [(sunday + timedelta(days=offset), name) for offset, name in _FROM_EASTER]
    return sorted(days)


@lru_cache(maxsize=None)
def _holiday_dates(year: int) -> frozenset[date]:
    return frozenset(d for d, _ in holidays(year))


def is_holiday(d: date) -> bool:
    """True if ``d`` is a Colombian public holiday."""
    return d in _holiday_dates(d.year)


def is_business_day(d: date) -> bool:
    """True if ``d`` is a Monday to Friday that is not a public holiday."""
    return d.weekday() < 5 and not is_holiday(d)


def business_days(start: date, end: date) -> int:
    """Number of business days from ``start`` to ``end``, both included."""
    if end < start:
        raise ValueError(f"end ({end}) is before start ({start})")
    return sum(is_business_day(start + timedelta(days=i)) for i in range((end - start).days + 1))
