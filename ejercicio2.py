#1.2  Escribe una función cuya firma sea even(k), y que tome un valor entero y devuelva True is k es par o False en otro caso.

def even(k):
    k=int(input("escribe un numero entero: "))
    if k % 2==0:
        print(True)
    else:
        print(False)
    return even