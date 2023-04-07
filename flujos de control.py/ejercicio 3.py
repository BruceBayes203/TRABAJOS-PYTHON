# ejerccio 5
# mostrar los numeros de la renta
renta=float(input("elvalor de larenta"))
tax=0
if renta <10000:
    tax =5/100
elif renta>=10000 and renta <=20000:
    tax =10/100
elif renta >= 20000 and renta <=35000:
    tax = 15/100
elif renta >=35000 and renta<= 60000:
    tax=20/100
elif renta >60000:
    tax=30/100
else:
    print("la renta ingresada es incorrecta")
    total=renta*tax
    print("elvalor del impuesto a pagar es:",total)
    print ("la renta a recibir es:"/renta-tax)
    