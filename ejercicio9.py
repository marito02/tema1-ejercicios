#1.9 Escribe una funcion que tome una secuencia de números y determine si todos los números en la secuencia son diferentes.

def num_dif(numeros):
    for numero in numeros:
        for i in numeros:
            if numero == i:
                print("hay dos numeros iguales")
            else:
                print("todos los numeros son diferentes")
numeros = [1,2,3,4]
num_dif(numeros)