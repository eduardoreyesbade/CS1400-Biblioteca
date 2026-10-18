##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/17/2026)
# Tarea: Proyecto M07
##########################

# Manejo de textos y listas
mensaje = "bienvenido al curso de python"
# comidas = ["tacos", "pizza", "hamburguesa"]


# Mostrar datos
# print(mensaje)
# print(comidas[0])

# 1. Ejecuta el código. ¿Cómo se muestra el texto de la variable mensaje en la consola?
# R: "bienvenido al curso de python
# tacos"

# 2. Observa la instrucción print(comidas[0]). ¿Qué comida se imprimió en pantalla y en qué posición de la lista se encuentra?
# R: tacos, posicion inicial 0

# Modificación 1: Métodos de cadenas (Strings)

# Ejemplo de modificación:
# print(mensaje.upper())
# print(comidas[0].upper()) # ehhhh

#. Ejecuta el programa modificado. ¿Qué cambio ocurrió en la salida del texto respecto al código original?
# R: Se imprimio todo en mayusculas

# Modificación 2: Acceso a elementos de una lista

# Cambia el índice dentro del corchete comidas[0] para mostrar en pantalla la segunda comida de tu lista. ¿Qué número de índice tuviste que utilizar y por qué?
# R: 1, porque las listas parten en 0

# Modifica la lista comidas para que incluya tres de tus alimentos favoritos reales y vuelve a imprimir únicamente la segunda opción.
# R:
comidas = ["completos", "empanadas", "casuelas"]

print(comidas[1])

# 5. ¿Qué método elimina todos los elementos de la lista?
# R: comidas.clear()

# 6. ¿Qué método elimina un elemento de la lista por su valor de índice?
# R: comidas.pop(2)

# 7. ¿Qué método elimina un elemento de la lista usando el valor del elemento?
# R: comidas.remove("empanadas")

# 8. ¿Qué método agrega un elemento al final de la lista?
# R: comidas.append("sushi")

# 9. ¿Qué método agrega un elemento en una ubicación específica?
# R: comidas.insert(1, "sushi") en la posicion 1
print(comidas)