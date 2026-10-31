from datetime import date

from colombia_utils import easter


def test_easter_sunday_known_years():
    assert easter(2024) == date(2024, 3, 31)
    assert easter(2025) == date(2025, 4, 20)
    assert easter(2026) == date(2026, 4, 5)
    assert easter(2038) == date(2038, 4, 25)  # latest possible date
    assert easter(2285) == date(2285, 3, 22)  # earliest possible date
