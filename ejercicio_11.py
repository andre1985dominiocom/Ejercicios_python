#Convertir un número decimal a binario.

#Imprimir título
print("Programa para pasar números décimales a binarios: ")

#Utilizar función
def Decimal_binary(Decimal):

    #Utilzar sentencia
    if Decimal == 0:
     print("0")
    Binary =""

#Utilzar bucles
    while Decimal > 0:
       Residue = Decimal % 2
       Binary = str(Residue) + Binary

       Decimal = Decimal // 2 
    return Binary

#Solicitar imgresar número
Num_decimal = int(input("Ingresar un número decimal: "))
Result = Decimal_binary(Num_decimal)
print(f"El número binario es: {Result}")
