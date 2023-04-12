# mostrar por pantalla
def suma(num1,num2):
    return num1+num2
def resta(num1 ,num2):
    return num1-num2
def saludo():
    print("hola bruce")
def formateo(nombre, apellido):
    print(nombre,apellido)
bandera=True
while bandera:
    print("Menu de opciones")
    print("1.ingrese la suma")
    print("2.ingrese la resta")
    print (" 3.ingrese la division")
    print("4.ingrese la multiplicacion")
    print("5.ingrese saludo")
    print("6.ingrese formateo")
    print("7. ingrese salida")
opciones=int(input("ingrese la opcion"))
if opciones==1:
    num1=int(input("ingrese uno"))
    num2=int(input("ingrese dos"))
    if opciones!=5:
        print("la suma es:",num1+num2)
    elif opciones ==1:
        print("la resta es",num2-num1) 
        
    elif opciones==3:
        print("la multiplicaciones",num1*num2)
    else:
        print("la division es :",num1/num2)
else:
    print("la salida es:")
# 6. saludo
# 7. formateo
