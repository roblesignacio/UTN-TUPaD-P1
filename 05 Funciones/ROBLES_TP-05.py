# 1. Función que imprime "Hola Mundo!"
import math


def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que devuelve un saludo personalizado


def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que imprime información personal


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# 4. Funciones para calcular área y perímetro de un círculo


def calcular_area_circulo(radio):
    return math.pi * radio ** 2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función para convertir segundos a horas


def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar del número


def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función que realiza operaciones básicas


def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "División por cero")

# 8. Función para calcular IMC


def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

# 9. Función para convertir Celsius a Fahrenheit


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# 10. Función para calcular el promedio de tres números


def calcular_promedio(a, b, c):
    return (a + b + c) / 3
