#1.4 Escribe una función  que come una numero entero positivo n y devuelva la suma de los cuadrados  de los cuadrados de todos los enteros positivos 
# menores a n. 
# Ejemplo: n = 5, solución 4**2 + 3**2 + 2**2 + 1**1

n = int(input("escribe un numero: "))
for i in range (n):
    suma =sum(i**2)
    print(suma)
