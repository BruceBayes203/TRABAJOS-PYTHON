### CURSO DE FUNDAMENTOS DE PYTHON
#1. Crear una lista de numeros del 1 al 5

mi_lista = [1,2,3,4,5]
print("imprime mi lista de numeros",mi_lista)

#2. Accede al elemento 3 de la lista:

print("imprime El elemento 2 es", mi_lista[1])

#3. Modifica un elemento de la lista:

mi_lista[4]=11 
print("Se modifico el elemento 4: ", mi_lista)

#4. Agrega el elemento 9 al final de la lista

mi_lista.append(9)
print("Se agrega el elemento 9", mi_lista)

#5. Eliminar el elemento 2 de la lista:

print("Se elimina el elemento 2: ", mi_lista.pop(1))

#6. Recorrer una lista con un bucle for:

for e in mi_lista:
    print(e)

#7. Ordenar una lista:

mi_lista.sort(reverse= False)
print("la lista ordenada", mi_lista)

#8. Obtener la longitud de una lista:

print("El numero de elementos es: ",len(mi_lista))

#9. Comprobar si un elemento está en la lista:

print("este elemento si esta y se repite: ",mi_lista.count(10), "numero de veces" )  