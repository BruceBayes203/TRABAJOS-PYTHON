#########1
a=set()
a.add(1)
a.add(3)
a.add(6)
a.add(5)
a.add(4)
print(a)
b=set()
b.add(3)
b.add(10)
b.add(5)
b.add(6)
b.add(4)
b.add(8)
print(b)
c=set()
c.add(3)
c.add(5)
c.add(9)
print(c)
#4##########eliminacion de elmentos
b.discard(8)
print(b)
# co`pia de un conjunto
d=a.copy()
print(d)
# limpiesa 
c.clear()
print(c)
# comprobacion
print(c.isdisjoint(a))
print(c.isdisjoint(b))
######2#######
e=set()
e.add(3)
e.add(4)
print(e.issubset(b))
# es contenendor de otro conjunto
print(b.issuperset(a))
print(e.issuperset(a))
# metodo union
f=c.union(b)
print('conjunto f:',f)
f=c.update(b)
print('conjunto f:',f)
a.update(b)
print('conjunto a',a)
# metodo diferente
print("conjunto a:",a)
print(a.difference(b))
a.difference_update(b)
print("conjunto a:",a)
#interseccion
c.intersection(d)
# intersection update para guardar todos los elemnentos
c.intersection_update(d)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# saber si son symetricos
print(c.symmetric_difference(d))