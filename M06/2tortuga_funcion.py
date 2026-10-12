
##########################
# Cybersecurity - CS1400
# Eduardo Reyes
# 10/06/2026)
# Tarea: Proyecto M06
##########################
# 
# 
"""
====================================================================
Mi Primera Función en Turtle
====================================================================
NOMBRE: Eduardo Reyes
Objetivo:
Entender cómo encapsular código en una función para reutilizarlo y 
dibujar figuras personalizadas de manera sencilla.

Corre este programa y toma captura del resultado
====================================================================
"""

import turtle

# ==================================================================
# 1. Configuración de la Pantalla y Tortuga
# ==================================================================
pantalla = turtle.Screen()
pantalla.bgcolor("lightyellow")
pantalla.title("Funciones y Figuras")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)


# ==================================================================
# 2. DEFINICIÓN DE LA FUNCIÓN
# ==================================================================

# Función para 

def dibujar_figura(lados, tamaño, color_borde, color_relleno):
    
#    Dibuja cualquier polígono regular basado en el número de lados.
    
#    Parámetros:
#    - lados: Número de lados que tendrá la figura (ej. 3 para triángulo, 5 para pentágono).
#    - tamaño: Longitud de cada lado en píxeles.
#    - color_borde: Color de las líneas.
#    - color_relleno: Color del interior de la figura.

    
    # La suma de los ángulos exteriores de cualquier polígono es 360 grados.
    angulo = 360 / lados

    # Configuración de colores
    t.color(color_borde, color_relleno)
    t.begin_fill()

    # Un bucle 'for' que repita el avance y el giro 'lados' veces.
    for _ in range(lados):
        t.forward(tamaño)
        t.left(angulo)

    t.end_fill()


# Función auxiliar para 
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# ==================================================================
# 3. DEMOSTRACIÓN / PRUEBAS (Demuestra el poder de la función)
# ==================================================================

# Dibujar una estrella/triángulo (3 lados)
mover(-300, 0)
dibujar_figura(lados=3, tamaño=80, color_borde="darkgreen", color_relleno="lightgreen")

# Dibujar un pentágono (5 lados)
mover(-200, 0)
dibujar_figura(lados=5, tamaño=60, color_borde="purple", color_relleno="plum")

# Dibujar un hexágono (6 lados)
mover(0, 0)
dibujar_figura(lados=6, tamaño=50, color_borde="darkblue", color_relleno="skyblue")


# Dibujar un hexágono (6 lados)
mover(200, 0)
dibujar_figura(lados=8, tamaño=50, color_borde="darkblue", color_relleno="red")

""" 
    # La suma de los ángulos exteriores de cualquier polígono es 360 grados.
angulo = 360 / 4

    # Configuración de colores
t.color("#F6771C", "#C9442C")
t.begin_fill()

    # Un bucle 'for' que repita el avance y el giro 'lados' veces.
for _ in range(4):
    t.forward(100)
    t.left(angulo)

    t.end_fill()


# Función auxiliar para 
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
# ==================================================================
# 4. PREGUNTAS
# ==================================================================

1.  ¿Cuantas funciones hay en este programa? Que proposito tienen? En tus propias palabras agrega comentario completo.
R: Hay dos funciones:dibujar_figura y mover. la primera dibuja las formas de acuerdo a la informacion y la segunda, hace el elemento que dibuja se desplace. 

2. ¿Qué parámetro de la función 'dibujar_figura' tendrías que cambiar para hacer un octágono (8 lados)?
R: Se cambia solo e l parametro a 8, que son los lados deseados. 

3 ¿En que numero de linea termina la funcion mover?
R: La funcion mover termina en la linea 93, en este caso porque agregue una 4a fihura de 8 lados.

4. Bajo la seccion de pruebas, intenta hacer una nueva figura sin el uso de la funcion dibujar_figura.
R: 

# La suma de los ángulos exteriores de cualquier polígono es 360 grados.
angulo = 360 / 4

# Configuración de colores
t.color("#F6771C", "#C9442C")
t.begin_fill()

    # Un bucle 'for' que repita el avance y el giro 'lados' veces.
for _ in range(4):
    t.forward(100)
    t.left(angulo)

    t.end_fill()


# Función auxiliar para 
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


5. Guarda una captura de pantalla con las 4 figuras en la carpeta M06.
      
"""


pantalla.exitonclick()