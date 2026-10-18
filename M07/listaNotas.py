##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/17/2026)
# Tarea: Proyecto M07
##########################


# Ejemplo de conteo de palabras
text = "sana sana curita de rana sana sana pomada de sapo sana sana hoy y manana manana y hoy, 2"

lst = text.split()
plbList = dict()

for x in lst:
    if x not in plbList:
        plbList[x] = 1
    else:
        plbList[x] += 1

for i in plbList:
    print (i, plbList[i])

# Ejemplo de conteo de calificaciones
notas = "A A A B B A C A B C C E A B A C C C A B B B A B A A A C D A B B C C A A A B A B A C A B B A"
listaNotas = notas.split()
notasDiccionario = dict()

for i in listaNotas:
  if i not in notasDiccionario:
    notasDiccionario[i] = 1
  else:
    notasDiccionario[i] += 1

for i in notasDiccionario:
  print(i, notasDiccionario[i])

# test 1
print(plbList)
# test 2 solo para estar seguro que el diccionario de notas se creo correctamente
print(notasDiccionario["A"]) 

# 1. Observa la variable listaNotas. ¿Es una lista o un diccionario?
# R: lista 

# 2. ¿Qué hace la función split()? (Puedes consultar lecciones anteriores).
# R: toma el string y lo divide en una lista de palabras

# 3. Observa la variable notasDiccionario. ¿Está definida como una lista o un diccionario?
# R: ese si es un diccionario

# 4. ¿Hay valores en el diccionario o está vacío?
# R: vacio al comenzar

# 5. Observa el bucle for. ¿Está iterando a través de la lista o del diccionario?
# R: Esta iterando en el diccionario, que se creo a partir d la lista

# 6. Dado que la primera puntuación en listaNotas es "A", ¿el código ejecutaría la sentencia if o la sentencia else dentro del bucle?
# R: Con la primera A, el if. 

# 7. El comando es notasDiccionario[i] = 1, cuando i es igual al texto "A", ¿cuál es el par clave-valor que se agrega al diccionario?
# R: "A": 1

# 8. La calificación "A" se agrega varias veces. La primera vez, pasa por el if. La segunda vez, pasará por el comando else. Hablando de esa segunda vez cuando i = "A", el par clave-valor es inicialmente "A": 1, ¿a qué valor se actualiza cuando se ejecuta el comando notasDiccionario[i] += 1?
# R: pasara de 1 a 2. 

# 9. Ejecuta el programa, ¿cuántas veces aparece la calificación "A" en los puntajes?
# R: 20