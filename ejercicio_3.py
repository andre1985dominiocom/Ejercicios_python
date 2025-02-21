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

#Imprimir título
print("Programa para calcular la nota definitiva de los estudiantes")

#Solicitar las notas de los dos parciales y el examen final
Exam_1 = float(input("Ingrese la nota del primer parcial (0.0 - 5.0): "))
Exam_2 = float(input("Ingrese la nota del segundo parcial (0.0 - 5.0): "))
Final_exam = float(input("Ingrese la nota del examen final (0.0 - 5.0): "))

#Calacular el promedio de los dos parciales
Average = (Exam_1 + Exam_2) / 2

#Utilizar sentencias para verificar si el estudiante puede presentar el examen final
if Average < 2.0:
    Final_note = Average
    print(f"El estudiante no puede presentar el examen final {Final_note} ")
else: 
    if Final_exam > 2.0:
        Final_note = Final_exam
        print(f"Nota definitva: {Final_note}")
    else:
        Final_note = (Exam_1 * 0.3) + (Exam_2 * 0.3) + (Final_exam * 0.4)
        print(f"Nota definitiva: {Final_note} ")

if Final_note >= 3.0:
    print("El estudiante aprueba la asignatura ")
else:
    if Final_exam >= 2.0:
        print("El estudiante puede habilitar la asignatura ")
    else:
        print("El estudiante reprueba la asigntura ")
