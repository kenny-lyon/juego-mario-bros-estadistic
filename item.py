import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 215, 0))  # Dorado
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
