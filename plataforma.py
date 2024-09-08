import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill((255, 255, 255))  # Blanco
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
