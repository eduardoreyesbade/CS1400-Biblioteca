# Parte 1: Código Vulnerable a Errores
"""
lst = [1, 3, 7, 3]

# Entrada de datos
num = int(input("Ingrese un número entero: "))

# Operación 1: División
print(10 / num)

# Operación 2: Acceso a Lista
print(lst[num])

# Operación 3: Continuación
print("El programa continuó con éxito.")


# ¿Por qué la Operación 1 (10 / num) fallará si el usuario ingresa 0?
# R: Porque no se puede dividir por cero. ZeroDivisionError: division by zero

# ¿Por qué la Operación 2 (lst[num]) fallará si el usuario ingresa 100?
# R: Porque no hay tantos elementos en la lista. IndexError: list index out of range

# Ingreso usuario
# R: con "dos", 0 o 100, todos error. 

# Parte 2: Control de Flujo con

try:
    lst = [1, 3, 7, 3]
    num = int(input("Ingrese un número entero: "))
    
    print(10 / num)
    print(lst[num])

except ValueError:
    print("❌ Error: Debes ingresar un número entero válido (sin letras).")



# 4. Ejecuta el código anterior e ingresa "dos". ¿Qué mensaje se imprime? ¿Se ejecuta la última línea de "El programa continúa..."?
# R: Error: Debes ingresar un número entero válido (sin letras). Si se muestra

# 5. Ejecuta el código e ingresa 0. ¿Por qué se activa el mensaje "Ocurrió un error general" en lugar del de ValueError?
# R: ❌ Ocurrió un error general. Si se muestra.

# 6. Modificación de código 1: Agrega un bloque except ZeroDivisionError específico con el mensaje: "❌ Error: No es posible dividir entre cero."
# R: "except:
# R:    print("❌ Ocurrió un error general.")"

# 7. Modificación de código 2: Identifica el tipo de error que ocurre al intentar acceder a un índice inexistente en la lista lst (al ingresar 100). Agrega un bloque except específico para capturar dicho error con un mensaje descriptivo.
# R: "except IndexError:
# R:   print('Ese índice no existe en la lista.')"

# 8. Pega tu código corregido con las 3 excepciones específicas aquí.
except ZeroDivisionError:
    print("❌ Error: No es posible dividir entre cero.")

except IndexError:
    print('Ese índice no existe en la lista.')

except:
    print("❌ Ocurrió un error general.")

print("El programa continúa su ejecución normal...")



# Parte 3: Rastrear Errores con traceback y Controlar r
# A. Diagnóstico técnico con traceback

import traceback

try:
    num = int(input("Ingrese un número: "))
    print(10 / num)
except ValueError as e:
    print("⚠️ Capturamos un ValueError. Detalle técnico:")
    s = traceback.format_tb(e.__traceback__)
    print(s)

print("El programa continúa...")

# 10. En la línea except ValueError as e, ¿qué representa la variable e?
# R: guarda el valor del error. 

# 11. ¿Qué ventaja ofrece la función traceback.format_tb() frente a simplemente mostrar un mensaje amigable al usuario?
# R: Permite ver la que pasa con el error, lo que ayuda a identificar dónde ocurrió el problema y eventualmente cómo solucionarlo.

# B. Validación explícita con raise y garantía con finally

print("--- Validación de Rango ---")
num = 0

while num < 1 or num > 10:
    try:
        num = int(input("Ingrese un número del 1 al 10: "))
        
        if num < 1 or num > 10:
            raise Exception("El número está fuera del rango permitido.")
            
    except ValueError:
        print("❌ Error: Formato incorrecto, se esperaba un número.")
    except Exception as e:
        print(f"⚠️ Error de validación: {e}")
    finally:
        print("🔔 [Bloque Finally] Intento de entrada finalizado.")

print(f"¡Número válido ingresado con éxito! ({num})")
"""

# 12. ¿En qué situaciones se ejecutará el código dentro del bloque finally?
# R: Yo creo que siempre..es como independiente del si hay o no un error. 

# 13. ¿Qué función cumple la palabra clave raise en el condicional if num < 1 or num > 10?
# R: especifica el error que se va a lanzar, en este caso un error de validación.

# 14. ¿Qué ocurre en el bucle while cuando el usuario ingresa un valor válido (ejemplo: 5)?
# R: Se cumple la condicioncio, se sale  del bucle y se imprime el mensaje de éxito.

# Parte 4: Aplicación Práctica — Calculadora Robusta

def calculadora_segura():
    print("\n--- Calculadora Robusta ---")
    
    while True:
        try:
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            op = input("Operación (+, -, *, /): ")

            # Validar operador permitido
            if op not in ['+', '-', '*', '/']:
                # TODO 1: Lanza (raise) un ValueError con el mensaje "Operador no válido"
                pass

            # Realizar cálculos
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                resultado = n1 / n2

            print(f"✅ Resultado: {resultado}")
            break  # Salir del bucle si el cálculo se realizó con éxito

        # --- MANEJO DE EXCEPCIONES ---

        # TODO 2: Captura el error de formato cuando el usuario ingresa texto en lugar de números
        # except ...:
        #     print("❌ Error: Ingrese valores numéricos válidos.")

        # TODO 3: Captura la división por cero
        # except ...:
        #     print("❌ Error: No se puede dividir entre cero.")

        # TODO 4: Captura el ValueError (generado por el operador inválido) y muestra e
        # except ValueError as e:
        #     print(f"❌ Error de entrada: {e}")

        except Exception as e:
            print(f"❌ Error no esperado: {e}")
        
        finally:
            # TODO 5: Muestra siempre un mensaje de cierre de intento
            pass

calculadora_segura()


# 15. ¿Cuál es el propósito de la instrucción break colocada al final de la sección try?
# R: si todo va bien, se sale del bucle. 

# 16. Si el usuario ingresa n2 = 0 y op = '/', ¿se llega a ejecutar la línea print(f"✅ Resultado: {resultado}")? Explica la secuencia del flujo de ejecución           .
# R: no, porque lo captura el error de devision pr cero. 

# 17/ ¿Qué sucedería con la experiencia de usuario si omitimos el bucle while True en este programa?
# R: El programa se cerraría y no permitiría al usuario intentar nuevamente.
