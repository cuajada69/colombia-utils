# Roadmap

Goal: one small, trustworthy library for the Colombian rules that apps keep re-implementing. Each item is tracked as an issue; estimates are rough.

| # | Item | Type | Estimate |
|---|---|---|---|
| [#1](https://github.com/cuajada69/colombia-utils/issues/1) | `add_business_days(d, n)` for legal and delivery deadlines | feature | ~2 h |
| [#2](https://github.com/cuajada69/colombia-utils/issues/2) | `is_valid_nit("800197268-4")` and NIT formatting | feature | ~2 h |
| [#3](https://github.com/cuajada69/colombia-utils/issues/3) | Validate and normalize Colombian phone numbers (mobile and 60X landlines) to E.164 | feature | ~3 h |
| [#4](https://github.com/cuajada69/colombia-utils/issues/4) | `format_cop(1234567)` → `$1.234.567` without depending on the system locale | feature | ~1.5 h |
| [#5](https://github.com/cuajada69/colombia-utils/issues/5) | Amounts in Spanish words for invoices ("un millón doscientos mil pesos") | feature | ~4 h |
| [#6](https://github.com/cuajada69/colombia-utils/issues/6) | DANE departments and municipalities with code lookup | feature | ~4 h |
| [#7](https://github.com/cuajada69/colombia-utils/issues/7) | Command line: `python -m colombia_utils festivos 2027`, `nit 800197268` | feature | ~3 h |
| [#8](https://github.com/cuajada69/colombia-utils/issues/8) | Export holidays as an iCalendar (.ics) file | feature | ~2 h |
| [#9](https://github.com/cuajada69/colombia-utils/issues/9) | Test holidays against official calendars for more years | test | ~2 h |
| [#10](https://github.com/cuajada69/colombia-utils/issues/10) | Publish to PyPI from GitHub Actions, add type information (`py.typed`) | release | ~2 h |
| [#11](https://github.com/cuajada69/colombia-utils/issues/11) | Usage examples tested with doctest and a short guide in Spanish | docs | ~2 h |

**Total: about 27 hours.**

## Suggested order

1. **Trust**: #9 (more official calendars) and #11 (tested examples).
2. **Most requested helpers**: #1, #2, #4.
3. **Bigger features**: #3, #5, #6, #8.
4. **Reach**: #7 and #10.

## Out of scope

- Storing or looking up real people's data (for example, querying the DIAN or the Registraduría).
- Runtime dependencies.
