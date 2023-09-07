import time
inicio = time.time()

a = input("Digite el numero menor del rango: ")
a = int(a)
b = input("Digite el numero mayor del rango: ")
b = int(b)

for i in range(a,b):
    conta = 0
    for n in range(1, i+1):
        residue = i%n
        if residue == 0:
            conta = conta + 1
              
    if conta == 2:
        print(f'{i} es un primo')
        
fin = time.time()
print("t = ", (fin - inicio)*1000)
