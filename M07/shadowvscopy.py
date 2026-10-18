##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/17/2026)
# Tarea: Proyecto M07
##########################

import copy

animalesRefugiados = {"perro": 49, "gato": 38, "conejo": 14}
# refugioOriginal = animalesRefugiados
refugioOriginal = copy.deepcopy(animalesRefugiados) 

animalesRefugiados['perro'] += 2
animalesRefugiados["huron"] = 2
# quitar 3 gatos del refugio
animalesRefugiados["gato"] -= 3
# agregar 4 serpientes del refugio
animalesRefugiados["serpientes"] = 4

print(animalesRefugiados)
if animalesRefugiados["perro"] > 50:
    print("Lleno o Full, no traigan mas perros")

if animalesRefugiados.get('raton') is None:
    print("No Ratones")
# test si es copia profunda o superficial
print(refugioOriginal)


# 1. ¿Cuántos perros hay en el refugio al principio?
# R: 49 perros

# 2. ¿Cuántos perros se están agregando al refugio?
# R: 2 perros mas

# 3. Escribe la línea de código para eliminar 3 gatos del refugio.
# R: animalesRefugiados["gato"] -= 3

# 4. Observa el código para agregar los hurones. ¿Cuántos se agregaron?
# R: 2 hurones que no existian antes, se agregaron al diccionario.

# 5. Escribe el código para agregar 4 serpientes al refugio.
# R: animalesRefugiados["serpientes"] = 4   

# 6. Escribe una sentencia if para imprimir "Lleno" si el número de perros es mayor a 50.
# R: Listo, en el codigo 

# 7. Escribe una sentencia if para imprimir "No Ratones" si "raton" no es una clave en el diccionario animalesRefugiados.
# R: Listo, en el codigo

# 8. Nota que la variable refugioOriginal es igual a la variable animalesRefugiados. ¿Es esta una copia superficial o profunda?
# R: Deberia ser na copia superficial, no cambia en nada el cptenido. 

# 9. Escribe el comando para mostrar los animales de refugioOriginal al final del segmento de código. ¿Muestra los animales originales?
# R: No, muestra los animales que fueron agregados.

# 10. Cambia refugioOriginal para que sea una copia profunda (deep copy) de animalesRefugiados (recuerda importar la librería copy). ¿Muestra los animales originales ahora?
# R: refugioOriginal = copy.deepcopy(animalesRefugiados) 

# 11. ¿Qué diferencia notas entre una copia profunda y una copia superficial?
# R: no son para nada lo mismo. Una copia prgunfa es exacamente eso, una fiel representacion del original. La superficial es solo una composicion de los elementos del original, pero no es el original.