a = input("Digite el numero menor del rango: ")
a = int(a)
b = input("Digite el numero mayor del rango: ")
b = int(b)

for i in range (a,b):
    residual = i%2
    if residual == 0:
        print (i, "par")
    else:
       print (str(i) + ' es impar')
        
