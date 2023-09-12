import random  # Importa el módulo random para generar números aleatorios

numbers_a = range(1, 13)  # Crea una secuencia de números del 1 al 12 y almacénalos en 'numbers_a'
numbers_b = [random.randint(1, 1000) for i in range(12)]  # Genera 12 números aleatorios entre 1 y 1000 y almacénalos en 'numbers_b'

for a, b in zip(numbers_a, numbers_b):  # Itera a través de los elementos de 'numbers_a' y 'numbers_b' al mismo tiempo
    print(f"Número {a}: {b}")  # Imprime el número 'a' junto con el número aleatorio correspondiente 'b'
