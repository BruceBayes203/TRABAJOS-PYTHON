# si un numero es negativo o positivo
numero = input("Escribe un número: ")
if numero == 0 and numero>0:
    print("Neutro")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")