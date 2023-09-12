#se crean dos diccionarios y se imprimen (palabra clave antes del dos puntos) lo otro es el valor asignado a la plabra clave

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)
-----------------------------------------------------------------------------------------------------
#aqui nos damos cuenta de que el valor asigando a la palabra clave puede ser una palabra
translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)
------------------------------------------------------------------------------------------------------
#esto es una lista en donde a la palabra clave se le puede asiganr varios valores y tambien a la palabra clave "25" tiene otro numero como valor
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"],"25":10000} 
print(children)

--------------------------------------------------------------------------------------------------------

#Creamos el diccionario y lo imprimimos como no tiene nada lo imprime como conjunto vacio
my_empty_dictionary ={}
print(my_empty_dictionary)

#las llaves cuadradas sirven para agregar un elemento al diccionario
my_empty_dictionary["Dinosaurios"] = 0
print(my_empty_dictionary)


---------------------------------------------------------------------------------------------------------------

#en la linea 1 cramos y asignamos valores al diccionario
animals_in_zoo = {"zebras": 8, "monkeys": 12}
#aqui agregamos un elemento y le asignamos un valor
animals_in_zoo["dinosaurs"] =  0
#imprimimos
print(animals_in_zoo)

#creamos otro diccionario
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#imprimimos
print(menu)
#aqui agregamos un elemento y le asignamos un valor
menu["cheesecake"] = 8
print(menu)

#reasignamos el valor en el diccionario
animals_in_zoo = {"dinosaurs": 0}
#hace lo mismo que el anterior 
animals_in_zoo = {"dinosaurs": 0}
print(animals_in_zoo)

----------------------------------------------------------------------------------------------------------
#creamos un diccionario y update sirve para agragar varios elementos al diccionario
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

---------------------------------------------------------------------------------------------------------
#creamos un diccionario y con update agregamos mas elementos
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})

#aqui reasignamos la referencia
oscar_winners["Best Picture"] = "pocoyo tactico"

print(oscar_winners)

--------------------------------------------------------------------------------------------------------------

#creamos una lista 
drinks = ["espresso", "chai", "decaf", "drip"]
#le asignamos valores
caffeine =[64, 40, 0, 120]

zipped_drinks =zip(drinks , caffeine)
drinks_to_cafeeine ={ key: value for key, value in zipped_drinks}

#imprimimos
print(drinks_to_cafeeine)
------------------------------------------------------------------------------------------
#creamos una lista 
drinks = ["20", "54", "48", "92"]
#creamos otra lista 
caffeine =["espresso", "chai", "decaf", "drip"]
#agrupamos
zipped_drinks =zip(drinks , caffeine)
#creamos un diccionario en donde "drinks" se vuelve los elementos y "caffeine" los valores de estos elementos 
drinks_to_cafeeine ={ key: value for key, value in zipped_drinks}

#imprimimos
print(drinks_to_cafeeine)























