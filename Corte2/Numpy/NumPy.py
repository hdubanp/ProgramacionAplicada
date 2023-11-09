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

---------------------------3-------------------------------------------

