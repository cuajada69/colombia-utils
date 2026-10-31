from datetime import date

import pytest

from colombia_utils import easter, holidays


def test_easter_sunday_known_years():
    assert easter(2024) == date(2024, 3, 31)
    assert easter(2025) == date(2025, 4, 20)
    assert easter(2026) == date(2026, 4, 5)
    assert easter(2038) == date(2038, 4, 25)  # latest possible date
    assert easter(2285) == date(2285, 3, 22)  # earliest possible date


def test_holidays_2026_match_official_calendar():
    # Official 2026 calendar: Emiliani holidays moved to Monday, Easter on April 5
    assert [d for d, _ in holidays(2026)] == [
        date(2026, 1, 1), date(2026, 1, 12), date(2026, 3, 23), date(2026, 4, 2),
        date(2026, 4, 3), date(2026, 5, 1), date(2026, 5, 18), date(2026, 6, 8),
        date(2026, 6, 15), date(2026, 6, 29), date(2026, 7, 20), date(2026, 8, 7),
        date(2026, 8, 17), date(2026, 10, 12), date(2026, 11, 2), date(2026, 11, 16),
        date(2026, 12, 8), date(2026, 12, 25),
    ]


def test_holidays_have_spanish_names():
    names = dict(holidays(2026))
    assert names[date(2026, 10, 12)] == "Día de la Raza"
    assert names[date(2026, 4, 3)] == "Viernes Santo"


def test_two_holidays_can_fall_on_the_same_monday():
    # 2025: Sagrado Corazón and San Pedro y San Pablo were both moved to June 30
    same_day = [name for d, name in holidays(2025) if d == date(2025, 6, 30)]
    assert same_day == ["Sagrado Corazón", "San Pedro y San Pablo"]
    assert len(holidays(2025)) == 18


def test_holidays_before_ley_emiliani_are_rejected():
    with pytest.raises(ValueError):
        holidays(1983)
