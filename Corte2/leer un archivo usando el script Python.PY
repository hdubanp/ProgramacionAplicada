#abre el archivo.txt en modo lectura. provoca un error si no existe dicho archivo.     
fileptr = open("file2.txt","r")  
#almacena todos los datos del archivo en el contenido variable     
content = fileptr.read(10)   
# imprime el tipo de datos almacenados en el archivo   
print(type(content))      
#imprime el contenido del archivo      
print(content)       
#cierra el archivo abierto       
fileptr.close()    
