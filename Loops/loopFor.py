import time  # Importa el módulo 'time' para utilizar la función 'sleep'.

cadena = 'Python'  # Define una cadena de caracteres 'Python'.

# Itera a través de cada letra en la cadena 'cadena'.
for letra in cadena:
    if letra == 't':  # Comprueba si la letra actual es 't'.
        continue  # Si es 't', se salta la iteración actual y pasa a la siguiente letra.

    print(letra)  # Muestra la letra actual en la consola.

    # Pausa la ejecución del programa durante 1 segundo.
    time.sleep(1)

# El bucle for se completa después de iterar a través de todas las letras de 'cadena'.

