import pygame

class Kello:
    """Kelloluokka, joka ajoittaa
    pelisilmukkaa
    """
    def __init__(self):
        self.kello = pygame.time.Clock()

    def tick(self, fps):
        self.kello.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()