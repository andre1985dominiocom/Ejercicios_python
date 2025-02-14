#En la universidad Buena Nota se requiere un algoritmo para calcular la nota definitiva y decidir
#si el estudiante aprueba o reprueba la asignatura. La nota final se obtiene a partir de dos notas
#parciales y un examen final, donde el primer parcial equivale al 30%, el segundo parcial al 30%
#y el examen final al 40%, y la nota mínima aprobatoria es 3.0. Si el promedio de los dos parciales
#es menor a 2.0, el estudiante no puede presentar examen final y pierde la materia por bajo
#promedio, en este caso la nota definitiva es el promedio de los parciales, si el promedio es igual
#o superior a 2.0 puede presentar el examen final. Si la nota del examen final es inferior a 2.0,
#se desconoce las notas parciales y la nota definitiva es la obtenida en el examen final. Si la nota
#es igual o superior a 2.0 se calcula la nota definitiva aplicando los porcentajes mencionados a
#los parciales y al final. Si la nota definitiva es igual o superior a 3.0 el estudiante aprueba la
#asignatura; si es inferior a 3.0 pierde la materia; sin embargo, puede habilitarla, siempre y
#cuando en el examen final obtenga nota mayor o igual a 2.0, en este caso la nota definitiva será
#la que obtenga en la habilitación.

#Variables

Parcial_1 = 0.30
Parcial_2 = 0.30
Parcial_3 = 0.40

Nota_def = float(input("Ingresar el valor de la nota : "))
print = ("Mostrar la nota definitiva : ")

if Nota_def > 3.0:
    print("Aprobado")

elif Nota_def < 2.0:
    print("No presenta examen")

prom_final = ((Parcial_1 + Parcial_2 + Parcial_3)/3) * 0.30 + 0.30 + 0.40

print("El promedio final es : " , {prom_final} )


