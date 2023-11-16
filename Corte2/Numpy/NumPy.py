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

Reformando matrices
Reformar significa cambiar la forma de una matriz.

La forma de una matriz es el número de elementos en cada dimensión.

Al remodelar podemos agregar o eliminar dimensiones o cambiar la cantidad de elementos en cada dimensión.

Reformar de 1-D a 2-D

-Ejemplo 1
Convierta la siguiente matriz 1D con 12 elementos en una matriz 2D.

La dimensión más externa tendrá 4 matrices, cada una con 3 elementos:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz 1D con 12 elementos
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Remodelar (reshape) la matriz 1D en una matriz 2D con 4 filas y 3 columnas
newarr = arr.reshape(4, 3)

# Imprimir la matriz 2D resultante
print(newarr)

Reformar de 1-D a 3-D

-Ejemplo 2
Convierta la siguiente matriz 1D con 12 elementos en una matriz 3D.

La dimensión más externa tendrá 2 matrices que contienen 3 matrices, cada una con 2 elementos:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz 1D con 12 elementos
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Remodelar (reshape) la matriz 1D en una matriz 3D con dimensiones 2x3x2
newarr = arr.reshape(2, 3, 2)

# Imprimir la matriz 3D resultante
print(newarr)

¿Podemos remodelarnos en cualquier forma?
Sí, siempre y cuando los elementos necesarios para remodelar sean iguales en ambas formas.

Podemos remodelar una matriz 1D de 8 elementos en una matriz 2D de 4 elementos en 2 filas, 
pero no podemos remodelarla en una matriz 2D de 3 elementos y 3 filas,
ya que eso requeriría 3x3 = 9 elementos.

-Ejemplo 3
Intente convertir una matriz 1D con 8 elementos en una matriz 2D con 3 elementos en cada dimensión (generará un error):

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)

-Ejemplo 4
Compruebe si la matriz devuelta es una copia o una vista:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz 1D con 8 elementos
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Remodelar (reshape) la matriz 1D en una matriz 2D de dimensiones 2x4
reshaped_arr = arr.reshape(2, 4)

# Imprimir el atributo 'base' de la matriz resultante
print(reshaped_arr.base)
El ejemplo anterior devuelve la matriz original, por lo que es una vista.

Dimensión desconocida
Se le permite tener una dimensión "desconocida".

Lo que significa que no es necesario especificar un número exacto para una de las dimensiones en el método de remodelación.

Pase -1como valor y NumPy calculará este número por usted.

-Ejemplo 5
Convierta una matriz 1D con 8 elementos en una matriz 3D con elementos 2x2:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz 1D con 8 elementos
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Remodelar (reshape) la matriz 1D en una matriz 3D con dimensiones 2x2x(-1)
newarr = arr.reshape(2, 2, -1)

# Imprimir la matriz 3D resultante
print(newarr)

Nota: No podemos pasar -1a más de una dimensión.

Aplanando las matrices
Aplanar una matriz significa convertir una matriz multidimensional en una matriz 1D.

Podemos usar reshape(-1)para hacer esto.

-Ejemplo 6
Convierta la matriz en una matriz 1D:

  # Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz 2D
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Remodelar (reshape) la matriz 2D en una matriz 1D utilizando -1
newarr = arr.reshape(-1)

# Imprimir la matriz 1D resultante
print(newarr)

Nota: Hay muchas funciones para cambiar las formas de las matrices en numpy flatteny raveltambién para reorganizar los elementos rot90, 
etc. Estas se flipencuentran en la sección Intermedia a Avanzada de numpy.fliplrflipud

--------------------------NumPy Array Iterating------------------------------

Iterando matrices
Iterar significa recorrer elementos uno por uno.

Mientras tratamos con matrices multidimensionales en numpy, podemos hacerlo usando forun bucle básico de Python.

Si iteramos en una matriz 1-D, pasará por cada elemento uno por uno.

-Ejemplo 1
Itere sobre los elementos de la siguiente matriz 1-D:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3])

# Iterar sobre cada elemento de la matriz e imprimirlo
for x in arr:
  print(x)

Iterando matrices 2-D
En una matriz 2-D, pasará por todas las filas.

-Ejemplo 2
Itere sobre los elementos de la siguiente matriz 2-D:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Iterar sobre cada fila de la matriz e imprimirla
for x in arr:
  print(x)

Si iteramos en una matriz n -D, pasará por la dimensión n-1 una por una.

Para devolver los valores reales, los escalares, tenemos que iterar las matrices en cada dimensión.

-Ejemplo 3
Iterar sobre cada elemento escalar de la matriz 2-D:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Iterar sobre cada fila de la matriz
for x in arr:
  # Iterar sobre cada elemento en la fila e imprimirlo
  for y in x:
    print(y)
Iterando matrices 3-D
En una matriz 3-D, pasará por todas las matrices 2-D.

-Ejemplo 4
Itere sobre los elementos de la siguiente matriz 3D:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy tridimensional
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Iterar sobre cada "capa" de la matriz e imprimirla
for x in arr:
  print(x)
Para devolver los valores reales, los escalares, tenemos que iterar las matrices en cada dimensión.

-Ejemplo 5
Iterar hasta los escalares:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy tridimensional
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Iterar sobre cada "capa" de la matriz
for x in arr:
  # Iterar sobre cada fila en la capa
  for y in x:
    # Iterar sobre cada elemento en la fila e imprimirlo
    for z in y:
      print(z)

Iterando matrices usando nditer()
La función nditer()es una función de ayuda que se puede utilizar desde iteraciones muy básicas hasta iteraciones muy avanzadas. 
Resuelve algunos problemas básicos que enfrentamos en la iteración, repasémoslo con ejemplos.

Iterando en cada elemento escalar
En los bucles básicos for, al iterar a través de cada escalar de una matriz, 
necesitamos usar n for bucles que pueden ser difíciles de escribir para matrices con una dimensionalidad muy alta.

-Ejemplo 6
Itere a través de la siguiente matriz 3-D:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy tridimensional
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Utilizar np.nditer() para iterar sobre todos los elementos de la matriz
for x in np.nditer(arr):
  print(x)

Matriz iterativa con diferentes tipos de datos
Podemos usar op_dtypesun argumento y pasarle el tipo de datos esperado para cambiar el tipo de datos de los elementos mientras iteramos.
NumPy no cambia el tipo de datos del elemento en el lugar (donde el elemento está en una matriz), 
por lo que necesita otro espacio para realizar esta acción, ese espacio adicional se llama buffer, 
y para habilitarlo nditer()pasamos flags=['buffered'].

-Ejemplo 7
Iterar a través de la matriz como una cadena:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3])

# Utilizar np.nditer() para iterar sobre los elementos de la matriz
# con opciones adicionales 'buffered' y op_dtypes=['S']
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

Iterando con diferentes tamaños de paso
Podemos usar filtrado y seguido de iteración.

-Ejemplo 8
Itere a través de cada elemento escalar de la matriz 2D omitiendo 1 elemento:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Utilizar np.nditer() para iterar sobre una vista específica de la matriz
for x in np.nditer(arr[:, ::2]):
  print(x)

Iteración enumerada usando ndenumerate()
Enumeración significa mencionar el número de secuencia de algo uno por uno.

A veces requerimos el índice correspondiente del elemento mientras iteramos, 
el ndenumerate()método se puede utilizar para esos casos de uso.

-Ejemplo 9
Enumere los siguientes elementos de matrices 1D:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3])

# Utilizar np.ndenumerate() para iterar sobre los índices y elementos de la matriz
for idx, x in np.ndenumerate(arr):
  print(idx, x)

-Ejemplo 10
Enumere los siguientes elementos de la matriz 2D:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Utilizar np.ndenumerate() para iterar sobre los índices y elementos de la matriz
for idx, x in np.ndenumerate(arr):
  print(idx, x)

----------------------------------NumPy Joining Array---------------------------------
Unirse a matrices NumPy
Unir significa poner el contenido de dos o más matrices en una sola matriz.

En SQL unimos tablas en función de una clave, mientras que en NumPy unimos arrays por ejes.

Pasamos una secuencia de arrays que queremos unir a la concatenate()función, junto con el eje. 
Si el eje no se pasa explícitamente, se toma como 0.

-Ejemplo 1
Unir dos matrices

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear dos matrices NumPy unidimensionales
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenar las dos matrices utilizando np.concatenate()
arr = np.concatenate((arr1, arr2))

# Imprimir la matriz resultante
print(arr)

-Ejemplo 2
Une dos matrices 2-D a lo largo de filas (eje=1):

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear dos matrices NumPy bidimensionales
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Concatenar las dos matrices a lo largo del eje 1 utilizando np.concatenate()
arr = np.concatenate((arr1, arr2), axis=1)

# Imprimir la matriz resultante
print(arr)

Unir matrices usando funciones de pila
El apilamiento es lo mismo que la concatenación, la única diferencia es que el apilamiento se realiza a lo largo de un nuevo eje.
Podemos concatenar dos matrices 1-D a lo largo del segundo eje, lo que daría como resultado colocarlas una sobre la otra, 
es decir. apilado.
Pasamos una secuencia de arrays que queremos unir al stack()método junto con el eje. 
Si el eje no se pasa explícitamente, se toma como 0.

-Ejemplo 3

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear dos matrices NumPy unidimensionales
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Apilar las dos matrices a lo largo del nuevo eje creado utilizando np.stack()
arr = np.stack((arr1, arr2), axis=1)

# Imprimir la matriz resultante
print(arr)

Apilado a lo largo de filas
NumPy proporciona una función auxiliar: hstack() apilar a lo largo de filas.

-Ejemplo 4
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear dos matrices NumPy unidimensionales
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Apilar las dos matrices horizontalmente utilizando np.hstack()
arr = np.hstack((arr1, arr2))

# Imprimir la matriz resultante
print(arr)

Apilado a lo largo de columnas
NumPy proporciona una función auxiliar: vstack()  apilar a lo largo de columnas.

-Ejemplo 5

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear dos matrices NumPy unidimensionales
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Apilar las dos matrices verticalmente utilizando np.vstack()
arr = np.vstack((arr1, arr2))

# Imprimir la matriz resultante
print(arr)

Apilado a lo largo de la altura (profundidad)
NumPy proporciona una función auxiliar: dstack() apilar a lo largo de la altura, que es lo mismo que la profundidad.

-Ejemplo 6

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear dos matrices NumPy unidimensionales
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Apilar las dos matrices a lo largo del tercer eje utilizando np.dstack()
arr = np.dstack((arr1, arr2))

# Imprimir la matriz resultante
print(arr)

------------------------------NumPy Splitting Array---------------------------

Dividir matrices NumPy
Dividir es una operación inversa a unir.

La unión fusiona varias matrices en una y la división divide una matriz en varias.

Usamos array_split()para dividir matrices, le pasamos la matriz que queremos dividir y el número de divisiones.

-Ejemplo 1
Divida la matriz en 3 partes:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3, 4, 5, 6])

# Dividir la matriz en tres partes utilizando np.array_split()
newarr = np.array_split(arr, 3)

# Imprimir las matrices resultantes
print(newarr)

Nota: El valor de retorno es una lista que contiene tres matrices.

Si la matriz tiene menos elementos de los necesarios, se ajustará desde el final en consecuencia.

-Ejemplo 2
Divida la matriz en 4 partes:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3, 4, 5, 6])

# Dividir la matriz en cuatro partes utilizando np.array_split()
newarr = np.array_split(arr, 4)

# Imprimir las matrices resultantes
print(newarr)

Nota: También tenemos el método split()disponible, 
pero no ajustará los elementos cuando haya menos elementos en la matriz fuente para dividir como en el ejemplo anterior, 
array_split()funcionó correctamente pero split()fallaría.

Dividir en matrices
El valor de retorno del array_split()método es una matriz que contiene cada una de las divisiones como una matriz.

Si divide una matriz en 3 matrices, puede acceder a ellas desde el resultado como cualquier elemento de la matriz:

-Ejemplo 3
Acceda a las matrices divididas:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3, 4, 5, 6])

# Dividir la matriz en tres partes utilizando np.array_split()
newarr = np.array_split(arr, 3)

# Imprimir cada parte por separado
print(newarr[0])
print(newarr[1])
print(newarr[2])

División de matrices 2-D
Utilice la misma sintaxis al dividir matrices 2D.

Utilice el array_split()método, pase la matriz que desea dividir y la cantidad de divisiones que desea realizar.

-Ejemplo 4
Divida la matriz 2-D en tres matrices 2-D.
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# Dividir la matriz en tres partes a lo largo del eje 0 utilizando np.array_split()
newarr = np.array_split(arr, 3)

# Imprimir las matrices resultantes
print(newarr)

El ejemplo anterior devuelve tres matrices 2-D.

Veamos otro ejemplo, esta vez cada elemento de las matrices 2D contiene 3 elementos.

-Ejemplo 5
Divida la matriz 2-D en tres matrices 2-D.
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Dividir la matriz en tres partes a lo largo del eje 0 utilizando np.array_split()
newarr = np.array_split(arr, 3)

# Imprimir las matrices resultantes
print(newarr)

El ejemplo anterior devuelve tres matrices 2-D.

Además, puede especificar en qué eje desea realizar la división.

El siguiente ejemplo también devuelve tres matrices 2D, pero están divididas a lo largo de la fila (eje=1).

-Ejemplo 6
Divida la matriz 2D en tres matrices 2D a lo largo de filas.

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Dividir la matriz en tres partes a lo largo del eje 1 utilizando np.array_split()
newarr = np.array_split(arr, 3, axis=1)

# Imprimir las matrices resultantes
print(newarr)

Una solución alternativa es usar hsplit()el opuesto de hstack()

-Ejemplo 7
Utilice el hsplit()método para dividir la matriz 2D en tres matrices 2D a lo largo de filas.

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Dividir la matriz en tres partes a lo largo del eje 1 utilizando np.hsplit()
newarr = np.hsplit(arr, 3)

# Imprimir las matrices resultantes
print(newarr)

Nota: Hay alternativas similares a vstack()y dstack()disponibles como vsplit()y dsplit().

----------------------------NumPy Searching Arrays---------------------------------------

Buscando matrices
Puede buscar en una matriz un valor determinado y devolver los índices que coinciden.

Para buscar una matriz, utilice el where()método.

-Ejemplo 1
Encuentre los índices donde el valor es 4:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3, 4, 5, 4, 4])

# Encontrar las posiciones donde el valor es igual a 4 utilizando np.where()
x = np.where(arr == 4)

# Imprimir las posiciones encontradas
print(x)

El ejemplo anterior devolverá una tupla:(array([3, 5, 6],)

Lo que significa que el valor 4 está presente en los índices 3, 5 y 6.

-Ejemplo 2
Encuentre los índices donde los valores son pares:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Encontrar las posiciones donde los elementos son pares utilizando np.where()
x = np.where(arr % 2 == 0)

# Imprimir las posiciones encontradas
print(x)

-Ejemplo 3
Encuentre los índices donde los valores son impares:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy unidimensional
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Encontrar las posiciones donde los elementos son impares utilizando np.where()
x = np.where(arr % 2 == 1)

# Imprimir las posiciones encontradas
print(x)

Búsqueda ordenada
Existe un método llamado searchsorted()que realiza una búsqueda binaria en la matriz y devuelve el índice donde se insertaría el valor especificado para mantener el orden de búsqueda.

Se supone que el searchsorted()método se utiliza en matrices ordenadas.

-Ejemplo 4
Encuentre los índices donde se debe insertar el valor 7:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy ordenada
arr = np.array([6, 7, 8, 9])

# Encontrar el índice donde debería insertarse el valor 7 utilizando np.searchsorted()
x = np.searchsorted(arr, 7)

# Imprimir el índice encontrado
print(x)

Ejemplo explicado: el número 7 debe insertarse en el índice 1 para seguir siendo el orden de clasificación.

El método inicia la búsqueda desde la izquierda y devuelve el primer índice donde el número 7 ya no es mayor que el siguiente valor.

Buscar desde el lado derecho
De forma predeterminada, se devuelve el índice más a la izquierda, 
pero side='right´ en su lugar podemos devolver el índice más a la derecha.

-Ejemplo 5
Encuentre los índices donde se debe insertar el valor 7, comenzando desde la derecha:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy ordenada
arr = np.array([6, 7, 8, 9])

# Encontrar el índice derecho donde debería insertarse el valor 7 utilizando np.searchsorted()
x = np.searchsorted(arr, 7, side='right')

# Imprimir el índice derecho encontrado
print(x)

Ejemplo explicado: el número 7 debe insertarse en el índice 2 para seguir siendo el orden de clasificación.

El método inicia la búsqueda desde la derecha y devuelve el primer índice donde el número 7 ya no es menor que el siguiente valor.

Múltiples valores
Para buscar más de un valor, utilice una matriz con los valores especificados.

-Ejemplo 6
Encuentre los índices donde se deben insertar los valores 2, 4 y 6:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy ordenada
arr = np.array([1, 3, 5, 7])

# Encontrar los índices donde deberían insertarse los valores 2, 4 y 6 utilizando np.searchsorted()
x = np.searchsorted(arr, [2, 4, 6])

# Imprimir los índices encontrados
print(x)

----------------------------NumPy Sorting Arrays---------------------------------

Ordenar matrices
Ordenar significa poner elementos en una secuencia ordenada .

Secuencia ordenada es cualquier secuencia que tiene un orden correspondiente a elementos, como numérico o alfabético, ascendente o descendente.

El objeto NumPy ndarray tiene una función llamada sort()que ordenará una matriz específica.

-Ejemplo 1
Ordena la matriz:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy
arr = np.array([3, 2, 0, 1])

# Ordenar la matriz de forma ascendente utilizando np.sort()
sorted_arr = np.sort(arr)

# Imprimir la matriz ordenada
print(sorted_arr)

Nota: Este método devuelve una copia de la matriz, sin modificar la matriz original.

También puedes ordenar matrices de cadenas o cualquier otro tipo de datos:

-Ejemplo 2
Ordene la matriz alfabéticamente:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy de cadenas
arr = np.array(['banana', 'cherry', 'apple'])

# Ordenar la matriz de forma alfabética (lexicográfica) utilizando np.sort()
sorted_arr = np.sort(arr)

# Imprimir la matriz ordenada
print(sorted_arr)

-Ejemplo 3
Ordenar una matriz booleana:

# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy de booleanos
arr = np.array([True, False, True])

# Ordenar la matriz utilizando np.sort()
sorted_arr = np.sort(arr)

# Imprimir la matriz ordenada
print(sorted_arr)

Ordenar una matriz 2-D
Si utiliza el método sort() en una matriz 2-D, ambas matrices se ordenarán:

-Ejemplo 4
Ordenar una matriz 2-D:
# Importar la biblioteca NumPy con el alias 'np'
import numpy as np

# Crear una matriz NumPy bidimensional
arr = np.array([[3, 2, 4], [5, 0, 1]])

# Ordenar la matriz a lo largo del último eje (columnas) utilizando np.sort()
sorted_arr = np.sort(arr)

# Imprimir la matriz ordenada
print(sorted_arr)




















  





















  
