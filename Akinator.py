import random

class Nodo:
    def __init__(self, pregunta, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no

class PersonajeMarioBros:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = {}

# Lista de personajes de Mario Bros con características aleatorias
personajes_mario_bros = [
    PersonajeMarioBros("Bowser"),
    PersonajeMarioBros("Wario"),
    PersonajeMarioBros("Waluigi"),
    PersonajeMarioBros("Shy Guy"),
    PersonajeMarioBros("Rey Boo"),
    PersonajeMarioBros("Huesitos"),
    PersonajeMarioBros("Koopalings"),
    PersonajeMarioBros("Bowser Jr"),
    PersonajeMarioBros("Bob-omb"),
    PersonajeMarioBros("Goomba")
]

# Preguntas comunes para todos los personajes
preguntas_comunes = [
    "cola",
    "bigote",
    "gorra",
    "mascara",
    "fantasma",
    "huesos",
    "caparazon",
    "panal",
    "bomba",
    "seta"
]

# Agregar las preguntas comunes a cada personaje con respuestas aleatorias
for personaje in personajes_mario_bros:
    for pregunta in preguntas_comunes:
        respuesta = random.choice(['s', 'n'])
        personaje.preguntas[pregunta] = respuesta

# Función para jugar al Akinator
def jugar_akinator(arbol):
    actual = arbol
    while True:
        respuesta = input(actual.pregunta + " (s/n): ").lower()
        if respuesta == 's':
            if actual.si is None:
                print("He adivinado el personaje!")
                return actual.personaje.nombre
            else:
                actual = actual.si
        elif respuesta == 'n':
            if actual.no is None:
                nuevo_personaje = input("No conozco ese personaje! En quien estabas pensando? ")
                nueva_pregunta = input("Escribe una pregunta para distinguir entre {} y {}: ".format(actual.pregunta, nuevo_personaje))
                respuesta_nueva = input("Para {} la respuesta seria (s/n): ".format(nuevo_personaje))
                if respuesta_nueva == 's':
                    actual.si = Nodo(nueva_pregunta, si=Nodo(nuevo_personaje))
                    actual.no = Nodo(actual.pregunta, si=Nodo(actual.personaje.nombre))
                else:
                    actual.si = Nodo(actual.pregunta, si=Nodo(actual.personaje.nombre))
                    actual.no = Nodo(nueva_pregunta, si=Nodo(nuevo_personaje))
                print("Gracias por ensenarme algo nuevo!")
                break
            else:
                actual = actual.no
        else:
            print("Por favor, responde 's' o 'n'.")

# Función para agregar un nuevo personaje
def agregar_personaje(arbol):
    nombre_personaje = input("Ingresa el nombre del nuevo personaje: ")
    nuevo_personaje = PersonajeMarioBros(nombre_personaje)
    for pregunta in preguntas_comunes:
        respuesta = input("{} es {}? (s/n): ".format(pregunta, nombre_personaje)).lower()
        nuevo_personaje.preguntas[pregunta] = respuesta
    nueva_pregunta_extra = input("Escribe una pregunta adicional sobre {}: ".format(nombre_personaje))
    respuesta_extra = input("{}? (s/n): ".format(nueva_pregunta_extra)).lower()
    if respuesta_extra == 's':
        arbol.si = Nodo(nueva_pregunta_extra, si=Nodo(nombre_personaje))
        arbol.no = Nodo(arbol.pregunta, si=Nodo(arbol.personaje.nombre))
    else:
        arbol.si = Nodo(arbol.pregunta, si=Nodo(arbol.personaje.nombre))
        arbol.no = Nodo(nueva_pregunta_extra, si=Nodo(nombre_personaje))
    print("Gracias por ensenarme algo nuevo!")

# Crear el árbol de preguntas y respuestas
arbol = Nodo("Es un personaje de Mario Bros?")

# Construir el árbol con los personajes de Mario Bros
arbol.personaje = None
for personaje in personajes_mario_bros:
    arbol.personaje = personaje
    arbol.si = Nodo(preguntas_comunes[0], si=Nodo(personaje.nombre))
    nodo_actual = arbol.si
    for pregunta in preguntas_comunes[1:]:
        nodo_actual.si = Nodo(pregunta, si=Nodo(personaje.nombre))
        nodo_actual = nodo_actual.si

# Menú principal
while True:
    print("\n=== MENU ===")
    print("1. Jugar")
    print("2. Agregar personaje")
    print("3. Salir")
    opcion = input("Selecciona una opcion: ")

    if opcion == '1':
        print("Piensa en un personaje de Mario Bros.")
        personaje_adivinado = jugar_akinator(arbol)
        print("El personaje es:", personaje_adivinado)
    elif opcion == '2':
        agregar_personaje(arbol)
    elif opcion == '3':
        print("Gracias por jugar!")
        break
    else:
        print("Opcion no valida. Por favor, selecciona una opcion del menu.")
