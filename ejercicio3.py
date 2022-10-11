#1.3 Escribe una función cuya firma sea minmax(data), y que tome una secuencia de uno o mas números, y que devuelva el máximo y mínimo de la secuencia
# No se puede usar las funciones min o max para implementar la solución.
lista = list(2,5,7,1,0,4,3)
lista.sort(reverse=True)
print(lista[0])
print(lista[6])