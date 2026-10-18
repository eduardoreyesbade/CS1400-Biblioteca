##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/17/2026)
# Tarea: Proyecto M07
##########################


num_salon = {
    "Murphy": 304,
    "Feiz": 336,
    "Mack": 207,
    "Ball": 227,
    "Bristow": 321,
    "Cruz": 101
}

print("La longitud es", len(num_salon))

# Agregar un elemento adicional al diccionario
num_salon["Valle"] = 216
print("La longitud ahora es ", len(num_salon))

print( num_salon.get("Valle") )
print( num_salon["Murphy"])

num_salon["DeLeon"] = 147

num_salon["Hernandez"] = 323
print("La longitud ahora es ", len(num_salon))

print( num_salon.get("Murphy") )


# 1. Observa el diccionario num_salon en el código de abajo. ¿Qué signo de puntuación separa la clave (key) del valor (value)?
# R: los dos puntos

# 2. Nota la coma al final de cada par clave-valor. ¿Por qué crees que no hay una coma después de "Cruz"?
# R: Para seoara el siguiente par ordenado de key y value.

# 3. ¿Cuántos pares clave-valor hay inicialmente en el diccionario?
# R: solo 6

# 4. Ejecuta el programa. ¿Qué reporta la función len() como la longitud del diccionario?
# R: inicial 5, luego 7, porque se agrego un nuevo par key - value

# 5.Agrega a "DeLeon" al diccionario asignándole el salón 147.
# R: Listo, se agrego a DeLeon con el numero de salon 147.

# 6. Ejecuta el programa. ¿Cambia la longitud del diccionario al agregar a DeLeon?
# R: Si, cambio a 8.

# 7.Observa la puntuación para agregar elementos adicionales al diccionario. Agrega un instructor adicional "Hernandez" con el número de salón 323. Asegúrate de usar los corchetes [] para agregar al instructor.
# R: num_salon["Hernandez"] = 323, listo

# 8.Ejecuta el programa. ¿Qué se imprime cuando se usa el método .get() al imprimir el instructor Valle? ¿La clave o el valor?
# R: Se imprime el valor del instructor Valle: 216.

# 9.¿Qué se imprime cuando usas los corchetes para imprimir los datos?
# R: Igual que antes, se imprime el valor del instructor, este caso Murphy: 304.

# 10. ¿Ves alguna diferencia entre acceder a los datos usando los corchetes [] y el método .get()?
# R: Sí, el método .get() no lanza un error si la clave no existe, mientras que los corchetes sí lo hacen.

# 11. Agrega una sentencia print para imprimir el número de salon de Murphy.
# R: print( num_salon.get("Murphy") )
