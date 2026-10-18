##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/17/2026)
# Tarea: Proyecto M07
##########################

def Even_Numbers(lista_origen):
    even = []

    # TODO: Itere la lista_origen y agregue a 'even' solo los números pares

    for num in lista_origen:
        if num % 2 == 0:
            even.append(num)
    return even


def Ten_Or_Less(lista_origen):
    # TODO: Cree una lista vacía, busque valores <= 10 y devuélvala
    
    for num in lista_origen:
        if num <= 10:
            print(num)
    pass


def Calcular_Diferencias(lista_origen):
    # TODO: Calcule la distancia entre números consecutivos
    # Ejemplo: [10, 7, 15] -> [3, 8]

    diferencias = []
    
    for i in range(len(lista_origen) -1):
        primero = lista_origen[i]
        segundo = lista_origen[i+1]
        diferencia = abs(primero - segundo)
        diferencias.append(diferencia)

#        break 
    return diferencias

if __name__ == "__main__":
    numeros = [10, 7, 15]
    print(Calcular_Diferencias(numeros))

