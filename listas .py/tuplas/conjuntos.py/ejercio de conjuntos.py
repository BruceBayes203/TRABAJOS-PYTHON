#imprimir el 1 al 10 y mostralo por pantalla
x = 1

while x<=10:

    print(x)

    x = x + 1
#2 crear los conjuntos pares e impares del 1 al 10
num=[1,10]
for num in range(1,11):
    print("imprimir los numeros",num)
num=[1,100]
for num in range(0,11,2):
    print("imprimir los numeros pares",num)
num=[1,100]
for num in range(0,11,3):
    print("imprimir los numeros imperes",num)
# crear elemntos
a = ["Manzana", "Pera", "Banana", "Naranja"]  
del a[1]
a
del a[2]
a
print("pedirle ausuario que ingrese los conjuntos de la cadena",a)
#elemntos del 1 al 5 y del 4 al 8
elemntos=[1,2,3,4,5]
elemntos=[4,5,6,7,8]
unique_elemtos = []
for elementos in elemntos:
  if elementos not in unique_elemtos:
    unique_elemtos.append(elemntos)

print(unique_elemtos)
#ingredientes
ingredientes=0
ingredientes=["leche", "pan", "huevos" ,"azúcar"]
ingredientes.remove(4)
ingredientes
ingredientes["harina"]
print(ingredientes)