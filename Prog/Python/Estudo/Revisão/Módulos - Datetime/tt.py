from datetime import datetime, timezone, timedelta


data_e_hora_atual = datetime.now()
diferenca = timedelta(hours=-3)
fuso_horario = timezone(diferenca)
horario_de_sao_paulo = data_e_hora_atual.astimezone(fuso_horario)
horario_de_sao_paulo_em_texto = horario_de_sao_paulo.strftime('%d/%m/%Y %H:%M')
print(horario_de_sao_paulo_em_texto)
