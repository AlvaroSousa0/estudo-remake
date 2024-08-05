from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem


    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: ', self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    mensagem_enviada = notificacao.enviar()
    
    if mensagem_enviada:
        print('Notificação enviada')
    else: 
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('Teste E-mail')
notificar(notificacao_email)


notificacao_sms = NotificacaoSMS('Teste SMS')
notificar(notificacao_sms)

