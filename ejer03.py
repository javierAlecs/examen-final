import time


def funcionA(func):

    def calcular(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        total = time.time() - start
        print("Tiempo de ejecución es: {}".format(total))
        return result
    return calcular


@funcionA
def divison(a, b):
    time.sleep(1)
    resultado = a / b
    return resultado