#1. Crear un menu iterativo con las siguientes opciones 
#2. opcion 1 'Saludar' , pedir datos personales
#3. opcion 2 Realizar una operacion matematica pedir 2 numeros 
#4. opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
#5. opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
#6. opcion 5 mostrar listado de alumnos aprobados 
#7. opcion 6 mostrar listado de alumnos desaprobados
#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#10. opcion 9 Salir. 

""" nombre=input("ingrese su nombre: ")
print("Buenos dias "+ nombre)

ep=float(input("ingrese nota de examen parcial: "))
ef=float(input("ingrese nota de examen final: "))
promedio=(ep+ef)*2**-1
print(promedio) """

""" alumnos=[
        {"nombre":"luis","edad":16,"correo":"luis23@gmail.com","cursos":{"algebra":12,"fisica":13,"lenguaje":17}},
        {"nombre":"genaro","edad":15,"correo":"gen63@gmail.com","cursos":{"algebra":18,"fisica":20,"lenguaje":17}},
        {"nombre":"lucia","edad":17,"correo":"lu005@gmail.com","cursos":{"algebra":16,"fisica":20,"lenguaje":17}},
        {"nombre":"alberto","edad":16,"correo":"beto9723@gmail.com","cursos":{"algebra":7,"fisica":10,"lenguaje":11}},
        {"nombre":"manuel","edad":16,"correo":"manuel661@gmail.com","cursos":{"algebra":19,"fisica":15,"lenguaje":14}},
        {"nombre":"marco","edad":15,"correo":"marco008@gmail.com","cursos":{"algebra":11,"fisica":10,"lenguaje":15}},
        {"nombre":"daniel","edad":15,"correo":"dani079@gmail.com","cursos":{"algebra":9,"fisica":8,"lenguaje":11}},
        {"nombre":"aaron","edad":18,"correo":"aaronp342@gmail.com","cursos":{"algebra":13,"fisica":13,"lenguaje":16}},
        {"nombre":"rosa","edad":17,"correo":"rosa885@gmail.com","cursos":{"algebra":12,"fisica":11,"lenguaje":15}},
        {"nombre":"malyn","edad":15,"correo":"malyn3@gmail.com","cursos":{"algebra":20,"fisica":19,"lenguaje":17}},
        {"nombre":"jacky","edad":16,"correo":"jacky332223@gmail.com","cursos":{"algebra":14,"fisica":13,"lenguaje":16}},
        ]
 """

# 9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado
""" print("ingrese dos numeros")
x=int(input("ingrese el primer numero: "))
y=int(input("ingrese el segundo numero: "))

if x>y:
    print(x)
else:
    print(y) """


#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
for i in range(0,10000000000,1000000):
    print(i)
