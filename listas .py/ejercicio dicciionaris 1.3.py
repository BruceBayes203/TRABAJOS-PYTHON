# ejercicios de python dicionarios
alumnado=[]
alumnado=dict
#Agregar elementos a un diccionario:
alumnos={
        "0106663792":"Juan Bravo",
        "1105050775":"Veronica Chimbo",
        "0107050270":"Antoni Mejia",
        "1501095408":"Pizango Jhordan",
        "0105410211":"Christian Preciado",
        "0106605017":"Astudullo Carlos",
        "0106767007":"Bruce Garate",
        "0105737365":"Stallin Barbecho",
        "0954337572":"Torres Eudyn",
        "0106637150":"Paredes Jennifer",
        "0150564078":"Danny Alex",
        "0106399041":"Jacqueline Tenesaca",
        "0150474021":"David Ñauta",
        "0107270282":"Edwin Arroyo",
        "0107416927":"Jose Muñoz",
        "0150578094":"Nayeli Gallegos"
}
alumnos["0107350788"]="Ariel Villa"
print(alumnos)
#Acceder a un valor en un diccionario:
print(alumnos("0954337572"))
#Verificar si una llave existe en un diccionario:
print( alumnos.get("0954337570","no se encuentra este elemento en la lista"))
#Eliminar un elemento de un diccionario:
alumnos.pop("0954337572")
print("alumnos")
print( alumnos.get("0954337572","no se encuentra este elemento en la lista"))
#Imprimir las llaves de un diccionario:
print(alumnos.keys())
#Imprimir los valores de un diccionario:
print(alumnos.values())
#Imprimir las llaves y valores de un diccionario:
for c,v in alumnos.items:
    print("imprimir valores de alumnos",c,v)
