import pygame
import os

hakemisto = os.path.dirname(__file__)

class Sotilas(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, valkoinen=True):
        super().__init__()
        self.valkoinen = valkoinen
        self.liikutettu = False

        if self.valkoinen:
            vari = "valkoinen_sotilas.png"
        else:
            vari = "musta_sotilas.png"

        self.image = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit", vari)
        )

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

