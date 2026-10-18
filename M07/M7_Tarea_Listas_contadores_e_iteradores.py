##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/17/2026)
# Tarea: Proyecto M07
##########################

import random

def Generate_Numbers():
    numbers = []
    for i in range(20):
        num = random.randint(1, 50)
        numbers.append(num)
    return numbers

# Llamada a la función
mis_numeros = Generate_Numbers()

print(mis_numeros)

# 10. ¿Qué tipo de datos se está agregando a la lista numbers?
# R: intergers, en este caso aleatorios

# 11. ¿Cuántos números se están agregando exactamente a la lista?
# R: 20

# 12. ¿Qué devuelve (return) la función al final de su ejecución?
# R: 20 numeros aleatorios entre 1 y 50
