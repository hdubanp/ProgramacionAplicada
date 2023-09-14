for i in range(1, 6):
    # Este bucle while está anidado dentro del bucle for.
    while i <= 4:
        i += 1  # Incrementa el valor de 'i' en 1 en cada iteración del bucle while.
        print(i)  # Imprime el valor actual de 'i'.

    # Una vez que 'i' es mayor que 4, se sale del bucle while.
    # Luego, se ejecuta la siguiente iteración del bucle for (si corresponde).

    break  # Después de la primera iteración del bucle for, se utiliza 'break' para salir del bucle for.

# Como resultado, este código imprimirá solo una serie de números 2, 3, 4, 5 y luego se detendrá.
