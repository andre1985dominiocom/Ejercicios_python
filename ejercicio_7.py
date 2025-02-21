#Una joyería establece el valor de sus productos según el peso y el material. Se requiere un
#algoritmo que lea un valor de referencia x y a partir de éste calcule el valor del gramo de
#material utilizado y el valor del producto. El gramo de plata procesado tiene un costo de 3x, el
#platino 5x y el oro 8x.

#Imprimir título
print("Programa para calcular el precio de los productos en una joyería")

#Solicitar el valor de referencia x, el peso y el material
X = int(input("Ingresar el valor de referencia x: "))
Weight = float(input("Ingresar el peso del producto en gramos: "))
Product = input("Ingresar el producto (plata, platino y oro): ")

#Utilizar sentencias para calcular el costo por gramo de los productos
if Product == "plata":
    Cost_gram = 3 * X
elif Product == "platino":
    Cost_gram = 5 * X
elif Product == "oro":
    Cost_gram = 8 * X
else:
    print("Producto no válido")
    exit()

#Calcular el valor del producto
Producto_value = Weight * Cost_gram

#Mostrar resultados
print(f"Costo por gramo: {Cost_gram} ")
print(f"Valor del producto: {Producto_value} ")
