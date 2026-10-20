##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/19/2026)
# Tarea: Proyecto M07 - Dia de los Muertps
##########################
# 
# 
"""Tarea 1: Preparando la Oferta (Listas y Tuplas)

"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]

# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)

ofrendas_tupla = "Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"

NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")

# Mostrar la segunda ofrenda (índice 1)
print("Segunda ofrenda:", ofrendas[1])

ofrendas.append("Incienso copal")
ofrendas.sort()
print(ofrendas)
print(NIVELES_ALTAR)
# NIVELES_ALTAR[0] = "Gloria"
# NIVELES_ALTAR.append("Gloria")
# print(NIVELES_ALTAR)

for posicion, ofrenda in enumerate(ofrendas, start=1):
    print(posicion, ofrenda)


# Ejecuta el código. Observa qué elemento se imprime al pedir el índice 1.
# 1. Modificación 1 (Listas): Agrega un nuevo elemento a la lista ofrendas usando
# .append("Incienso copal") y luego ordena la lista alfabéticamente usando
# la función .sort().  ¿Qué notas del variable en linea #12?
# R: Al ejeuctar se imprime Segunda ofrenda: Flor de cempasúchil
# R: luego de ordenar alfabeticamente, imprimi ambos. El NIVELES_ALTAR no se vio afectado, solo el ofrenas. 

#2. Modificación 2 (Tuplas): Intenta modificar el primer elemento de la tupla escribiendo
#  NIVELES_ALTAR[0] = "Gloria".
# ¿Qué sucede al ejecutar el código y por qué no permite realizar este cambio?
# R: Hice dos intente con alterar un elemento y agregar son append para probar. Entra en error. 

# 3. Utiliza la función enumerate() dentro de un bucle for para imprimir cada ofrenda
# de tu lista junto con su número de posición en el altar.
# R: Listo! No digamos que quedo hermoso pero es funcional.
