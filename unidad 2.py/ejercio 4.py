#suma de elementos
suma_de_notas = 10
notas=[10,9,7,6]
for nota in notas:
    suma_de_notas  += nota

print(suma_de_notas)
#####2########contar elementos de una lista
milistas=[1,2,3,4,5,6,7,8,9,10]
for i,v in enumerate(milistas):
    print(i,v)
#####3##########imprimir una lista de elemntos
losdicionarios={"amarillo":"yellow","azul":"blue","verde":"green"}
for c in losdicionarios:
    print("imprime la lista de:",c)
########4######contar caracteres de una cadena con bucle for
prefijos = "JKLMNOPQ"
sufijo = "ack"

for letra in prefijos:
    print (letra + sufijo)
#####5 imprimir elentos de una cadena
print("Comienzo")
for i in [0, 1, 2]:
    print("Hola ")
print()
print("Final")
# 6imprimir numeros naturales con for
for x in range(11):
    print(x)
#7imprimir los numeros enteros pares
for num in range(0,11,2):
    print("imprimir los numeros pares",num)
#8 imprimi la serie con numeros impares
for num in range(0,11,3):
    print("imprimir los numeros impares",num)

