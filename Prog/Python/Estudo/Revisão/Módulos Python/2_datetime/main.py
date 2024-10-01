from datetime import datetime
# from pytz import timezone
from dateutil.relativedelta import relativedelta


# data_str_data = '2024-09-28 10:04:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2024, 9, 27)
# data = datetime.strptime(data_str_data, data_str_fmt)
# data = datetime.now(timezone('America/Sao_Paulo'))
# print(data)

# contador_timestamp = 30
# i = 0

# while i < contador_timestamp:
#     data = datetime.now()
#     print(data.timestamp())
#     print(data.fromtimestamp(data.timestamp()))
#     i += 1

# delta = relativedelta(data_fim, data_inicio)
# print(delta.years, delta.days)
# print(data_inicio)
# print(data_fim)
# print(data_inicio > data_fim)
# print(data_fim == data_inicio)
# print(data_fim > data_inicio)
# print(data_fim - data_inicio)
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1994 03:42:19', fmt)
data_fim = datetime.strptime('28/02/2052 14:26:57', fmt)
data_p = datetime.strptime('2024-09-30 21:30:40', '%Y-%m-%d %H:%M:%S')

print(data_p)
print(data_p.strftime(fmt))