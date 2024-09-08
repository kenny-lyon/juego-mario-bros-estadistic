import random

class Preguntas:
    def __init__(self):
        self.preguntas = [
            {"pregunta": "¿Cuál es la media de los siguientes números: 2, 4, 6, 8?", "opciones": ["4", "5", "6", "7"], "respuesta": "5"},
            {"pregunta": "¿Qué es la desviación estándar?", "opciones": ["Medida de dispersión", "Media", "Moda", "Mediana"], "respuesta": "Medida de dispersión"},
            # Añade más preguntas aquí
        ]

    def obtener_pregunta(self):
        return random.choice(self.preguntas)

def mostrar_pregunta():
    preguntas = Preguntas()
    pregunta = preguntas.obtener_pregunta()
    print(pregunta["pregunta"])
    print("Opciones: ", pregunta["opciones"])
    # Aquí puedes agregar lógica para manejar la interacción del usuario y validar la respuesta
