lista = []

"""Usando iteración con for"""

def almacenar():
    for item in range(10):
        lista.append(item)

    print("El valor de mi lista es: {}".format(lista))

def norepetir():

    lista.count()
    print("Mi lista no repetida es: {}".format(lista))

def ordenar():
    lista.sort()
    print("Mi lista ordenado de menor a mayor es: {}".format(lista))
    lista.reverse()

almacenar()
ordenar()
norepetir()