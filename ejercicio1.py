#1.1 Escribe una función cuya firma sea multiple(n, m), y que tome dos enteros y devuelva True is n es un múltiplo de m,
# es decir n = m*i, para una algún entero i, o False en cualquier otro caso.

n=int(input("escribe un numero entero: "))
m=int(input("escribe un numero entero: "))
def multiplos(n,m):
    multiplos=n % m
    if multiplos==0:
        print(True)
    else:
        print(False)
    return multiplos