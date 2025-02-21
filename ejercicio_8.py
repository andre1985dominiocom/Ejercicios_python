#Un estudiante de ingeniería necesita tres libros: Cálculo, Física y Programación, cuyos precios
#son: v1, v2, v3 respectivamente. El estudiante cuenta con una cantidad x de dinero que ha
#recibido como apoyo económico para este fin. Se requiere un algoritmo que le ayude a decidir
#si puede comprar los tres, dos o un libros. El estudiante desea dar prioridad a los libros de mayor
#valor, ya que el dinero sobrante deberá devolverlo y los libros de menor valor serán más fácil
#de adquirir con recursos propios.

#Imprimir título
print("Programa para calcular la compra de libros de ingenieria")

#Solicitar los precios de los libros y el dinero disponible
V1 = float(input("Ingresar el precio del libro de cálculo: "))
V2 = float(input("Ingresar el precio del libro de Física: "))
V3 = float(input("Ingresar el precio del libro de Programación: "))
X = float(input("Ingresar la cantidad de dinero disponible: "))

Price = [V1 , V2 , V3]

#Iniciar varaiables en cero
Books = 0
Money = X

#Calcular la compra de libros 
for Price in Price:
    if Money >= Price:
        Money -= Price
        Books += 1
        
#Mostrar resultados
print(f"El estudiante puede comprar {Books} ")
print(f"Dinero restante: {Money} ")
