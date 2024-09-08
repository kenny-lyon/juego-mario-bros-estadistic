from nivel import Nivel
from plataforma import Plataforma
from enemigo import Enemigo
from item import Item
import pygame

class BloqueDestructible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((139, 69, 19))  # Color marrón para el bloque
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = True

class Moneda(Item):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((255, 215, 0))  # Color dorado para la moneda
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Tubo(Plataforma):
    def __init__(self, x, y, alto):
        super().__init__(x, y, 80, alto)  # Un tubo ancho de 80 y altura variable
        self.image.fill((0, 255, 0))  # Color verde para el tubo

class Bandera(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 70))
        self.image.fill((255, 255, 255))  # Blanco para la bandera
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Nivel1(Nivel):
    def __init__(self, pantalla, jugador):
        super().__init__(pantalla, jugador)

        # Inicializar el grupo de items
        self.items = pygame.sprite.Group()

        # Crear plataformas
        suelo = Plataforma(0, 560, 800, 40)
        plataforma1 = Plataforma(200, 500, 200, 20)
        plataforma2 = Plataforma(500, 450, 150, 20)
        plataforma3 = Plataforma(700, 350, 200, 20)

        # Crear tubos
        tubo1 = Tubo(350, 460, 100)
        tubo2 = Tubo(600, 420, 140)

        # Crear bloques destructibles
        bloque1 = BloqueDestructible(220, 460)
        bloque2 = BloqueDestructible(260, 460)

        # Crear monedas
        moneda1 = Moneda(250, 400)
        moneda2 = Moneda(520, 400)

        # Crear enemigo patrullante
        enemigo1 = Enemigo(700, 320)

        # Crear bandera de fin de nivel
        bandera = Bandera(750, 280)

        # Agregar todos los elementos al nivel
        self.agregar_plataforma(suelo)
        self.agregar_plataforma(plataforma1)
        self.agregar_plataforma(plataforma2)
        self.agregar_plataforma(plataforma3)
        self.agregar_plataforma(tubo1)
        self.agregar_plataforma(tubo2)
        self.agregar_plataforma(bloque1)
        self.agregar_plataforma(bloque2)

        self.items.add(moneda1)
        self.items.add(moneda2)

        self.agregar_enemigo(enemigo1)
        self.bandera = bandera

    def actualizar(self):
        # Actualiza el estado del nivel
        super().actualizar()

        # Verifica colisión del jugador con los items (monedas)
        items_recogidos = pygame.sprite.spritecollide(self.jugador, self.items, True)
        for item in items_recogidos:
            print("¡Moneda recogida!")

        # Verifica si el jugador ha alcanzado la bandera (fin del nivel)
        if pygame.sprite.collide_rect(self.jugador, self.bandera):
            self.terminado = True

        # Verifica si el jugador ha golpeado bloques destructibles desde abajo
        bloques_golpeados = pygame.sprite.spritecollide(self.jugador, self.plataformas, False)
        for bloque in bloques_golpeados:
            if isinstance(bloque, BloqueDestructible) and self.jugador.vel_y < 0:
                bloque.kill()
                print("¡Bloque destruido!")

    def dibujar(self):
        # Dibuja el nivel
        super().dibujar()

        # Dibuja la bandera de fin de nivel
        self.pantalla.blit(self.bandera.image, self.bandera.rect)
        
        # Dibuja los items (monedas)
        self.items.draw(self.pantalla)
