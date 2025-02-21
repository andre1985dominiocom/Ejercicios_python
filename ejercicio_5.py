#La distribuidora de motocicletas Rueda Floja ofrece una promoción que consiste en lo siguiente:
#las motos marca Honda tienen un descuento del 5%, las de marca Yamaha del 8% y las Suzuki el
#10%, las de otras marcas el 2%. Se requiere calcular el valor a pagar por una motocicleta.

#Imprimir título
print("Programa para calcular el descuento a pagar por una motocicleta: ")

#Solicitar los valores de las motocicletas y las marcas
Motorcycle_value = float(input("Ingrese el valor de la motocicleta: "))
Brand = input("ingrese la marca de la motocicleta (Honda, Yamaha, Suzuki, Otra): ")

#Utilizar condicionantes para determinar el descuento
if Brand == "Honda":
    Discount = 0.05
elif Brand == "Yamaha":
    Discount = 0.08
elif Brand == "Suzuki":
    Discount = 0.10
else: 
    Discount = 0.02

#Calcular el valor del descuento
Discount_value = Motorcycle_value * Discount

#Calcular el valor a pagar
Value_pay = Motorcycle_value - Discount_value

#Mostrar resultado
print(f"Valor del descuento: {Discount_value} ")
print(f"Valor a pagar: {Value_pay} ")
