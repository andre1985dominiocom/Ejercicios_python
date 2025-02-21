#El banco Buena Paga ofrece diferentes tasas de interés anual para depósitos a término
#dependiendo del tiempo por el que se hagan. Si el depósito es por un periodo menor o igual a
#seis meses la tasa es del 8% anual; entre siete y 12 meses, 10%; entre 13 y 18, 12%; entre 19 y
#24, 15%; y para periodos superiores a 24 meses el 18%. Se requiere un algoritmo para
#determinar cuánto recibirá un cliente por un depósito, tanto por concepto de interés como en
#total.

#Imprimir título
print("Programa para calcular los intereses pagados a los clientes")

#Solicitar el monto del depósito y el tiempo en meses
Deposit = int(input("Ingrese el monto del depósito: "))
Month_time = int(input("Ingrese el tiempo del depósito en meses: "))

#Utilizar condicionantes para calcular la tasa de interés
if Month_time <= 6:
    interest_rate = 0.08
elif Month_time <= 12:
    interest_rate = 0.10
elif Month_time <= 18:
    interest_rate = 0.12
elif Month_time <= 24:
    interest_rate = 0.15
else:
    interest_rate = 0.18

#Calcular el interés generado
General_interest = Deposit * interest_rate * (Month_time / 12)

#Calcular el total a recibido
Total_received = Deposit + interest_rate

#Mostrar resultados
print(f"Interés generado: {interest_rate} ")


print(f"Total recibido: {Total_received} ")
