class MyError(Exception):
    ...


def levantar():
    exception_ = MyError('Deu erro aqui fera.')
    raise exception_

levantar()