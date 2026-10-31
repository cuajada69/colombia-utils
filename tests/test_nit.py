import pytest

from colombia_utils import nit_check_digit


def test_check_digit_of_public_nits():
    assert nit_check_digit("800197268") == 4  # DIAN
    assert nit_check_digit("899999068") == 1  # Ecopetrol
    assert nit_check_digit("890903938") == 8  # Bancolombia


def test_check_digit_ignores_dots_and_spaces():
    assert nit_check_digit("800.197.268") == 4
    assert nit_check_digit(" 800 197 268 ") == 4


def test_check_digit_accepts_int():
    assert nit_check_digit(800197268) == 4


def test_remainder_zero_or_one_is_used_as_is():
    assert nit_check_digit("15") == 0  # 1*7 + 5*3 = 22, remainder 0
    assert nit_check_digit("4") == 1   # 4*3 = 12, remainder 1
    assert nit_check_digit("8") == 9   # 8*3 = 24, remainder 2 -> 11 - 2


@pytest.mark.parametrize("bad", ["", "abc", "800-197-268", "1234567890123456", "-5"])
def test_invalid_input_is_rejected(bad):
    with pytest.raises(ValueError):
        nit_check_digit(bad)
