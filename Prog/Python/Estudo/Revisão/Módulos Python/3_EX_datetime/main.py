from datetime import datetime
from dateutil.relativedelta import relativedelta


fmt = '%d/%m/%Y' 
data = datetime.strptime('20/12/2020', fmt)
data_final = datetime.strptime('20/12/2025', fmt)
emprestimo = 1_000_000
parcelas = emprestimo / (5 * 12)

while data < data_final:
    print(data.strftime(fmt), f'R${parcelas:,.2f}')
    print()
    data += relativedelta(months=1)