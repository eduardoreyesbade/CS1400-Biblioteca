##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/19/2026)
# Tarea: Proyecto M07 - Dia de los Muertps
##########################

# Tarea 3: Organización de calaveritas y conteo de caracteres

calaveritas = ["123456", "Alebrije", "Catrina", "Cempasúchil", "Pan de muerto", "Papel picado"]

# Filtrar palabras que tengan más de 7 letras (Método tradicional)
largas_tradicional = []
"""
for elemento in calaveritas:
    if len(elemento) > 7:
        largas_tradicional.append(elemento)
"""
largas_tradicional = [elemento for elemento  in calaveritas if len(elemento) > 7]

print("Palabras largas (Tradicional):", largas_tradicional)

#8. Comprensión de Listas (List Comprehension): Re-escribe el bloque de código anterior
#  en una sola línea utilizando comprensión de listas para crear largas_comprehension.
# R: Funciona, agregue un elemento con solo 6 caracters y no lo muestra.

#9. Utiliza una comprensión de listas para convertir todos los elementos de la lista
# calaveritas a mayúsculas usando .upper().
# R:

largas_tradicional = [elemento.upper() for elemento in calaveritas]
print("Palabras largas (Mayusculas):", largas_tradicional)


# 10. Comprensión de Diccionarios (Dictionary Comprehension): Crea un diccionario a
#  partir de  la lista calaveritas donde la llave sea el nombre del elemento y el valor
# sea la cantidad de letras que tiene esa palabra (usando la función len()).

letras_calaveritas = {elemento: len(elemento) for elemento in calaveritas}
print(letras_calaveritas)

# 11. Pregunta de análisis: ¿Qué ventaja ofrece escribir la solución con comprensiones
# en lugar de usar un bucle for tradicional con un .append()?
# R: se reduce enormemente el escribir codigo, pero sinceramemte, la gramatica que hay que usar no es trivial.. es mas clara y sencilla en un bucle comun y corriente. 

