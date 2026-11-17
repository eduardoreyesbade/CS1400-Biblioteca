# TODO 2: lineas para arreglar el problema con los acentos.
import sys
sys.stdout.reconfigure(encoding='utf-8')

from api import obtener_coordenadas

print("[TEST] Iniciando pruebas de la API...")

# Prueba 1: Ciudad válida con acentos o espacios
print("\n--- Probando una ciudad válida (Bogotá) ---")
resultado_bogota = obtener_coordenadas("Bogotá ")
print(resultado_bogota)

# Prueba 2: Otra ciudad válida en otro país
print("\n--- Probando otra ciudad (Tokio) ---")
resultado_tokio = obtener_coordenadas("Tokyo")
print(resultado_tokio)

# Prueba 3: Ciudad inventada o que no existe (para probar el manejo de errores)
print("\n--- Probando un lugar falso (AtlantisXYZ) ---")
resultado_falso = obtener_coordenadas("AtlantisXYZ123")
print(resultado_falso)

# TODO 3: Intenta con otra ciudad.
print("\n--- Probando otra ciudad (Ogden, Estados Unidos) ---")
resultado_ogden = obtener_coordenadas("Ogden, Estados Unidos")
print(resultado_ogden)

print("\n[FIN] Pruebas finalizadas.")

# TODO 1: Que notas raro en la salida al correr test_api?
# Los acentos y las enes salen mal. En lugar de "ciudad valida (Bogota)" con
# acentos, la consola imprime caracteres raros como "v?lida (Bogot?)".
# Esto pasa porque la consola de Windows no usa UTF-8 por defecto, asi que no
# sabe como mostrar los caracteres que no son del alfabeto ingles basico.
# El programa no se rompe, nada mas se ve mal la salida.

"""
Si quieres probar ciudades que se llaman igual en distintos países
(por ejemplo, San José en Costa Rica y San José en California, EE. UU.),
puedes escribir la consulta de manera más específica como "San Jose, Costa Rica"
"""
#TODO 4:
