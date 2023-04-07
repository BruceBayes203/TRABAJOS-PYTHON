numero=str(input("ingrese el numero:"))
if len(numero)!= 1:
    print("no se puede procesar el dato.debe ingresar solo numeros")
elif numero in "123456789":
    print("el numero ingresado se encuentra dentro de la cadena")
else:
    print("el numero ingresado no se encuentra en la cadena")