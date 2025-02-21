#Una compañía de seguros abrió una nueva agencia y estableció un programa para captar
#clientes, que consiste en lo siguiente: si el monto por el que se contrata el seguro es menor que
#$5.000.000 pagará el 3%, si el monto es mayor o igual a $5.000.000 y menor de 20.000.000
#pagará el 2% y si el monto es mayor o igual a 20.000.000 el valor a pagar será el 1.5 % ¿Cuál
#será el valor de la póliza?

#Imprimir título
print("Prograna para calcular el monto del descuento por adquirir un seguro")

#Solcitar el monto del seguro
Safe = int(input("Ingrese el monto del seguro: "))

#Utilizar sentencias para calcular el porcentaje a pagar
if Safe < 5000000:
    Percentage_pay = 0.03
elif Safe < 20000000:
    Percentage_pay = 0.02
else:
    Percentage_pay = 0.015

#Calcular el valor de la poliza
Policy_value = Safe * Percentage_pay

#Mostrar resultados
print(f"El valor de la poliza es: {Policy_value} ")
