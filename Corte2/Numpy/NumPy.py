//////////////////////NUMPY//////////////////////////////////


------------------------NumPy Getting Started--------------------------------------
# Importa la biblioteca NumPy y le asigna el alias "np"
import numpy as np

# Crea un arreglo NumPy con los valores 1, 2, 3, 4, 5
arr = np.array([1, 2, 3, 4, 5])

# Imprime el arreglo en la consola
print(arr)

# Imprime el tipo de objeto de la variable arr, que debería ser un arreglo NumPy
print(type(arr))

-------------------------NumPy Creating Arrays------------------------------------------
--Ejemplo 1

#NumPy se utiliza para trabajar con matrices. El objeto de matriz en NumPy se llama ndarray.
#Podemos crear un ndarrayobjeto NumPy usando la array()función.

# Importa la biblioteca NumPy y le asigna el alias "np"
import numpy as np

# Crea un arreglo NumPy con los valores 1, 2, 3, 4, 5
arr = np.array([1, 2, 3, 4, 5])

# Imprime el arreglo en la consola
print(arr)

# Imprime el tipo de objeto de la variable arr, que debería ser un arreglo NumPy
print(type(arr))

-- Ejemplo 2
Matrices 0-D
Las matrices 0-D, o escalares, son los elementos de una matriz. Cada valor de una matriz es una matriz 0-D.
Crea una matriz 0-D con valor 42

import numpy as np

arr = np.array(42)

print(arr)

--Ejemplo 3
Matrices 1-D
Una matriz que tiene matrices 0-D como elementos se llama matriz unidimensional o 1-D.

Estas son las matrices más comunes y básicas.

Ejemplo
Cree una matriz 1-D que contenga los valores 1,2,3,4,5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

--Ejemplo 4
Matrices 2-D
Una matriz que tiene matrices 1-D como elementos se llama matriz 2-D.

Se utilizan a menudo para representar matrices o tensores de segundo orden.

NumPy tiene un submódulo completo dedicado a operaciones matriciales llamado numpy.mat

Ejemplo
Cree una matriz 2-D que contenga dos matrices con los valores 1,2,3 y 4,5,6:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

--Ejemplo 5
matrices 3-D

Una matriz que tiene matrices 2D (matrices) como elementos se llama matriz 3D.

Se utilizan a menudo para representar un tensor de tercer orden.

Ejemplo
Cree una matriz 3D con dos matrices 2D, ambas conteniendo dos matrices con los valores 1,2,3 y 4,5,6:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

--Ejemplo 6
¿Verificar número de dimensiones?
NumPy Arrays proporciona el ndimatributo que devuelve un número entero que nos dice cuántas dimensiones tiene la matriz.

Ejemplo
Compruebe cuántas dimensiones tienen las matrices:

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

---------------------------NumPy Array Indexing-------------------------------------------

La indexación de matrices es lo mismo que acceder a un elemento de matriz.

Puede acceder a un elemento de matriz consultando su número de índice.

Los índices en las matrices NumPy comienzan con 0, lo que significa que el primer elemento tiene el índice 0 y el segundo tiene el índice 1, etc.

--Ejemplo 1
Obtenga el primer elemento de la siguiente matriz:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

-Obtenga el segundo elemento de la siguiente matriz.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])

--Ejemplo 2
Ejemplo
Obtenga el tercer y cuarto elemento de la siguiente matriz y agréguelos.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

-Ejemplo 3

Acceder a matrices 2-D
Para acceder a elementos de matrices 2-D, podemos usar números enteros separados por comas que representan la dimensión y el índice del elemento.

Piense en matrices 2D como una tabla con filas y columnas, donde la dimensión representa la fila y el índice representa la columna.

Ejemplo 
Acceda al elemento en la primera fila, segunda columna:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

Ejemplo
Acceda al elemento en la 2.ª fila, 5.ª columna:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])

-Ejemplo 4
Acceda a matrices 3-D
Para acceder a elementos de matrices 3-D, podemos usar números enteros separados por comas que representan las dimensiones y el índice del elemento.

Ejemplo
Accede al tercer elemento de la segunda matriz de la primera matriz:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
Ejemplo explicado
arr[0, 1, 2]imprime el valor 6.

Y es por esto:

El primer número representa la primera dimensión, que contiene dos matrices:
[[1, 2, 3], [4, 5, 6]]
y:
[[7, 8, 9], [10, 11, 12]]
Desde seleccionamos 0, nos queda el primer array:
[[1, 2, 3], [4, 5, 6]]

El segundo número representa la segunda dimensión, que también contiene dos matrices:
[1, 2, 3]
y:
[4, 5, 6]
Como seleccionamos 1, nos queda la segunda matriz:
[4, 5, 6]

El tercer número representa la tercera dimensión, que contiene tres valores:
4
5
6
Como seleccionamos 2, terminamos con el tercer valor:
6

-Ejemplo 5
Indexación negativa
Utilice indexación negativa para acceder a una matriz desde el final.

Ejemplo
Imprime el último elemento de la segunda matriz:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

------------------------------NumPy Data Types----------------------------------

---Tipos de datos en Python---
Por defecto, Python tiene estos tipos de datos:

strings- se utiliza para representar datos de texto, el texto aparece entre comillas. por ejemplo "ABCD"
integer- Se utiliza para representar números enteros. por ejemplo -1, -2, -3
float- utilizado para representar números reales. por ejemplo, 1,2, 42,42
boolean- utilizado para representar Verdadero o Falso.
complex- utilizado para representar números complejos. por ejemplo, 1,0 + 2,0j, 1,5 + 2,5j

---Tipos de datos en NumPy---
NumPy tiene algunos tipos de datos adicionales y se refieren a tipos de datos con un carácter, como inúmeros enteros, unúmeros enteros sin signo, etc.

A continuación se muestra una lista de todos los tipos de datos en NumPy y los caracteres utilizados para representarlos.

i- número entero
b- booleano
u- entero sin signo
f- flotar
c- flotador complejo
m- delta de tiempo
M- fecha y hora
O- objeto
S- cadena
U- cadena unicode
V- fragmento fijo de memoria para otro tipo (nulo)

El objeto de matriz NumPy tiene una propiedad llamada dtype que devuelve el tipo de datos de la matriz:

-Ejemplo 1

Obtenga su propio servidor Python
Obtenga el tipo de datos de un objeto de matriz:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista
arr = np.array([1, 2, 3, 4])

# Imprimir el tipo de datos de la matriz utilizando el atributo 'dtype'
print(arr.dtype)

-Ejemplo 2

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de cadenas
arr = np.array(['apple', 'banana', 'cherry'])

# Imprimir el tipo de datos de la matriz utilizando el atributo 'dtype'
print(arr.dtype)

Crear matrices con un tipo de datos definido
Usamos la array()función para crear matrices, esta función puede tomar un argumento opcional: dtype que nos permite definir el tipo de datos esperado de los elementos de la matriz:

-Ejemplo 3

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de enteros con tipo de datos de cadena de bytes ('S')
arr = np.array([1, 2, 3, 4], dtype='S')

# Imprimir la matriz
print(arr)

# Imprimir el tipo de datos de la matriz utilizando el atributo 'dtype'
print(arr.dtype)

Para i, u, f y S también Upodemos definir el tamaño.

-Ejemplo 4
  
Cree una matriz con tipo de datos entero de 4 bytes:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de enteros con tipo de datos entero de 4 bytes ('i4')
arr = np.array([1, 2, 3, 4], dtype='i4')

# Imprimir la matriz
print(arr)

# Imprimir el tipo de datos de la matriz utilizando el atributo 'dtype'
print(arr.dtype)

   ¿Qué pasa si un valor no se puede convertir?
Si se proporciona un tipo en el que los elementos no se pueden convertir, NumPy generará un ValueError.

ValueError: en Python, ValueError se genera cuando el tipo de argumento pasado a una función es inesperado/incorrecto.

-Ejemplo 5

Una cadena que no es un número entero como 'a' no se puede convertir a un número entero (generará un error):

import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')

Conversión de tipos de datos en matrices existentes
La mejor manera de cambiar el tipo de datos de una matriz existente es hacer una copia de la matriz con el astype()método.

La astype()función crea una copia de la matriz y le permite especificar el tipo de datos como parámetro.

El tipo de datos se puede especificar usando una cadena, como 'f'flotante, 'i'entero, etc. o puede usar el tipo de datos directamente como floatflotante y intentero.

-Ejemplo 6

Cambie el tipo de datos de flotante a entero usando 'i'como valor de parámetro:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de números de punto flotante
arr = np.array([1.1, 2.1, 3.1])

# Convertir la matriz a un tipo de datos de enteros ('i')
newarr = arr.astype('i')

# Imprimir la nueva matriz
print(newarr)

# Imprimir el tipo de datos de la nueva matriz utilizando el atributo 'dtype'
print(newarr.dtype)

-Ejemplo 7
Cambie el tipo de datos de flotante a entero usando intcomo valor de parámetro:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de números de punto flotante
arr = np.array([1.1, 2.1, 3.1])

# Convertir la matriz a un tipo de datos de enteros (utilizando la función int)
newarr = arr.astype(int)

# Imprimir la nueva matriz
print(newarr)

# Imprimir el tipo de datos de la nueva matriz utilizando el atributo 'dtype'
print(newarr.dtype)

-Ejemplo 8
Cambie el tipo de datos de entero a booleano:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de enteros
arr = np.array([1, 0, 3])

# Convertir la matriz a un tipo de datos booleano
newarr = arr.astype(bool)

# Imprimir la nueva matriz
print(newarr)

# Imprimir el tipo de datos de la nueva matriz utilizando el atributo 'dtype'
print(newarr.dtype)

---------------------------NumPy Array Copy vs View--------------------------------

La diferencia entre copiar y ver
La principal diferencia entre una copia y una vista de una matriz es que la copia es una nueva matriz y la vista es solo una vista de la matriz original.

La copia posee los datos y cualquier cambio realizado en la copia no afectará la matriz original, y cualquier cambio realizado en la matriz original no afectará la copia.

La vista no posee los datos y cualquier cambio realizado en la vista afectará a la matriz original, y cualquier cambio realizado en la matriz original afectará a la vista.


-Ejemplo 1

Haga una copia, cambie la matriz original y muestre ambas matrices:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de enteros
arr = np.array([1, 2, 3, 4, 5])

# Realizar una copia de la matriz original
x = arr.copy()

# Modificar un elemento en la matriz original
arr[0] = 42

# Imprimir la matriz original después de la modificación
print(arr)

# Imprimir la copia de la matriz original
print(x)

nota: La copia NO DEBE verse afectada por los cambios realizados en la matriz original.

-Ejemplo 2

Cree una vista, cambie la matriz original y muestre ambas matrices:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de enteros
arr = np.array([1, 2, 3, 4, 5])

# Crear una vista de la matriz original
x = arr.view()

# Modificar un elemento en la matriz original
arr[0] = 42

# Imprimir la matriz original después de la modificación
print(arr)

# Imprimir la vista de la matriz original
print(x)

Nota: La vista DEBE verse afectada por los cambios realizados en la matriz original.

-Ejemplo 3

Cree una vista, cambie la vista y muestre ambas matrices:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de enteros
arr = np.array([1, 2, 3, 4, 5])

# Crear una vista de la matriz original
x = arr.view()

# Modificar un elemento en la vista
x[0] = 31

# Imprimir la matriz original después de la modificación en la vista
print(arr)

# Imprimir la vista de la matriz original
print(x)

Nota: La matriz original DEBE verse afectada por los cambios realizados en la vista.

Compruebe si Array posee sus datos
Como se mencionó anteriormente, las copias son propietarias de los datos y las vistas no son propietarias de los datos, pero ¿cómo podemos verificar esto?

Cada matriz NumPy tiene el atributo baseque devuelve Nonesi la matriz posee los datos.

De lo contrario, el base  atributo se refiere al objeto original.

-Ejemplo 4

Imprima el valor del atributo base para verificar si una matriz posee sus datos o no:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy a partir de una lista de enteros
arr = np.array([1, 2, 3, 4, 5])

# Crear una copia de la matriz original
x = arr.copy()

# Crear una vista de la matriz original
y = arr.view()

# Imprimir el atributo 'base' de la copia
print(x.base)

# Imprimir el atributo 'base' de la vista
print(y.base)


------------------------------NumPy Array Shape---------------------------------------

Forma de una matriz
La forma de una matriz es el número de elementos en cada dimensión.

Obtener la forma de una matriz
Las matrices NumPy tienen un atributo llamado shapeque devuelve una tupla y cada índice tiene el número de elementos correspondientes.

-Ejemplo 1
Imprima la forma de una matriz 2-D:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional a partir de una lista de listas
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Imprimir la forma (shape) de la matriz
print(arr.shape)
Nota: El ejemplo anterior devuelve (2, 4), lo que significa que la matriz tiene 2 dimensiones, donde la primera dimensión tiene 2 elementos y la segunda tiene 4.

-Ejemplo 2
Cree una matriz con 5 dimensiones usando ndminun vector con valores 1,2,3,4 y verifique que la última dimensión tenga el valor 4:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear un arreglo NumPy unidimensional con una dimensión mínima de 5
arr = np.array([1, 2, 3, 4], ndmin=5)

# Imprimir el arreglo
print(arr)

# Imprimir la forma (shape) del arreglo
print('shape of array :', arr.shape)

¿Qué representa la tupla de forma?
Los números enteros en cada índice indican la cantidad de elementos que tiene la dimensión correspondiente.

En el ejemplo anterior en el índice 4 tenemos el valor 4, por lo que podemos decir que la quinta (4 + 1) dimensión tiene 4 elementos.


--------------------------NumPy Array Reshaping-----------------------------










  
