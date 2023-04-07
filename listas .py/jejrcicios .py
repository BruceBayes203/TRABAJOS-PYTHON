# crear una lista de ventas
listas=[10,30,40,50,60,70,80]
print("imprimir",[listas])
#remplazar el valor
listas[4]=100
print(listas)
#agregar valore s append
listas .append(120)
# agregar listas con bucle for
for e in  listas:
    print(e)
# ordenar las listas
listas.sort
print(listas)
#agregar comando len
print(len(listas))
# verificar si estan en el comando listas
print("imprimir",listas.count(120),"imprimir")
#ejejrcicicos 2
numeros=[]
for e in range(5):
    print("muestrame los numeros",(numeros))
#muetra los nombres de tus amigos
llaves=['Sandro', 'Sebastian', 'Ariel', 'Paul', 'Bruce', 'Jhonnathan']
print("imprimir el primer ",llaves[0])
#crear una lista con numeros pares
numeros1=[1,2,3,4,5,6,7,8,9,10]
for e in numeros1:
     if e %2 == 0:
         print("El numero es par: ",e)
# eliminar el ultimo elemento de la lista de amigos
llaves=['Sandro', 'Sebastian', 'Ariel', 'Paul', 'Bruce', 'Jhonnathan']
print("imprimir el ulimo",llaves[-1])
"# añade a un nuevo amigo"
llaves=['Sandro', 'Sebastian', 'Ariel', 'Paul', 'Bruce', 'Jhonnathan']
llaves.insert(2,"Carlos")
print(llaves)
#muestra el primer y el ultimo
numeros = [1,2,3,4,5,6,7,8,9,10]
print(F"El primer elemento de la lista es: {numeros[1]} \n\t y el ultimo elemento es: {numeros[-1]}")
#contar los valores de los nombres
llaves=['Sandro', 'Sebastian', 'Ariel', 'Paul', 'Bruce', 'Jhonnathan']
print("imprimir los numeros",len (llaves))
# relizar la suma de los numeros
numeros=[1,2,3,4,5,6,7,8,9,10]
suma = 0    
for e in numeros:
     suma = e + suma
     print(suma)
     

