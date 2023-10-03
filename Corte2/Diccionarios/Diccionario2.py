#Esquema General de diccionarios, en los tres diccionarios las palabras clave son string 
#pero los elementos solo en los dos primeros son Int en el tercero es tambien string  
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
print(sensors)
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
print(num_cameras)
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
print(translations)

-----------------------------------------------------------
#La palabra clave no puede ser una lista
#Verificando errores
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
print(powers)
------------------------------------------------------------------
#Un diccionario donde las listas son elementos pero las palabras claves no lo son
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

---------------------------------------------------------------------
#Es posible crear un diccionario vacio
my_empty_dictionary = {}
print(my_empty_dictionary)
-----------------------------------------------------------------------
#Se crea un diccionario llamado menu y se imprime
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
#Se agrega un elemento que no existe y se imprime la actualizacion
menu["cheesecake"] = 8
print("After", menu)
#se crea y se imprime el diccionario Animales de Zoologico
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}
#por mas que se esta realizando el diccionario Animales de Zoologico 2 veces no 
#se imprime dos veces
#agragamos un elemento diferente 
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)
-----------------------------------------------------------------------
#Agregamos varias palabras claves
##Add multiple keys
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

#Si queremos agragar 3 nuevas salas usamos la siguiente sintasis
# #If we wanted to add 3 new rooms, we could use:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)
-----------------------------------------------------------------------
#Otro ejemplo usando la sentencia Update para agregar mas palabras claves 
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
-----------------------------------------------------------------------
#sabemos que podemos sobreescribir un elemento y que si lo 
#sobre escribimos el elemento actual va a remplazar el valor anterior 
## Overwrite Values ##
#We know that we can add a key by using the following syntax:
menu["banana"] = 3

#Declaramos el dicionario menu y hacemos una actualizacion de un elemento (lo sobreescribimos)
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5
print("After", menu)
-------------------------------------------------------------------------------
## Notice the value of "oatmeal" has now changed to 5.
#creamos diccionario
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
#usando la sentencia update agregamos otro elemento que no estaba en el diccionario original
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()
#sobre escribimos que la mejor imagen en peliculas sea Moonlinght
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)
---------------------------------------------------------------------------
#Aqui se muestra como podemos tener dos listas y estas se pueden convinar para
#crear un diccionario, una lista va a contener nombre de los estudiantes y la sigueinte
#su estatura en pulgadas
###Dict Comprehensions
#Let’s say we have two lists that we want to combine into a 
#dictionary, like a list of students and a list of their heights, 
#in inches:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#creamos un paquete y le hacemos un for que nos permite convinar las dos listas
#es un objeto que esta en una dirrecion de memoria de la computadora
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)

#pytho puede crearun diccionario usando comprehension usando la siguiente sintasis
students = {key:value for key, value in zip(names, heights)}
#acri se va a crear un nuevo diccionario y se va a imprimir
students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print(students)

# #zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:
----------------------------------------------------------------
#Aqui otro ejemplo donde combinamos los tipos de cafe con su diferentes tipos de bebidas
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

-----------------------------------------------------------------------------------
#Aqui seguimos haciendo ejemplos con la combinaciond de listas
#creamos una lista de canciones y de numero de veces que se escucho
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
#aqui la combinamos para un diccionario y lo imprimimos
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
#agregamos "Purple Haze" con update 
plays.update({"Purple Haze": 1})
#sobreescribimos "Respect" y lo imprimos
plays.update({"Respect": 94})
print("After: ", plays)
#sobre escribimos y imprimimos
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)




