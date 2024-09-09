class CallMe:
    def __init__(self,phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'Está chamando', self.phone)
call1 = CallMe('1234423432323')
call1('João')