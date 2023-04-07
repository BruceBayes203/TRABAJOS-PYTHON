calificacion=float(input("ingrese la calificacion:"))
print(calificacion)
if 0 <= calificacion <= 10:
 if calificacion>=0 and calificacion<4:
     print(f"Su nota de: {calificacion} \nTiene una equivalencia de Deficiente")
elif calificacion>=4 and calificacion<6.99:
     print(f"Su nota de: {calificacion} \nTiene una equivalencia de Regular")
elif calificacion>=6.99 and calificacion< 8:
     print(f"Su nota de: {calificacion} \nTiene una equivalencia de Bueno")
elif calificacion >=8 and calificacion<9:
     print(f"Su nota de: {calificacion} \nTiene una equivalencia de Muy Bueno")
elif calificacion >=9 and calificacion<9.5:
        print(f"Su nota de: {calificacion} \ntiene una equivalencia de  Muy bueno ")
        
else:
        calificacion >= 9.5
        print(f"Su nota de: {calificacion} \ntiene una equivalencia de Excelente ")





