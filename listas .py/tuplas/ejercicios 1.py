#1 crear una tupla vacia
mi_tupla=()
#2 acceder el comando de una tupla
empty_tuple = ()
empty_tuple1 =  (19,20)
#3acceder al elemento de una tupla
tupla = ('a', 'b', 'd')
tupla[0]  
tupla[1] 
print(tupla)
print(tupla[0])
print(tupla[1])
#intentar agragar algo en las tuplas
"tupla[1]=20"
#4concatenar tuplas
test_tup1 = (3, 4)
test_tup2 = (5, 6)
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
res = ((test_tup1, ) + (test_tup2, ))
print("Tuples after Concatenating : " + str(res))
# obtener la longitud de una tupla
print(len(test_tup1))
len(tupla)
#convertir de tupla a lista
lista = ['rojo', 'azul', 'verde', 'amarillo']
tupla = tuple(lista)
print(tupla)
#convertir de lista a tupla
tupla = ('rojo', 'azul', 'verde', 'amarillo')
lista = list(tupla)
print(type(lista))
print(tupla[-1])
print(tupla[2])

