# 1) Factorial recursivo y mostrar del 1 al n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


limite = int(input(
    "Ingresá un número para calcular los factoriales desde 1 hasta ese número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

# 2) Fibonacci recursivo y mostrar serie hasta n


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


pos = int(input("Ingresá hasta qué posición mostrar la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print()

# 3) Potencia recursiva


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


b = int(input("Ingresá la base: "))
e = int(input("Ingresá el exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

# 4) Decimal a binario recursivo


def a_binario(n):
    if n == 0:
        return ""
    return a_binario(n // 2) + str(n % 2)


num_bin = int(input("Ingresá un número para convertir a binario: "))
bin_resultado = a_binario(num_bin)
print(f"El número {num_bin} en binario es: {bin_resultado or '0'}")

# 5) Palíndromo recursivo


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


texto = input("Ingresá una palabra para verificar si es palíndromo: ").lower()
print(f"¿'{texto}' es palíndromo? {es_palindromo(texto)}")

# 6) Suma de dígitos recursiva


def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


numero_suma = int(input("Ingresá un número para sumar sus dígitos: "))
print(
    f"La suma de los dígitos de {numero_suma} es {suma_digitos(numero_suma)}")

# 7) Contar bloques de pirámide recursivo


def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


niveles = int(input("Ingresá cuántos bloques hay en la base de la pirámide: "))
print(f"Se necesitan {contar_bloques(niveles)} bloques en total.")

# 8) Contar dígitos recursivo


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


numero_contar = int(input("Ingresá el número para buscar un dígito: "))
digito_buscar = int(input("¿Qué dígito querés contar?: "))
print(f"El dígito {digito_buscar} aparece {contar_digito(numero_contar, digito_buscar)} veces en {numero_contar}")
