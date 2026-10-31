from datetime import date

import pytest

from colombia_utils import business_days, easter, holidays, is_business_day, is_holiday


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


def test_is_holiday():
    assert is_holiday(date(2026, 10, 12))
    assert not is_holiday(date(2026, 10, 13))
    assert not is_holiday(date(2026, 4, 5))  # Easter Sunday itself is not a holiday


def test_is_business_day_excludes_weekends_and_holidays():
    assert is_business_day(date(2026, 10, 13))      # Tuesday
    assert not is_business_day(date(2026, 10, 12))  # Monday holiday
    assert not is_business_day(date(2026, 10, 17))  # Saturday
    assert not is_business_day(date(2026, 10, 18))  # Sunday


def test_business_days_counts_both_ends():
    # October 2026: 22 weekdays minus Día de la Raza
    assert business_days(date(2026, 10, 1), date(2026, 10, 31)) == 21
    assert business_days(date(2026, 10, 13), date(2026, 10, 13)) == 1


def test_business_days_across_years():
    # Dec 24 2026 (Thu) to Jan 4 2027 (Mon): Dec 24, 28, 29, 30, 31 and Jan 4
    assert business_days(date(2026, 12, 24), date(2027, 1, 4)) == 6


def test_business_days_rejects_reversed_range():
    with pytest.raises(ValueError):
        business_days(date(2026, 10, 31), date(2026, 10, 1))
