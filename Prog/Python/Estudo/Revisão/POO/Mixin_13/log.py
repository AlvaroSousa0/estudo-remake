from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')
    

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')      


if __name__ == '__main__':
    lf = LogFileMixin()
    lf.log_error('Log Errado')
    lf.log_success('Log Successo')
    lp = LogPrintMixin()
    lp.log_error('Log Errado')
    lp.log_success('Log Successo')