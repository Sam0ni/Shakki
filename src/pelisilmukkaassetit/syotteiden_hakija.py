import pygame

class SyotteidenHakija:
    """Hakee käyttäjän syötteet
    """
    def hae(self):
        return pygame.event.get()
