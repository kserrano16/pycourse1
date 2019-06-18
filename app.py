import funciones
a = int(input("Que desea hacer? Para suma presione: 1, para resta presione: 2"))
b = int(input())
c = int(input())

if a == 1: 
    print(funciones.suma(b,c))
elif a == 2:
    print(funciones.resta(b,c))