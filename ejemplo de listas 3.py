lista1=[0,1,-1,0,5,-2,-6,8,10,9,-3,-5,-10,0]
ceros=[]
positivos=list()
negativos=list()

for e in  lista1:
  if e == 0:
    ceros.append(e)
  elif e >=1:
    positivos.append(e)
else:
     negativos.append(e)

print("imprimir lista que muestre ceros",ceros)
print("imprimir  lista que muestre positivos",positivos)
print ("imprimir  lista que muestre negativos",negativos)