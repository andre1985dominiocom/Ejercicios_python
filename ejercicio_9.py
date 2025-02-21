#Para implementar un reloj digital es necesario declarar tres variables, para controlar: horas,
#minutos y segundos. Cada una de estas variables controla un ciclo, así: los segundos se
#incrementan desde 0 a 59, los minutos también desde 0 a 59 y las horas desde 1 a 12 o de 1 a
#24. Este algoritmo está diseñado para terminar la ejecución al llegar a 12:59:59

#Imprimir título
print("Programa para implementar un reloj digital")

#Llamar a la función sleep
import time

#Iniciar las variables
Hours = 0
minutes = 0
Seconds = 0

#Utilizar bucles
while Hours <= 12:
    print (f"{Hours}:{minutes}:{Seconds} ")
    if Seconds == 60:
        Seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        Hours += 1
        Seconds += 1

#Incrementar los segundos

#Utilizar condicionante para verificar que los segundos lleguen a 60


#Esperar un segundo antes de continuar
#time.sleep(1)

#Mostrar resultados
print("El reloj ha terminaddo ")
