# Actividad 1
for i in range(101):
    print(i)

# Actividad 2
numero = input("Ingrese un número entero: ")
print(f"Cantidad de dígitos: {len(numero)}")

# Actividad 3
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = sum(range(inicio + 1, fin))
print(f"Suma de números entre {inicio} y {fin} (excluyendo): {suma}")

# Actividad 4
total = 0
while True:
    n = int(input("Ingrese un número entero (0 para salir): "))
    if n == 0:
        break
    total += n
print(f"Suma total: {total}")

# Actividad 5
import random
objetivo = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == objetivo:
        break
print(f"¡Correcto! Lo lograste en {intentos} intento(s)")

# Actividad 6
for i in range(100, -1, -2):
    print(i)

# Actividad 7
limite = int(input("Ingrese un número entero positivo: "))
suma = sum(range(limite + 1))
print(f"La suma de los números entre 0 y {limite} es: {suma}")

# Actividad 8
cantidad = 100  # Cambiar este valor para probar con menos
pares = impares = positivos = negativos = 0
for _ in range(cantidad):
    n = int(input("Ingrese un número entero: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# Actividad 9
cantidad = 100  # Cambiar este valor para probar con menos
suma = 0
for _ in range(cantidad):
    n = int(input("Ingrese un número entero: "))
    suma += n
media = suma / cantidad
print(f"La media de los {cantidad} números es: {media}")

# Actividad 10
numero = input("Ingrese un número entero: ")
invertido = numero[::-1]
print(f"Número invertido: {invertido}")