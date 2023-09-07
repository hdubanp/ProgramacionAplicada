print("inserte numero menor del rango")

print("inserte numero mayor del rango")

for i in range(100, 301): #Lo que hace este codigo es dentro de un rango pre establecido tomar unicamente los numeros que son divisibles de 15 y dan residuo 5#
    if (i%15) != 0:
        continue
    print(i)
