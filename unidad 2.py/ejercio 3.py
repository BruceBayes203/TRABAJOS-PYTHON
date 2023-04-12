# escribir con contadores el numero ascendente
def contadorascendente(num):
    cadena=""
    contador=0
    while contador <=num:
        cadena+=cadena+str(contador)+"\n"
        contador+=1
    return cadena
num=int(input("ingrese un numero"))
print(contadorascendente(num))
# numero descendente
def contadordescendente(num):
    cont=num
    while cont>=0:
        print(num)
        num-=1
num=int(input("ingrese un numero"))
contadorascendente(num)
#suma de numeros
def sumanumeros(num):
    cont=0
    suma=0
    while cont <=num:
        cont+=1
        suma+=cont
    return suma-(num+1)
num=int(input("ingrese un numero"))
print(sumanumeros(num))
# factorial multiplicacion
def factorial(num):
    cont=0
    mul=0
    while cont<=num:
        cont+=1
        mul=cont*mul
    return mul
num=int(input("ingrese un numero"))
print(factorial(num))
# 5 adivinar un numero
import random
def adivina(num_generado):
    adivina=0
    while adivina!=num_generado:
        adivina=int(input("advina entre 1 al 10"))
        if adivina<num_generado:
            print("el numero que busco es menor")
        elif adivina<num_generado:
            print("el numero que busco es mayor")
        else:
            print("print felicitaciones busco el numero",adivina)
num_generado=random.randint(1,10)
print("adivina el numero es:",str(num_generado))
adivina(num_generado)

# 6 vocales
def contador_vocales(texto):
    vocales="a,e,i,o,u"
    while vocales==texto:
        vocales=int(input("ingrese las vocales de la cadena"))
    return vocales
print("muestrame las voceles:",str(contador_vocales))
##7#####

###8#####calculo de potencia
def potencia(numero,exponente):
    resultado=1
    contador=1
    while contador <=exponente:
     resultado=resultado*numero
###9### promedio
def promedio(lista):
    suma=0
    cont=0
    while cont<len(lista):
     suma=suma+lista[ cont]
    cont +=1
    return suma/len(lista)
promedio= sum
len()
#10 contador de palabras
def contador_palabras(cadena):
    contador=0
    indice=0
    while indice<len(cadena):
        if cadena[indice]=="":
            contador+=1
            indice+=1
    print("la cadena de texto tiene",contador,"palabras.")
    if len(cadena)==0:
        contador=0
    else:
        contador=1
#menu de opciones
opcion=1
while opcion>=0 and opcion <=0:
    print("##########opciones···#########")
    print("1.caluclo ascendente")
    print("2.calulo desc")
    print("3.suma de valores")
    print("4.factorizacion de numero")
    print("5.adivinar el numero")
    print("6.contador de vocales")
    print("7.suma de numeros pares")
    print("8.calculo de potencia")
    print("9.calulo de promedio")
    print("10.contador de palabras")
    print("0.salir del bucles")
opcion=int(input("ingrese una opcion"))
if opcion==0:
    print('ha seleccionado salir') 
elif opcion==1:
    num=int(input("ingrese un numero entero positivo"))
    contadorascendente(num)
elif opcion==2:
    num=int(input("ingrese un numero entero positivo"))
    contadorascendente(num)
elif opcion==3:
    num=int(input("ingrese un numero entero positivo"))
    sumanumeros(num)
elif opcion==4:
    num=int(input("ingrese un numero entero positivo"))
    factorial(num)
elif opcion==5:
    num=int(input("ingrese un numero entero positivo"))
    adivina(num)
elif opcion==6:
    num=int(input("ingrese un numero entero positivo"))
    contador_vocales(num)



    