import pygame

class Syotteiden_hakija:
    """Hakee käyttäjän syötteet
    """
    def hae(self):
        return pygame.event.get()