#1 la suma de elementos de una tupla
def sumar(tupla):

    suma = 0

    for i in tupla:

        suma += i

    return suma

numeros = (1,2,3,4,5,6,7,8,9,10)

print("la suma de sus elementos es:",sumar(numeros))
#2crear unas tuplas y realizar la suma
a = 0
xd1 = (0,1)
xd2 = (9,8,7,6)
for i in range(len(xd1)):
        a += (xd1[i]+xd2[i])

print("El resultado de la suma es: ",a)
#crear una lista de nombres

mijines = ("Stalin","Sandro","Sebastian","ana","riven","sett","yasho")
print(sorted(mijines))
#buscar el minimo y el maximo

print("El valor minimo de la tupla es: ", min(numeros))
print("El valor maximo de la tupla es: ", max(numeros))
#convertir tupla atipo lista
tupla = (1,2,4,5,67,8,9,10,27)
lista = list(tupla)
print(type(lista))
print(tupla[-1])
print(tupla[2])

dias_delasemana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(dias_delasemana[3])
print(dias_delasemana[-2])


las_tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
pares = 0 

for i in las_tupla:
    if i % 2 == 0:
          print("Los numeros pares son:",i)


bacanos_meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
for mes in bacanos_meses:
      if len(mes) > 5:
            print(mes)



lasedades = (12, 25, 32, 16, 20, 18, 19, 22, 15, 30)
contador = 0
for edad in lasedades:
    if edad > 18:
        contador += 1

print("mayores de 18:", contador)

