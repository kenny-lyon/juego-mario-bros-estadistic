import pygame

class Nivel:
    def __init__(self, pantalla, jugador):
        self.pantalla = pantalla
        self.jugador = jugador
        self.plataformas = pygame.sprite.Group()  # Grupo de plataformas
        self.enemigos = pygame.sprite.Group()     # Grupo de enemigos
        self.terminado = False                    # Indica si el nivel está completado

    def agregar_plataforma(self, plataforma):
        self.plataformas.add(plataforma)

    def agregar_enemigo(self, enemigo):
        self.enemigos.add(enemigo)

    def actualizar(self):
        # Actualiza las posiciones de los objetos y maneja la lógica del nivel
        self.plataformas.update()
        self.enemigos.update()
        self.jugador.update()

        # Verifica colisiones con plataformas
        if pygame.sprite.spritecollide(self.jugador, self.plataformas, False):
            self.jugador.saltar = False

        # Verifica si el jugador ha llegado al final del nivel
        if self.jugador.rect.x >= self.pantalla.get_width() - 50:
            self.terminado = True

    def dibujar(self):
        # Dibuja todos los objetos en la pantalla
        self.pantalla.fill((0, 0, 0))  # Fondo negro
        self.plataformas.draw(self.pantalla)
        self.enemigos.draw(self.pantalla)
        self.pantalla.blit(self.jugador.image, self.jugador.rect)
