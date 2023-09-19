
def generar_tuplas_de_lista(lista):
    
    indice = 0
    
    while indice < len(lista)-1:
        print(lista[indice],lista[indice+1])
        indice = indice + 1
        
print(generar_tuplas_de_lista([64,68,97]))
