# Actividad 1: Añadir frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actividad 2: Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Actividad 3: Lista de frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# Actividad 4: Agenda telefónica
agenda = {}
for _ in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero
consulta = input("¿De quién querés saber el número? ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no está en la agenda.")

# Actividad 5: Frase y análisis
frase = input("Ingresá una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Frecuencia de palabras:", conteo)

# Actividad 6: Notas de alumnos
alumnos = {}
for _ in range(3):
    nombre = input("Ingresá el nombre del alumno: ")
    notas = tuple(
        float(input(f"Ingresá nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

# Actividad 7: Sets de aprobados
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}
print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# Actividad 8: Stock de productos
stock = {"Arroz": 20, "Fideos": 30, "Harina": 10}
producto = input("Ingresá el nombre del producto: ")
if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(
        input("Producto nuevo. ¿Cuántas unidades querés agregar? "))
    stock[producto] = nuevo_stock
print("Stock actualizado:", stock)

# Actividad 9: Agenda de eventos
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '14:00'): 'Clase de inglés',
    ('Viernes', '16:00'): 'Gimnasio'
}
dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (formato HH:MM): ")
evento = agenda_eventos.get((dia, hora), "No hay actividad programada.")
print(f"Actividad para {dia} a las {hora}: {evento}")

# Actividad 10: Invertir diccionario país-capital
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Brasil': 'Brasilia',
    'Italia': 'Roma'
}
capitales_paises = {capital: pais for pais,
                    capital in paises_capitales.items()}
print("Diccionario invertido (capital: país):", capitales_paises)
