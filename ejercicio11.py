# 1.11 Escribe una función que cuente el numero de vocales en una un cadena de caracteres dada.

cadena="Que buen dia hace hoy"
contador_vocales=0
for i in cadena:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        contador_vocales+=1
        print(contador_vocales)
        