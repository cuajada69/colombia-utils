# colombia-utils

[English](README.md) · **Español**

Utilidades pequeñas en Python, sin dependencias, para lo que toda aplicación colombiana termina necesitando: **festivos, días hábiles y dígito de verificación del NIT**.

Para quien desarrolla software de facturación, agendamiento, nómina o comercio electrónico en Colombia y está cansado de escribir a mano los festivos del próximo año o copiar la fórmula del dígito de verificación de un foro.

## Qué hace

- **Festivos de cualquier año desde 1984**, calculados según la ley y no copiados de una lista: fechas fijas, los que se corren al lunes por la Ley 51 de 1983 (Ley Emiliani) y los que dependen de la Semana Santa.
- **Días hábiles**: `is_business_day()` y `business_days(inicio, fin)` (lunes a viernes, sin festivos).
- **Dígito de verificación del NIT** con los pesos oficiales de la DIAN.
- Solo usa la biblioteca estándar, Python 3.10+, con pruebas.

## Instalación

Todavía no está en PyPI (mira el [roadmap](ROADMAP.md)). Se instala desde GitHub:

```bash
pip install git+https://github.com/cuajada69/colombia-utils
```

## Uso

```python
from datetime import date
from colombia_utils import holidays, is_holiday, business_days, nit_check_digit

holidays(2027)[:3]
# [(date(2027, 1, 1), 'Año Nuevo'), (date(2027, 1, 11), 'Reyes Magos'), (date(2027, 3, 22), 'San José')]

is_holiday(date(2027, 1, 11))                          # True: Reyes Magos pasa al lunes
business_days(date(2027, 3, 1), date(2027, 3, 31))     # 20: cuenta ambos extremos
nit_check_digit("800.197.268")                         # 4
```

Las funciones tienen nombres en inglés y los festivos vienen con su nombre en español. La tabla completa de funciones está en el [README en inglés](README.md#usage).

## Licencia

MIT
