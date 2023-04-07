#la suma de los numeros
valor_1=int(input("valor1="))
valor_2=int(input("valor2="))
tablilla3=valor_1+valor_2
tablilla4=valor_1-valor_2
tablilla5=valor_1*valor_2
print("presione 1para sumar")
print("presione 2para restar")
print("presione 3 para multiplicar")
comando=input("digite opcion")
if comando==1:
    print("lasumaes:",tablilla3)
if comando==2:
    print("la resta es:",tablilla4)
if comando==3:
    print("la multiplicacion es:",tablilla5)
else:
    print("comando no encontrado")
