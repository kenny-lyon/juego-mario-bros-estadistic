import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Verde
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 2

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.vel_x *= -1
