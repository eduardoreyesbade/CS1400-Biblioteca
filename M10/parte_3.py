import json

usuario = {
    "nombre": "Estudiante",
    "habilidades": ["Python", "HTML"],
    "activo": True
}

# GUARDAR
with open('datos.json', 'w') as f:
    json.dump(usuario, f, indent=4)

# LEER
with open('datos.json', 'r') as f:
    datos = json.load(f)
    print(f"Usuario: {datos['nombre']}")

# 11. ¿Qué hace la función json.dump()?
#R: guarad los datos en el json

# 12. ¿Cuál es la ventaja de usar with open(...) en lugar de .close()?
#R: El open cierra el archivo solo, y no es necesario usar close(). Esto funciona con error y todo. 