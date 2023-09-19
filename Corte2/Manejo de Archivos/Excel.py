#Escribir
"""f= open("fileejemplos.txt","a")
f.write('\n'+" añadir nuevo texto")
f.close()"""

#lectura
"""f= open("fileejemplos.txt","r")
print(f.read())

#lectura por linea
print(f.readline(25))

#Crear nuevo Archivo
f=open("Nuevoarchivo.txt", "x")"""

#Borrar archivo
os.remove("Nuevoarchivo.txt")
