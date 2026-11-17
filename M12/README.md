#######
## Eduado Reyes
## 17 de Noviembre, 2026
#######


## Preguntas para familia_madrigal.py
#1. ¿Qué pasaría si quitas @abstractmethod y creas un Madrigal("Alguien", 30)? Pruébalo y explica qué error aparece y por qué es útil.

R: Lo probé de las dos formas. Con `@abstractmethod`, Python no deja crear el objeto y marca este error:

```
TypeError: Can't instantiate abstract class Madrigal without an implementation
for abstract method 'usar_don'
```

Si le quito el `@abstractmethod`, el objeto sí se crea, pero queda con el `usar_don()` de la clase base, que solo tiene `pass` y no hace nada: en `dia_de_milagros()` ese personaje pasaría de largo sin mostrar ningún don.

Parece  útil porque el error aparece de inmediato, en el momento de crear el objeto,
y no más tarde con el programa ya corriendo. `@abstractmethod` funciona como un
contrato: obliga a que cada personaje nuevo escriba su propio don.

#2. En Casita.dia_de_milagros() solo se escribe madrigal.usar_don(). ¿Por qué no necesitamos un if para cada personaje? (Pista: polimorfismo).

R:para eso esta el polimorfismo. Todos los personajes heredan de `Madrigal` y todos tienen un método que se llama igual, `usar_don()`, aunque por dentro cada uno haga algo distinto. Python revisa al momento de ejecutar de qué clase es el objeto y llama la versión que le toca.

Por eso la `Casita` no necesita saber quién es quién. La prueba está en el punto 5: agregué a la Abuela Alma y no cambié ni una línea de `Casita`.

#3. ¿Por qué la energía es __energia y no simplemente energia? Intenta hacer familia[0].energia = 500 y luego familia[0].__energia = 500. ¿Qué diferencia notas?

R: Los dos guiones bajos activan el *name mangling*: por dentro Python le cambia el nombre a `_Madrigal__energia`, para que no se modifique por accidente desde afuera.

#4. Si quisieras que todos los Madrigal tuvieran una “casa” (habitación), ¿en qué clase lo agregarías y por qué?

R; En la clase base `Madrigal`, dentro de `__init__` (algo como `self.habitacion = habitacion`). Si lo pongo ahí, los nueve personajes lo heredan de una sola vez y no tengo que repetir el mismo código en cada clase hija; si después cambio cómo funciona la habitación, la cambio en un solo lugar.


## Tareas para programar
#5. Agrega un nuevo personaje, por ejemplo Abuela Alma, con un don propio (como “proteger a la familia”) y añádelo a la lista familia. Observa que no tienes que cambiar nada en Casita.

R: clase `AbuelaAlma(Madrigal)` con su `usar_don()` (cuida la vela milagrosa, gasta 10 de energía) y agregada a la lista `familia`. Efectivamente **no toqué nada de `Casita`**.

#6. Modifica Mirabel para que, además, tenga un atributo tiene_gafas = True usando super().__init__(), igual que lo hace Antonio.

R :`Mirabel` ahora tiene su propio `__init__` que primero llama a `super().__init__(nombre, edad)` (para guardar nombre, edad y energía) y después agrega `self.tiene_gafas`. Cuando usa su don imprime además
"(se acomoda sus gafas verdes)".

#7. Agrega un método esta_cansado() en Madrigal que devuelva True si la energía es menor a 30. Luego haz que dia_de_milagros() salte a quien esté cansado y diga que necesita descansar.

R: `esta_cansado()` está en la clase base, así lo heredan todos. `dia_de_milagros()` lo revisa antes de llamar al don y usa `continue` para saltarse a quien esté cansado. En la corrida se ve así, cuando Bruno se queda con 10% de energía:

```
🛏️ Bruno está muy cansado hoy, necesita descansar.
```

#8. Crea una clase Villano o Visitante que no herede de Madrigal pero tenga también usar_don(). ¿Funciona con dia_de_milagros()? ¿Qué te dice eso sobre cómo funciona Python?

R: Creé la clase `Visitante` (Mariano), que no hereda de `Madrigal`, y aun así la Casita lo trata igual que a los demás:

```
🧳 Mariano no es de la familia, pero trae café de regalo.
```

#9. Crea una subclase Antonio que, al cumplir la ceremonia, reciba un don y que el método cumplir_anios() aumente la edad en uno. Después haz que Pepa cambie su estado_de_animo según su energía (si baja de 50, se pone “triste”).

R: `Antonio` ahora empieza con `self.don = None`, tiene `ceremonia(don)` para recibir su don y `cumplir_anios()` q ue le suma un año a la edad. Si todavía no hubo ceremonia y trata de usar su don, avisa que está esperando .

`Pepa` revisa su energía al final de `usar_don()`, **después** de gastarla, para que el cambio se note la próxima vez. En la corrida:

```
Antonio cumple años: ahora tiene 6.
La puerta de Antonio brilla! Su don es: hablar con los animales.
...
cae una tormenta con rayos porque Pepa está enojada.
 Pepa se cansó y su ánimo cambió a triste.
```

#10. Haz un pequeño menú con input() donde el usuario elija un personaje y use su don, mostrando cómo baja su energía.

R: la función `menu_dones()` muestra la lista numerada, pide un número con `input()` y se repite hasta que el usuario escribe 0. Valida que no escriban texto y que el número exista en la lista. Después de cada don muestra el cambio de energía:

```Antonio habla con los animales: jaguar, tucán, capibara, coatí.
   Energía de Antonio: 80% → 70%
```

Un truco para motivar

Si logras agregar un personaje nuevo sin tocar la clase Casita, ¡ya entendiste el poder del polimorfismo! Esa es justamente la ventaja de la POO: añadir cosas nuevas sin romper lo que ya funciona.

