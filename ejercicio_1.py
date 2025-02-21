#Un profesor diseña un cuestionario con n preguntas, estima que para calificar cada pregunta
#requiere m minutos. Si el cuestionario se aplica a x estudiantes, cuánto tiempo (horas y
#minutos) necesita para calificar todos los exámenes. Se debe validar que los datos ingresados
#deben ser positivos y si ingresa valores negativos debe mostrar un mensaje al usuario y
#culminar el algoritmo.

#Imprimir título

print("Programa para calcular el tiempo para calificar un examen ")

#Variables de entrada para desarollar el algoritmo

n = int(input("Ingresar el número de preguntas (n) : "))
m = int(input("Ingresar el número por preguntas en minutos (m) : "))
x = int(input("Ingresar el número de estudiantes (x) : "))

#Utilizar sentencias para validar que los valores sean positivos
if n < 0 or m < 0 or x < 0:
    print("Error: Todos los valores deben ser positivos: ")
else: 
    #Calcular el tiempo total en minutos
    times_minutes = n * m * x

    #Convertir el tiempo total a horas y minutos
    hours = times_minutes // 60
    minutes = times_minutes % 60

    #Mostrar resultados
    print(f"El tiempo total necesario es: en horas {hours} y minutos {minutes} ")
