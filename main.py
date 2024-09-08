import pygame
from niveles.nivel_1 import Nivel1
#from niveles.nivel_2 import Nivel2
# Importa los demás niveles conforme los vayas creando

from jugador import Jugador

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mario Bros")
    reloj = pygame.time.Clock()

    # Inicial  iza el jugador
    jugador = Jugador()

    # Lista de niveles
    niveles = [Nivel1(pantalla, jugador), "Nivel2(pantalla, jugador)"]  # Añade más niveles aquí
    nivel_actual = 0

    corriendo = True
    while corriendo:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                corriendo = False

        # Actualiza y dibuja el nivel actual
        niveles[nivel_actual].actualizar()
        niveles[nivel_actual].dibujar()
        jugador.manejar_eventos(eventos)

        if niveles[nivel_actual].terminado:
            nivel_actual += 1
            if nivel_actual >= len(niveles):
                print("¡Juego completado!")
                corriendo = False

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
