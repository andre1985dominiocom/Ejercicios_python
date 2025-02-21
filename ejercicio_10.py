#Dados dos números enteros, se requiere encontrar el máximo común divisor de los mismos. El
#máximo común divisor (MCD) entre dos números es el número más grande que los divide a
#ambos, incluso puede ser uno de ellos dado que todo número es divisor de sí mismo.

#Imprimir título
print("Programa para encontrar el máximo común divisor entre dos números: ")

#Definir funciones
def MCD(Num1 , Num2):
    
    #Utilizar bucles 
    while Num2 != 0:
        Rest = Num1 % Num2 
        Num1 = Num2
        Num2 = Rest
    return Num1

#Solicitar los dos números enteros
Num1 = int(input("Ingresar el primer número: "))
Num2 = int(input("Ingresar el segundo número: "))

#Calcular el MCD
Result = MCD(Num1 , Num2)

#Mostrar Resultados
print(f"El MCD de {Num1} y {Num2} es: {Result} ")
