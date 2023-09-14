# Este bucle se ejecutará indefinidamente hasta que el usuario decida salir manualmente.
while True:
    # El programa solicita al usuario que ingrese un número positivo y lo almacena en la variable 'value'.
    value = int(input("Ingrese un numero positivo: "))
    print("Value: ", value)
    
    # Se verifica si 'value' es de tipo entero (int).
    a = isinstance(value, int)
    
    # Se verifica si 'a' es True (es decir, 'value' es un entero) y si 'value' es mayor que 0.
    if a == True and value > 0:
        # Si 'value' es un número entero positivo, se inicializa 'fact' a 1 para calcular el factorial.
        fact = 1
        
        # Se calcula el factorial de 'value' usando un bucle for.
        for i in range(1, value + 1):
            fact = fact * i
            
        # Se muestra el resultado del cálculo del factorial.
        print(f'El factorial de {value} es: ', fact)
    else:
        # Si 'value' no es un número entero positivo, se muestra un mensaje de error.
        print("Por favor, digite un numero positivo")

