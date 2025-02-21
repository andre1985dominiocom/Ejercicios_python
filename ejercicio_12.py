#Diseñar un algoritmo para validar una fecha en el formato dd/mm/aaaa. Se considera que una
#fecha es válida si está entre 01/01/1900 y 31/12/2100, el mes entre 1 y 12 y el día entre 1 y 31,
#teniendo en cuenta que algunos meses tienen 28 (o 29), 30 o 31 días. Si la fecha no es válida se
#muestra un mensaje de error y se vuelve a leer los datos. El algoritmo termina cuando la fecha
#ingresada es válida.

#Imprimir título
print("Programa para definir la fecha en el calendario: ")

#Validar formato año
list[1 , 12]
list[1 , 31]

#Declarar variables
Day = 1
Month = 1
Year = 1900

#Solicitar el ingreso de la fecha
Calendary = int(input("Ingresar la fecha en el calendario: "))

#Utilizar sentencias
if Day < 1:
    Day == 31
elif Month < 1:
    Month == 12
elif Year < 1900:
    Year == 2100

else:
    print("Formato de fecha incorrecto: ")
    exit()

#Utilzar bucles
for Day in range (1 , 31):
    for Month in range(1 , 12):
        if Day % Month == 0:
            print(f"{Day} {Month} * {Day // Month}")








