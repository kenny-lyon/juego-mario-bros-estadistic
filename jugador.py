import pygame
from utils import cargar_imagen

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar las imágenes del jugador
        self.imagen_idle = cargar_imagen("pngegg (2).png")
        #self.imagen_run1 = cargar_imagen("jugador/jugador_run1.png")
        #self.imagen_run2 = cargar_imagen("jugador/jugador_run2.png")
        
        # Inicializar con la imagen idle
        self.image = self.imagen_idle
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
        self.vel_x = 0
        self.vel_y = 0
        self.saltar = False
        self.contador_pasos = 0  # Para la animación
        
    def manejar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.vel_x = -5
                if evento.key == pygame.K_RIGHT:
                    self.vel_x = 5
                if evento.key == pygame.K_SPACE:
                    if not self.saltar:
                        self.vel_y = -10
                        self.saltar = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and self.vel_x < 0:
                    self.vel_x = 0
                if evento.key == pygame.K_RIGHT and self.vel_x > 0:
                    self.vel_x = 0
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Gravedad
        if self.saltar:
            self.vel_y += 1
        if self.rect.y >= 300:
            self.rect.y = 300
            self.saltar = False
            self.vel_y = 0

        # Animación simple
        if self.vel_x != 0:
            self.contador_pasos += 1
            if self.contador_pasos < 10:
                self.image = self.imagen_run1
            elif self.contador_pasos < 20:
                self.image = self.imagen_run2
            else:
                self.contador_pasos = 0
        else:
            self.image = self.imagen_idle
