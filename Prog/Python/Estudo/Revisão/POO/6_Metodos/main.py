class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    def set_user(self, user):
        self.user = user


    def set_password(self, password):
        self.password = password


    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


    @staticmethod
    def log(msg):
        print('LOG:', msg)

# Uso do Método de instância
c1 = Connection()
print(c1.user)
c1.set_user('Alvaro')
c1.set_password(2049234)
print(c1.user, c1.password)


# Uso do Método de classe
c2 = Connection.create_with_auth('Zé da manga', 'chavinho123')
print(c2.user)
print(c2.password)


# Uso do Método Estático
Connection.log('Mensagem de log.')