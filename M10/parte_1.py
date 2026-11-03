# Para almacenar la lista
roster = []

# Cargar la lista desde el archivo
try:
    archivoRoster = open('roster.txt', 'r')
    for line in archivoRoster:
        roster.append(line.strip())
    archivoRoster.close()
except FileNotFoundError:
    print('Creando archivo para la lista.')
    archivoRoster = open("roster.txt", "x")
    archivoRoster.close()

while True:
    print(f"\nLista: {roster}")
    print('1. Agregar Nombre\n2. Eliminar Nombre \n3. Salir')
    try:
        eleccion = int(input("Seleccion: "))
    except ValueError:
        break

    if eleccion == 1:
        toAdd = input('Nombre:')
        roster.append(toAdd)
    elif eleccion == 2:
        toRemove = input('Eliminar:')
        try:
            roster.remove(toRemove)
        except:
            print('Error al eliminar')
    else:
        break

# Guarda la lista en el archivo
try:     
    archivoRoster = open('roster.txt', 'w')
    for n in roster:         
        archivoRoster.write(n + '\n')
    archivoRoster.close()
except:
    print('Error al escribir.')



# ¿Cómo se llama el archivo .txt que se crea en este programa?
# R: roster.txt

# ¿Qué objeto de Python se utiliza para leer el archivo?
# R: open('roster.txt', 'r') pero es solo para leerlo

# ¿Cuál es el propósito del bucle while al leer el archivo?
# R:revis la lista y la imprime, ofrece las opciones o acciones y finalmente ejecuta la acción que el usuario elija

# ¿Qué sucede con los datos a medida que se leen del archivo?
# R: se guardan en rooster

# ¿Qué representa la variable n?
# R: cada elemento de la lista 

# ¿Qué debe hacerse siempre con un archivo después de terminar de acceder a él?
# R:   cerralo.. es como las bases de datos al parecer, que idealmente tb. es recomedable cerrarlas
