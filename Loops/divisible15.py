a = input("Digite el numero menor del rango: ")
a = int(a)
b = input("Digite el numero mayor del rango: ")
b = int(b)


for i in range(a, b): #Lo que hace este codigo es dentro de un rango pre establecido tomar unicamente los numeros que son divisibles de 15 y dan residuo 5#
    if (i%15) != 0:
        continue
    print(i)
