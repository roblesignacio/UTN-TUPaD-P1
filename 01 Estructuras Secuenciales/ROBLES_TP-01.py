def ejercicio_1():
    # 1) Imprimir "Hola Mundo!"
    print("Hola Mundo!")


def ejercicio_2():
    # 2) Pedir nombre y saludar
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}!")


def ejercicio_3():
    # 3) Pedir nombre, apellido, edad y lugar de residencia
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    lugar = input("Ingrese su lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")


def ejercicio_4():
    # 4) Calcular área y periímetro de un círculo
    import math
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"El área del círculo es {area:.2f}")
    print(f"El perímetro del círculo es {perimetro:.2f}")


def ejercicio_5():
    # 5) Convertir segundos en horas
    segundos = int(input("Ingrese una cantidad de segundos: "))
    horas = segundos / 3600
    print(f"Equivale a {horas:.2f} horas.")


def ejercicio_6():
    # 6) Tabla de multiplicar de un número
    numero = int(input("Ingrese un número: "))
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def ejercicio_7():
    # 7) Operaciones con dos números
    num1 = int(input("Ingrese el primer número (distinto de 0): "))
    num2 = int(input("Ingrese el segundo número (distinto de 0): "))
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2:.2f}")


def ejercicio_8():
    # 8) Cálculo del Índice de Masa Corporal (IMC)
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Su Índice de Masa Corporal (IMC) es {imc:.2f}")


def ejercicio_9():
    # 9) Conversión de grados Celsius a Fahrenheit
    temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    temp_fahrenheit = (9/5) * temp_celsius + 32
    print(f"La temperatura en Fahrenheit es {temp_fahrenheit:.2f}")


def ejercicio_10():
    # 10) Promedio de tres números
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    promedio = (n1 + n2 + n3) / 3
    print(f"El promedio de los tres números es {promedio:.2f}")


# Menú para seleccionar el ejercicio a ejecutar
if __name__ == "__main__":
    while True:
        print("\nSeleccione el ejercicio a ejecutar (1-10) o 0 para salir:")
        opcion = input("Ingrese un número: ")
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7()
        elif opcion == "8":
            ejercicio_8()
        elif opcion == "9":
            ejercicio_9()
        elif opcion == "10":
            ejercicio_10()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
