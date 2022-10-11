#1.10 Escribe una función que tome dos listas a y b de longitud n de números enteros, y devuelva el producto escalar de a y b.
# Es decir, devuelva una vector c de longitud n tal que  c[i] = a[i] · b[i], para i = 0,...,n− 1.

def producto_escalar (lista1, lista2):
    result = []
    for i in range(len(lista1)):
        result.append[i] = lista1[i]*lista2[i]
    return result
lista1 = [1,2,3,4]
lista2 = [1,2,3,6]

producto_escalar = mult(lista1, lista2)