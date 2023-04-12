from ejemplo1 import*
opcion=0
while opcion>=0 and opcion<=10:
    print("0.salir del bucle")
    print("1.realizar la suma")
    print("2.ingrese la resta")
    print("3.ingrese la multiplicacion")
    print("4.ingrese la division")
    opcion=int(input("ingrese una opcion"))
    if opcion==0:
        print("salir del bucle")
        break
    elif opcion >=1:
        a=int(input("ingrese el primer numero"))
        b=int(input("ingrese el segundo numero"))
        print("realizar la suma: ",suma)
    elif opcion==2:
        a=int(input("ingrese el primer numero"))
        b=int(input("ingrese el segundo numero"))
        print("realizar la resta:",resta)
    elif opcion ==3:
        print("ingrese la multiplicacion")
    elif opcion==4:
        a=int(input("ingrese el primer numero"))
        b=int(input("ingrese el segundo numero"))
        print("ingrese la division:",division)
else:
    print("el comando ingresaso no ha sido el correcto")