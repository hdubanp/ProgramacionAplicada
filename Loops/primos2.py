a = 1  # Inicializa la variable 'a' con el valor 1

# Solicita al usuario ingresar un valor y lo convierte en un número entero
value = input('Ingrese un valor: ')
value = int(value)

while a == 1:  # Inicia un bucle while que se ejecutará mientras 'a' sea igual a 1
    for i in range(1, value + 1):  # Inicia un bucle for que recorre los números del 1 hasta el valor ingresado por el usuario
        conta = 0  # Inicializa la variable 'conta' en 0

        # Realiza un bucle for interno para verificar si 'i' es primo contando sus divisores
        for n in range(1, i + 1):
            residue = i % n  # Calcula el residuo de la división de 'i' entre 'n'
            if residue == 0:
                conta = conta + 1  # Si el residuo es 0, aumenta el contador 'conta'

    if conta == 2:
        print(f'{i} es un primo: ')  # Si 'conta' es igual a 2, significa que 'i' es primo y se imprime
        print("\n")
    else:
        print(f'{i} NOOO es un primo: ')  # Si 'conta' no es igual a 2, 'i' no es primo y se imprime
        print("\n")

    print('Do you want to continue?. Press 1 to do that: ')  # Pregunta al usuario si desea continuar
    a = input()
    a = int(a)

    if a != 1:  # Si 'a' no es igual a 1, sale del bucle while
        break

    # Solicita nuevamente al usuario ingresar un valor y lo convierte en un número entero
    value = input('Ingrese un valor: ')
    value = int(value)
