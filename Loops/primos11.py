import time  # Importa el módulo 'time' para medir el tiempo de ejecución.

inicio = time.time()  # Registra el tiempo de inicio de la ejecución del programa.

# Solicita al usuario ingresar el número menor y mayor del rango y los almacena en las variables 'a' y 'b'.
a = input("Digite el numero menor del rango: ")
a = int(a)
b = input("Digite el numero mayor del rango: ")
b = int(b)

# Itera a través de todos los números en el rango desde 'a' hasta 'b-1'.
for i in range(a, b):
    conta = 0  # Inicializa el contador 'conta' a 0 para contar los divisores del número 'i'.
    
    # Itera a través de todos los números desde 1 hasta 'i'.
    for n in range(1, i+1):
        residue = i % n  # Calcula el residuo de la división de 'i' entre 'n'.
        
        # Si el residuo es 0, significa que 'n' es un divisor de 'i'.
        if residue == 0:
            conta = conta + 1  # Incrementa el contador 'conta' en 1 para contar los divisores.

    # Si 'conta' es igual a 2, significa que 'i' solo tiene dos divisores (1 y él mismo) y, por lo tanto, es primo.
    if conta == 2:
        print(f'{i} es un primo')
        print("\n")  # Agrega una línea en blanco después de imprimir el número primo.

fin = time.time()  # Registra el tiempo de finalización de la ejecución del programa.
print("t = ", (fin - inicio) * 1000)  # Calcula y muestra el tiempo de ejecución en milisegundos.
