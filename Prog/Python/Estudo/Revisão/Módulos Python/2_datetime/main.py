from datetime import datetime


data_str_data = '2024-09-28 10:04:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2024, 9, 27)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
