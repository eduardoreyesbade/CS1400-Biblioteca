##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/19/2026)
# Tarea: Proyecto M07 - Dia de los Muertps
##########################

""" 
M7 Laboratorio presencial:
Elije una pareja para entrevistar.
La concatenación de cadenas para aprender a usar + y unir cadenas de texto.
Incluir espacios manualmente (" "), y combinar entrada del usuario con otros textos.
"""

# TODO Tarea 1: Escribe una linea de bienvenida a este programa 

print("Bienvenido al curso CS1400, clase 8")

# TODO Tarea 2: Solicitar datos del usuario. 
# Usar tres variables: nombre, apellido, y cancion.
# ## Entrevista algun companero(a) para averiguar su cancion preferida y su nombrecompleto.

nombre = input("Cual es tu primer nombre? ")
segundo_nombre = input("Cual es tu segundo nombre? (deja vacio si no tienes) ")
apellido = input("Cual es tu primer apellido? ")
segundo_apellido = input("Cual es tu segundo apellido? (deja vacio si no tienes) ")
cancion = input("Cual es tu cancion favorita? ")

# Una manera de validar entradas vacías
# Toma en cuenta que cambios podrias realizar si tienen un segundo nombre, y/o un segundo apellido.
# La meta es obtener su nombre completo.
if not nombre.strip():
    print("Por favor, escribe tu primer nombre.")
    exit()

if not apellido.strip():
    print("Por favor, escribe tu apellido.")
    exit()

if not cancion.strip():
    print("Por favor, escribe el nombre de una canción que te guste.")
    exit()

# Formatear entrada: capitalizar nombres
# Agregar nuevos variables si es necesario.
nombre = nombre.strip().capitalize()
segundo_nombre = segundo_nombre.strip().capitalize()
apellido = apellido.strip().capitalize()
segundo_apellido = segundo_apellido.strip().capitalize()
cancion = cancion.strip().title()

# TODO Tarea 3: Crear un variable llamado nombre_completo para juntar
#  (concatenar) todos los nombres ingresados, usando los espacios adecuado.

nombre_completo = nombre

if segundo_nombre != "":
        nombre_completo = nombre_completo + " " + segundo_nombre

apellido_completo = apellido

if segundo_apellido != "":
        apellido_completo = apellido_completo + " " + segundo_apellido


# TODO Tarea 4: Mostrar el resultado con alguna frase como por ejemplo, "Tu nombre completo es  ___ "

print("Tu nombre completo es " + nombre_completo  + apellido_completo + ".")


# TODO Tarea 5: Crear un ultimo variable, y agruegale más texto concatenado.
# Puede ser un saludo, o un piropo que incluya el variable para la cancion.
# Por ejemplo, "Hola ___, me encanta que tu cancion favorita sea ___! "

saludo = "Hola " + nombre + ", que gusto conocerte! " + "Me encanta que tu cancion favorita sea " + cancion + ". " + "Seguro que " + nombre_completo + " tiene muy buen gusto musical."

print(saludo)
# Imprimir a la terminal

