import pygame
from spritet.sotilas import Sotilas
from spritet.torni import Torni
from spritet.ratsu import Ratsu
from spritet.lahetti import Lahetti

class Alustajatesti5:
    def __init__(self, ruudun_koko):
        self.ruudun_koko = ruudun_koko
        self.mustat_sotilaat = pygame.sprite.Group()
        self.mustat_tornit = pygame.sprite.Group()
        self.mustat_ratsut = pygame.sprite.Group()
        self.mustat_lahetit = pygame.sprite.Group()
        self.valkoiset_sotilaat = pygame.sprite.Group()
        self.valkoiset_tornit = pygame.sprite.Group()
        self.valkoiset_ratsut = pygame.sprite.Group()
        self.valkoiset_lahetit = pygame.sprite.Group()

    def alusta_spritet(self, lauta):
        uusi_torni = Torni(1 * self.ruudun_koko, 6 * self.ruudun_koko, True)
        self.valkoiset_tornit.add(uusi_torni)
        lauta[6][1] = uusi_torni

        uusi_torni = Torni(6 * self.ruudun_koko, 1 * self.ruudun_koko, False)
        self.mustat_tornit.add(uusi_torni)
        lauta[1][6] = uusi_torni

        return [
            self.mustat_sotilaat,
            self.mustat_tornit,
            self.mustat_ratsut,
            self.mustat_lahetit,
            self.valkoiset_sotilaat,
            self.valkoiset_tornit,
            self.valkoiset_ratsut,
            self.valkoiset_lahetit
        ]