import calendar 
import locale

locale.setlocale(locale.LC_ALL, '')


print(calendar.calendar(2024))
# print(calendar.month(2019, 6))
# print(calendar.monthrange(2024, 10))
# print(list(enumerate(calendar.day_name)))

# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2024, 10)
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2024, 10, ultimo_dia)])
