#Un profesor diseña un cuestionario con n preguntas, estima que para calificar cada pregunta
#requiere m minutos. Si el cuestionario se aplica a x estudiantes, cuánto tiempo (horas y
#minutos) necesita para calificar todos los exámenes. Se debe validar que los datos a ingresados
#deben ser positivos y si ingresa valores negativos debe mostrar un mensaje al usuario y
#culminar el algoritmo.


#Variables
time = min
contador = 0

#Resolver el algoritmo 

n_question=int(input("Ingresar el número de preguntas a calificar: "))
x_student=int(input("Ingresar el estudiante a calificar: "))
print("Las horas que se necesitan son: ")
time=n_question*x_student
if x_student < 0:
    x_student = 0
    print("El número de estudiantes es : ")
elif n_question < 0:
    n_question = 0
    print("Sumar el número de preguntas : ")





