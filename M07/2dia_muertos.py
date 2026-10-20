##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/19/2026)
# Tarea: Proyecto M07 - Dia de los Muertps
##########################
# 
# Tarea 2: El Registro de los Ancestros (Diccionarios y Conjuntos)

# Tarea 2: Registro de visitas y ofrendas asignadas

# Diccionario con el ancestro (llave) y su platillo favorito (valor)
altares_familiares = {
    "Abuela Coco": "Tamales de dulce",
    "Tío Héctor": "Mole poblano",
    "Bizabuelo Julio": "Atole de chocolate"
}

# Lista con flores traídas por los visitantes (contiene duplicados)
flores_recibidas = ["Cempasúchil", "Nube", "Cempasúchil", "Terciopelo",
 "Nube", "Cempasúchil"]

# 4. Iteración en Diccionarios: Escribe un bucle for utilizando el método .items()
# para imprimir una frase por cada ancestro.
# (Ejemplo de salida esperada: "Para Abuela Coco preparamos: Tamales de dulce").
print("####### EJERCICIO 4 #######")

for key, value in altares_familiares.items():
    print("Para", key, "preparamos:", value)

# 5. Usa los métodos .keys() y .values() por separado para mostrar en pantalla
#  únicamente los nombres de los ancestros y luego únicamente los platillos.
print("\n")
print("####### EJERCICIO 5 #######")
print("####### Nombre Ancestros #######")

for key in altares_familiares.keys():
    print(key)
print("####### Platillos #######")
for value in altares_familiares.values():
    print(value)

# 6. Uso de Sets (Conjuntos): Para evitar contar flores repetidas en el inventario,
#  convierte la lista flores_recibidas en un set usando la función set().

print("\n")
print("####### EJERCICIO 6 #######")
flores_recibidas_set = set(flores_recibidas)
print(flores_recibidas_set)

# 7. Reflexión: ¿Cuántos elementos tenía la lista original de flores y cuántos quedaron
# en el conjunto? ¿Por qué los conjuntos (sets) son ideales para la limpieza de datos?
# R: otiginalmemte eran 6 y quedaron 3. 
# R: quita los duplicados... !
