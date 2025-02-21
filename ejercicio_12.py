#Diseñar un algoritmo para validar una fecha en el formato dd/mm/aaaa. Se considera que una
#fecha es válida si está entre 01/01/1900 y 31/12/2100, el mes entre 1 y 12 y el día entre 1 y 31,
#teniendo en cuenta que algunos meses tienen 28 (o 29), 30 o 31 días. Si la fecha no es válida se
#muestra un mensaje de error y se vuelve a leer los datos. El algoritmo termina cuando la fecha
#ingresada es válida.

#Imprimir título
print("Programa para definir la fecha en el calendario: ")

#Utilizar función para año bisiesto
def Year_leap(Year):
    print (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0)

# Utilzar función para validar fecha
def Date(Day , Month , Year):

    #Utilizar sentencia para validar año
    if Year < 1900 or Year >2100:
        print("Año fuera de rango (1900-2100)")

    #Utilizar sentencia para validar mes
    if Month < 1 or Month > 12:
        print("Mes fuera de rango (1-12)")
    
    #Utilizar sentencia para validar día
    if Day < 1 or Day > 31:
        print("Mes fuera de rango (1-31)")
    
    #Utilizar sentencia para validar meses con 30 días
    if Month in [4 , 6 , 9 , 11] and Day > 30:
        print("Este mes solo tiene 30 días")
    
    #Utilizar sentencia para validar el mes de febrero
    if Month == 2:
        if Year_leap(Year):
            if Day > 29:
                print("Febrero solo tiene 29 días en años bisiestos")
            else:
                if Day > 28:
                    print("Febrero solo tiene 28 días")

    print("Fecha valida")

#Utilizar bucle para definir la fecha
while True:
    Date = input("Ingresar una fecha en formato dd/mm/aaaa: ")
    try:
        Day , Month , Year = map(int, Date.split)
        Result = Date(Day , Month , Year)
        print(Result)
        if Result == "Fecha valida":
            break
    except ValueError:
        print("Formato de fecha incorrecto. Usa dd/mm/aaaa: ")
