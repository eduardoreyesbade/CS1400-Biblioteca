# ListaNumeros

try:
    suma = 0
    # 1. Abre el archivo numeros.txt aquí
    archivo = open('./numeros.txt', 'r')

    for line in archivo:
        # 2. Convierte la línea a entero
        num = int(line.strip())
        print(num)
        suma += num

    print(f"Total: {suma}")
    archivo.close()

except Exception as err:
    print(err)

# 7. ¿Cuál es el resultado de la suma de los números proporcionados?
# R: 179 (note que no se separan por comas, sino que se listas hacia abajo linea por linea)

# 8. Si agregas la palabra "Python" al archivo de texto, ¿qué error muestra el programa?
# R: invalid literal for int() with base 10: 'Python'

# 9. ¿Por qué es necesario usar .strip() antes de convertirla a número?
# R: Para quitar los salts de linea u espacios, es para limpiar el dato

# 10. Si el archivo tiene 9 números, ¿cuántas veces se ejecuta el bloque dentro del for?
# R: 9
