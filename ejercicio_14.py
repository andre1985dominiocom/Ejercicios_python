#Simula el funcionamiento de una máquina expendedora creando una operación que reciba
#dinero de monedas y un número que indique la selección del producto.
#▪ El programa retornará el nombre del producto y el dinero de vuelta (con el menor
#número de monedas).
#▪ Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un
#mensaje y retornar todas las monedas. Si no hay dinero de vuelta, se retornará cero.
#▪ Para que resulte más simple, trabajaremos en céntimos con monedas 5, 10, 50, 100 y
#200.
#▪ Se debe controlar que las monedas enviadas estén dentro de las soportadas.

#Imprimir título
print("Programa para calcular el cambio de una máquina expendedora: ")

#Denominación de las monedas
Coins = {5, 10, 50, 100, 200}
    
#Utilizar el bucle para determinar la devolución de las monedas
for Coins in Coins:
        if Coins not in Coins:
            print("Moneda no soportada:" , Coins)
            print("Monedas devueltas:" , Coins)
    
#Calcular el total de dinero que se inserta en la máquina
Money = sum(Coins)
    
