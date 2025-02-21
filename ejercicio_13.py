#Desarrollar un algoritmo con generalización de la secuencia:

#Imprimir título
print("Programa para seguir una secuencia: ")

#Utilizar funcióm
def Calculate(N):
    Sum = 0

    #Se define el rango de la formúla
    for n in range(N):
        Numerator = (2 * N + 1) ** 4 + 4
        Denominator = ((-1) ** N) * (Numerator / Denominator)
    print({Sum})

#Calcular la suma de los primeros 10 términos
N = 10
Result = Calculate(N)
print(f"La suma de los primero {N} términos es: {Result}")
