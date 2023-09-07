a = input("digite el primer numero entero: ")
a = int(a)
b = input("digite el segundo numero flotante: ")
b = float(b)
c = a + b

if a == b:
    print("igual")
else:
    print("Diferente")

print("A es del tipo: ", type(a))
print("B es del tipo: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b son de diferente tipo")
