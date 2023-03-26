import pygame
from spritet.sotilas import Sotilas
from spritet.torni import Torni
from spritet.ratsu import Ratsu
from spritet.lahetti import Lahetti

class Alustajatesti2:
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
        uusi_sotilas = Sotilas(5 * self.ruudun_koko, 6 * self.ruudun_koko, True)
        self.valkoiset_sotilaat.add(uusi_sotilas)
        lauta[6][5] = uusi_sotilas

        uusi_sotilas = Sotilas(4 * self.ruudun_koko, 5 * self.ruudun_koko, False)
        self.mustat_sotilaat.add(uusi_sotilas)
        lauta[5][4] = uusi_sotilas

        uusi_ratsu = Ratsu((5 * self.ruudun_koko), (4 * self.ruudun_koko), True)
        self.valkoiset_ratsut.add(uusi_ratsu)
        lauta[4][5] = uusi_ratsu

        uusi_ratsu = Ratsu((4 * self.ruudun_koko), (7 * self.ruudun_koko), False)
        self.mustat_ratsut.add(uusi_ratsu)
        lauta[7][4] = uusi_ratsu

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