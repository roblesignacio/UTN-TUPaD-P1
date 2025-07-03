# Actividad 1: Edad mayor de 18
def actividad_1():
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad")

# Actividad 2: Nota aprobada o desaprobada


def actividad_2():
    nota = float(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# Actividad 3: Solo números pares


def actividad_3():
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

# Actividad 4: Categoría según edad


def actividad_4():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# Actividad 5: Contraseña longitud correcta


def actividad_5():
    contrasena = input("Ingrese una contraseña: ")
    if 8 <= len(contrasena) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 6: Sesgo estadístico con lista aleatoria


def actividad_6():
    import random
    from statistics import mode, median, mean

    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

    if media > mediana > moda:
        print("Sesgo positivo o a la derecha")
    elif media < mediana < moda:
        print("Sesgo negativo o a la izquierda")
    elif media == mediana == moda:
        print("Sin sesgo")
    else:
        print("Distribución irregular")

# Actividad 7: Frase que termina con vocal


def actividad_7():
    frase = input("Ingrese una frase o palabra: ")
    if frase[-1].lower() in "aeiou":
        frase += "!"
    print(frase)

# Actividad 8: Transformar nombre según opción


def actividad_8():
    nombre = input("Ingrese su nombre: ")
    opcion = input(
        "Ingrese opción (1: mayúsculas, 2: minúsculas, 3: primera mayúscula): ")

    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción no válida")

# Actividad 9: Clasificar terremoto según magnitud


def actividad_9():
    mag = float(input("Ingrese la magnitud del terremoto: "))

    if mag < 3:
        print("Muy leve")
    elif mag < 4:
        print("Leve")
    elif mag < 5:
        print("Moderado")
    elif mag < 6:
        print("Fuerte")
    elif mag < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")

# Actividad 10: Estación según hemisferio, mes y día


def actividad_10():
    hemisferio = input("Ingrese hemisferio (N/S): ").upper()
    mes = int(input("Ingrese mes (1-12): "))
    dia = int(input("Ingrese día: "))

    dias_mes = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    fecha = dias_mes[mes-1] + dia

    if hemisferio == "N":
        if (fecha >= 355 or fecha <= 79):
            estacion = "Invierno"
        elif fecha <= 171:
            estacion = "Primavera"
        elif fecha <= 264:
            estacion = "Verano"
        else:
            estacion = "Otoño"
    elif hemisferio == "S":
        if (fecha >= 355 or fecha <= 79):
            estacion = "Verano"
        elif fecha <= 171:
            estacion = "Otoño"
        elif fecha <= 264:
            estacion = "Invierno"
        else:
            estacion = "Primavera"
    else:
        estacion = "Hemisferio inválido"

    print("Estación:", estacion)


if __name__ == "__main__":
    print("Selecciona la actividad que quieres ejecutar (1-10):")
    opcion = input()
    if opcion == "1":
        actividad_1()
    elif opcion == "2":
        actividad_2()
    elif opcion == "3":
        actividad_3()
    elif opcion == "4":
        actividad_4()
    elif opcion == "5":
        actividad_5()
    elif opcion == "6":
        actividad_6()
    elif opcion == "7":
        actividad_7()
    elif opcion == "8":
        actividad_8()
    elif opcion == "9":
        actividad_9()
    elif opcion == "10":
        actividad_10()
    else:
        print("Opción inválida")
"""
