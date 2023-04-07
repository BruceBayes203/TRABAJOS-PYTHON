# ejercico de letras
letra=str(input("ingrese la letra:"))
if len (letra)!=1:
    print("no se puede procesar el dato.debeingresar solo una letra")
elif letra in"aeiuou":
    print("es vocal")
else:
    print("no es vocal")