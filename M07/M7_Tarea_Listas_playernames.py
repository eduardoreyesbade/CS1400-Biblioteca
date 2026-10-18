##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/17/2026)
# Tarea: Proyecto M07
##########################

playerNames = ["Adam", "Bethanie", "Carrie", "Doug", "Eddie"]
playerNumbers = [5, 2, 6, 13, 0]

# 1. Adam ha dejado el equipo. Use 'remove' para eliminarlo:

# hice un diccionario primero, para agregar o eliinar simultaneamente nombre y numeros. 
equipo = dict(zip(playerNames, playerNumbers))
# equipo.pop("Adam")
# print(equipo)

# 2. Elimine el primer número de la lista (5) usando 'pop':
"""
for nombre in equipo:
    print(nombre)
    break

equipo.pop(nombre)
print(equipo)

# 3. Use 'append' para agregar estas variables a sus listas:

name = "Lucas" 
num = 7
playerNames.append(name)
playerNumbers.append(num)
equipo = dict(zip(playerNames, playerNumbers))

print(equipo)
"""
# 4. Use 'insert' para que "Raven" (número 1) sea la primera en la lista:

playerNames.insert(0, "Raven")
playerNumbers.insert(0, 9)
equipo = dict(zip(playerNames, playerNumbers))

print(equipo)

