from string import Template
from datetime import datetime
from dados_email import meu_email, senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Álvaro Sousa', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Álvaro de Sousa Oliveira'
msg['to'] = meu_email
msg['subject'] = 'Atenção: esse é um email de teste.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, senha)
    smtp.send_message(msg)
    print('e-mail enviado com sucesso')
    