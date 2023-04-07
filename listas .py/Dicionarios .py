alumnos={
    "nombre": "Juan",
    "apellido": "Galarza",
    "direccion": "Av Loja",
    "cedula": "010676723",
    "correo":"juan Galarza@gmail.com"}
print (alumnos)
print(alumnos["cedula"])
print(alumnos["correo"])
alumnos["cedula"]="010674567"
alumnos["genero"]="Masculino"
print(alumnos)
#crear carreras del instituto
instituto={
    "carreras":["entrenamiento deportivo","big data","gestion patrimonio cultural","desarrollo de sofware","desarrolllo infantil integral"],
    "materias":["legislacion","aprendizaje de aquina","fundamentos","base de datos","base de datos no relacionables","estadistica"],
    "profesores":["lady","hector","germania","catherine","veronica","diana"],
    "notas":[10,7,8,9,7,6]
}
print(instituto["carreras"])
print(instituto["materias"])
print(instituto["notas"])
# forma tradicional
print(sum(instituto["notas"])/len(instituto["notas"]))
#forma manual
suma=0
for e in instituto["notas"]:
    suma +=float (e)
    print(suma/len(instituto["notas"]))
#imprimir con decimales
print (round(suma/len(instituto["notas"]),2))
#nota minima profesor y materia
nota_minima=min(instituto["notas"])
posicion=instituto["notas"].index(nota_minima)
print("la nota minima es:",nota_minima)
print("asignatura",instituto["materias"][posicion])
print("profesor",instituto["profesores"][posicion])

    
 
