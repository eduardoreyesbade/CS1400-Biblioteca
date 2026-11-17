"""
La familia Madrigal de Encanto: un ejemplo de Programación Orientada a Objetos.

Conceptos que se muestran:
  1. Clases y objetos
  2. Herencia (Madrigal -> personajes con don)
  3. Polimorfismo (cada don se usa de forma distinta)
  4. Encapsulamiento (atributo privado: la energía)
  5. Métodos especiales (__str__)
  6. Composición (la Casita contiene a los Madrigal)

-------------------------------------------------------------------
Tarea M12 - POO: Clases y Funciones
Alumno: Eduardo Reyes
Fecha: 17 de noviembre de 2026
Los puntos 5 al 10 están resueltos en el código (busca "# PUNTO n").
Las respuestas a las preguntas 1 a 4 están al final del archivo.
-------------------------------------------------------------------
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# CLASE BASE (abstracta): todo Madrigal comparte estas cosas
# ---------------------------------------------------------------
class Madrigal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.__energia = 100  # atributo privado (encapsulamiento)

    # --- Encapsulamiento: solo se accede a la energía con estos métodos ---
    @property
    def energia(self):
        return self.__energia

    def gastar_energia(self, cantidad):
        self.__energia = max(0, self.__energia - cantidad)

    def descansar(self):
        self.__energia = 100
        print(f"😴 {self.nombre} descansa y recupera toda su energía.")

    # PUNTO 7: avisa si al personaje ya casi no le queda energía.
    # Va en la clase base para que TODOS los Madrigal lo hereden.
    def esta_cansado(self):
        """Devuelve True si al personaje le queda menos de 30 de energía."""
        return self.energia < 30

    # --- Cada hijo DEBE definir su propio don (polimorfismo) ---
    @abstractmethod
    def usar_don(self):
        pass

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - Energía: {self.energia}%"


# ---------------------------------------------------------------
# CLASES HIJAS: heredan de Madrigal y redefinen usar_don()
# ---------------------------------------------------------------
class Mirabel(Madrigal):
    # PUNTO 6: Mirabel ahora tiene su propio atributo, igual que Antonio.
    # Primero llamamos al constructor del padre con super().__init__() para
    # que se guarden nombre, edad y energía, y luego agregamos lo nuevo.
    def __init__(self, nombre, edad, tiene_gafas=True):
        super().__init__(nombre, edad)
        self.tiene_gafas = tiene_gafas

    def usar_don(self):
        print(f"🔍 {self.nombre} no tiene don mágico, ¡pero tiene el don de ser valiente!")
        if self.tiene_gafas:
            print("   (se acomoda sus gafas verdes)")
        self.gastar_energia(5)


class Isabela(Madrigal):
    def usar_don(self):
        print(f"🌸 {self.nombre} hace crecer flores y cactus por todos lados.")
        self.gastar_energia(15)


class Luisa(Madrigal):
    def usar_don(self):
        print(f"💪 {self.nombre} levanta un burro como si nada.")
        self.gastar_energia(25)


class Julieta(Madrigal):
    def usar_don(self):
        print(f"🍲 {self.nombre} cocina arepas que sanan cualquier herida.")
        self.gastar_energia(10)


class Pepa(Madrigal):
    def __init__(self, nombre, edad, estado_de_animo="feliz"):
        super().__init__(nombre, edad)  # llama al constructor del padre
        self.estado_de_animo = estado_de_animo

    def usar_don(self):
        clima = {
            "feliz": "☀️ sale el sol",
            "triste": "🌧️ empieza a llover",
            "enojada": "⛈️ cae una tormenta con rayos",
        }
        print(f"{clima[self.estado_de_animo]} porque {self.nombre} está {self.estado_de_animo}.")
        self.gastar_energia(15)

        # PUNTO 9 (segunda parte): si Pepa se queda sin energía, se pone triste.
        # Lo revisamos DESPUÉS de gastar la energía, así el cambio se nota la
        # próxima vez que use su don.
        if self.energia < 50 and self.estado_de_animo != "triste":
            self.estado_de_animo = "triste"
            print(f"   😔 {self.nombre} se cansó y su ánimo cambió a triste.")


class Dolores(Madrigal):
    def usar_don(self):
        print(f"👂 {self.nombre} escucha un susurro a kilómetros de distancia.")
        self.gastar_energia(10)


class Camilo(Madrigal):
    def usar_don(self):
        print(f"🎭 {self.nombre} se transforma en otra persona. ¡Qué travieso!")
        self.gastar_energia(20)


class Antonio(Madrigal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.animales = ["jaguar", "tucán", "capibara", "coatí"]
        # PUNTO 9 (primera parte): todavía no ha recibido su don.
        self.don = None

    # PUNTO 9: la ceremonia le entrega su don.
    def ceremonia(self, don):
        """Le da un don a Antonio, como cuando se abre su puerta en la película."""
        self.don = don
        print(f"🚪 ¡La puerta de {self.nombre} brilla! Su don es: {don}.")

    # PUNTO 9: cada cumpleaños le suma un año a su edad.
    def cumplir_anios(self):
        """Aumenta la edad en uno y devuelve la edad nueva."""
        self.edad += 1
        print(f"🎂 {self.nombre} cumple años: ahora tiene {self.edad}.")
        return self.edad

    def usar_don(self):
        # Si todavía no hubo ceremonia, no puede usar ningún don.
        if self.don is None:
            print(f"🙁 {self.nombre} todavía no tiene don, está esperando su ceremonia.")
            return
        print(f"🐆 {self.nombre} habla con los animales: {', '.join(self.animales)}.")
        self.gastar_energia(10)


class Bruno(Madrigal):
    def usar_don(self):
        print(f"🔮 {self.nombre} ve el futuro... pero ¡no hablamos de Bruno!")
        self.gastar_energia(30)


# PUNTO 5: personaje nuevo. Solo hereda de Madrigal y escribe su usar_don().
# Fíjate que NO hubo que tocar nada dentro de la clase Casita.
class AbuelaAlma(Madrigal):
    def usar_don(self):
        print(f"🕯️ {self.nombre} protege a la familia y cuida la vela milagrosa.")
        self.gastar_energia(10)


# PUNTO 8: este NO hereda de Madrigal, pero también tiene usar_don().
# Python no revisa de qué clase viene el objeto, solo si sabe hacer lo que le
# pedimos. A eso se le llama "duck typing": si camina como pato y hace cuac,
# para Python es un pato.
class Visitante:
    def __init__(self, nombre):
        self.nombre = nombre

    def usar_don(self):
        print(f"🧳 {self.nombre} no es de la familia, pero trae café de regalo.")

    def esta_cansado(self):
        """El visitante no tiene energía, así que nunca está cansado."""
        return False

    def __str__(self):
        return f"{self.nombre} (visitante, sin don mágico)"


# ---------------------------------------------------------------
# COMPOSICIÓN: la Casita "tiene" una lista de Madrigal
# ---------------------------------------------------------------
class Casita:
    def __init__(self):
        self.habitantes = []

    def dar_bienvenida(self, madrigal):
        self.habitantes.append(madrigal)
        print(f"🏠 La Casita le da la bienvenida a {madrigal.nombre}.")

    def mostrar_familia(self):
        print("\n👨‍👩‍👧‍👦 FAMILIA MADRIGAL:")
        for madrigal in self.habitantes:
            print("  •", madrigal)  # usa __str__

    def dia_de_milagros(self):
        """Polimorfismo: llamamos usar_don() en todos sin importar su clase."""
        print("\n✨ ¡Comienza el día de los milagros! ✨")
        for madrigal in self.habitantes:
            # PUNTO 7: al que ya está cansado lo saltamos y lo mandamos a dormir.
            # Usamos hasattr() por si llega alguien que no tenga ese método,
            # como un Visitante hecho por otra persona.
            if hasattr(madrigal, "esta_cansado") and madrigal.esta_cansado():
                print(f"🛏️ {madrigal.nombre} está muy cansado hoy, necesita descansar.")
                continue
            madrigal.usar_don()


# ---------------------------------------------------------------
# PUNTO 10: menú para que el usuario elija quién usa su don
# ---------------------------------------------------------------
def mostrar_personajes(habitantes):
    """Imprime la lista numerada de quién vive en la Casita."""
    print("\n--- ¿A quién quieres ver usar su don? ---")
    for numero, habitante in enumerate(habitantes, start=1):
        print(f"{numero}. {habitante}")
    print("0. Salir")


def menu_dones(casita):
    """Menú con input(): el usuario elige un personaje y usa su don.

    Se repite hasta que el usuario escribe 0. Después de cada don muestra
    cómo le bajó la energía a ese personaje.
    """
    while True:
        mostrar_personajes(casita.habitantes)
        opcion = input("Elige un número: ").strip()

        # Validamos que haya escrito algo y que sea un número.
        if not opcion.isdigit():
            print("⚠️ Escribe solo el número de la lista.")
            continue

        opcion = int(opcion)

        if opcion == 0:
            print("👋 ¡Gracias por visitar la Casita Madrigal!")
            break

        # Validamos que el número exista en la lista.
        if opcion < 1 or opcion > len(casita.habitantes):
            print("⚠️ Ese número no está en la lista, intenta otra vez.")
            continue

        elegido = casita.habitantes[opcion - 1]
        # El visitante no tiene energía, por eso usamos getattr con None.
        energia_antes = getattr(elegido, "energia", None)

        print()
        elegido.usar_don()

        if energia_antes is None:
            print(f"   {elegido.nombre} no gasta energía.")
        else:
            print(f"   Energía de {elegido.nombre}: {energia_antes}% → {elegido.energia}%")
            if elegido.esta_cansado():
                print(f"   🛏️ {elegido.nombre} ya está cansado, debería descansar.")


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
if __name__ == "__main__":
    casita = Casita()

    familia = [
        Mirabel("Mirabel", 15),
        Isabela("Isabela", 21),
        Luisa("Luisa", 19),
        Julieta("Julieta", 50),
        Pepa("Pepa", 48, estado_de_animo="enojada"),
        Dolores("Dolores", 22),
        Camilo("Camilo", 17),
        Antonio("Antonio", 5),
        Bruno("Bruno", 52),
        AbuelaAlma("Abuela Alma", 75),   # PUNTO 5: el personaje nuevo
        Visitante("Mariano"),            # PUNTO 8: no es un Madrigal
    ]

    for persona in familia:
        casita.dar_bienvenida(persona)

    casita.mostrar_familia()

    # PUNTO 9: Antonio cumple años y recibe su don en la ceremonia.
    print()
    antonio = familia[7]
    antonio.cumplir_anios()
    antonio.ceremonia("hablar con los animales")

    casita.dia_de_milagros()

    # Hacemos que Bruno y Pepa trabajen de más para que se note el punto 7
    # (cansancio) y el punto 9 (el ánimo de Pepa).
    print("\n🔁 Bruno y Pepa usan su don varias veces...")
    bruno = familia[8]
    pepa = familia[4]
    for _ in range(2):
        bruno.usar_don()
        pepa.usar_don()

    # PUNTO 7: en este segundo día, a Bruno ya lo saltamos por cansancio.
    casita.dia_de_milagros()
    casita.mostrar_familia()

    print()
    bruno.descansar()
    print(bruno)

    # PUNTO 10: al final dejamos jugar al usuario.
    menu_dones(casita)


# ===================================================================
# RESPUESTAS A LAS PREGUNTAS (puntos 1 al 4)
# ===================================================================
#
# 1. ¿Qué pasaría si quitas @abstractmethod y creas un Madrigal("Alguien", 30)?
#
#    Lo probé de las dos formas:
#    - CON @abstractmethod, Python no deja crear el objeto y marca:
#        TypeError: Can't instantiate abstract class Madrigal without an
#        implementation for abstract method 'usar_don'
#    - SIN @abstractmethod sí se puede crear, pero ese "Madrigal suelto" se
#      queda con el usar_don() que no hace nada (solo pass), así que en
#      dia_de_milagros() pasaría de largo sin mostrar ningún don.
#    Es útil porque el error sale de inmediato, al crear el objeto, y no más
#    tarde cuando el programa ya está corriendo. @abstractmethod obliga a que
#    cada personaje nuevo escriba su propio don: funciona como un contrato.
#
# 2. En Casita.dia_de_milagros() solo se escribe madrigal.usar_don().
#    ¿Por qué no necesitamos un if para cada personaje?
#
#    Por el polimorfismo. Todos los personajes heredan de Madrigal y todos
#    tienen un método que se llama igual, usar_don(), aunque por dentro cada
#    uno haga algo distinto. Python revisa en el momento de ejecutar de qué
#    clase es el objeto y llama la versión que le toca. Por eso la Casita no
#    necesita saber quién es quién, y por eso agregar a la Abuela Alma
#    (punto 5) no me obligó a cambiar ni una línea de Casita.
#
# 3. ¿Por qué la energía es __energia y no simplemente energia?
#
#    Los dos guiones bajos activan el "name mangling": por dentro Python le
#    cambia el nombre a _Madrigal__energia para que no se modifique por
#    accidente desde afuera. Lo probé:
#    - familia[0].energia = 500 marca:
#        AttributeError: property 'energia' of 'Mirabel' object has no setter
#      porque energia es una @property de solo lectura.
#    - familia[0].__energia = 500 NO da error, pero tampoco sirve: crea un
#      atributo nuevo y aparte llamado __energia, y al imprimir la energía
#      sigue saliendo 100, porque el valor de verdad vive en
#      _Madrigal__energia.
#    O sea: la energía solo se puede cambiar con gastar_energia() y
#    descansar(), que son los métodos que yo controlo. Eso es encapsulamiento.
#
# 4. Si quisieras que todos los Madrigal tuvieran una "casa" (habitación),
#    ¿en qué clase lo agregarías y por qué?
#
#    En la clase base Madrigal, dentro de __init__ (algo como
#    self.habitacion = habitacion). Si lo pongo ahí, los nueve personajes lo
#    heredan de una vez y no tengo que repetir el mismo código en cada clase
#    hija; si después cambio cómo funciona la habitación, lo cambio en un solo
#    lugar. Solo lo pondría en una clase hija si fuera algo de un personaje en
#    particular, como los animales de Antonio o las gafas de Mirabel.
