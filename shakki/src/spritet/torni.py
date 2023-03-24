import pygame
import os

hakemisto = os.path.dirname(__file__)

class Torni(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, valkoinen=True):
        super().__init__()
        self.valkoinen = valkoinen
        self.liikutettu = False

        if self.valkoinen:
            vari = "valkoinen_torni.png"
        else:
            vari = "musta_torni.png"

        self.image = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit", vari)
        )

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
