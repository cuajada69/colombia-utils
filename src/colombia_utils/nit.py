"""NIT (Número de Identificación Tributaria) check digit, as defined by the DIAN."""

# DIAN weights, applied from the rightmost digit
_WEIGHTS = (3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71)


def nit_check_digit(nit: str | int) -> int:
    """Check digit (dígito de verificación) of a NIT without its check digit.

    Dots and spaces are ignored. Raises ``ValueError`` for anything that is
    not 1 to 15 digits, including a hyphen, which usually means the check
    digit is already attached.
    """
    digits = str(nit).replace(".", "").replace(" ", "")
    if not (digits.isdigit() and digits.isascii() and len(digits) <= len(_WEIGHTS)):
        raise ValueError(f"a NIT must be 1 to {len(_WEIGHTS)} digits, got {nit!r}")
    remainder = sum(int(c) * w for c, w in zip(reversed(digits), _WEIGHTS)) % 11
    return remainder if remainder < 2 else 11 - remainder
