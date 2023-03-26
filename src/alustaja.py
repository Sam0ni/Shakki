import pygame
from spritet.sotilas import Sotilas
from spritet.torni import Torni
from spritet.ratsu import Ratsu
from spritet.lahetti import Lahetti

class Alustaja:
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

        """Luo nappulat ja asettaa ne omille paikoilleen laudalle
        """
    def alusta_spritet(self, lauta):
        """Luo nappulat ja asettaa ne omille paikoilleen laudalle

        Args:
            lauta: 2-ulotteinen taulukko johon asetetaan nappulat

        Returns:
            List: sisältää spritejen ryhmät
        """
        for i in range(8):
            uusi_sotilas = Sotilas(i * self.ruudun_koko, 6 * self.ruudun_koko, True)
            self.valkoiset_sotilaat.add(uusi_sotilas)
            lauta[6][i] = uusi_sotilas
        uusi_torni = Torni(0 * self.ruudun_koko, 7 * self.ruudun_koko, True)
        self.valkoiset_tornit.add(uusi_torni)
        lauta[7][0] = uusi_torni
        uusi_torni = Torni(7 * self.ruudun_koko, 7 * self.ruudun_koko, True)
        self.valkoiset_tornit.add(uusi_torni)
        lauta[7][7] = uusi_torni
        uusi_ratsu = Ratsu(1 * self.ruudun_koko, 7 * self.ruudun_koko, True)
        self.valkoiset_ratsut.add(uusi_ratsu)
        lauta[7][1] = uusi_ratsu
        uusi_ratsu = Ratsu(6 * self.ruudun_koko, 7 * self.ruudun_koko, True)
        self.valkoiset_ratsut.add(uusi_ratsu)
        lauta[7][6] = uusi_ratsu
        uusi_lahetti = Lahetti(2 * self.ruudun_koko, 7 * self.ruudun_koko, True)
        self.valkoiset_lahetit.add(uusi_lahetti)
        lauta[7][2] = uusi_lahetti
        uusi_lahetti = Lahetti(5 * self.ruudun_koko, 7 * self.ruudun_koko, True)
        self.valkoiset_lahetit.add(uusi_lahetti)
        lauta[7][5] = uusi_lahetti

        for i in range(8):
            uusi_sotilas = Sotilas(i * self.ruudun_koko, 1 * self.ruudun_koko, False)
            self.mustat_sotilaat.add(uusi_sotilas)
            lauta[1][i] = uusi_sotilas
        uusi_torni = Torni(0 * self.ruudun_koko, 0, False)
        self.mustat_tornit.add(uusi_torni)
        lauta[0][0] = uusi_torni
        uusi_torni = Torni(7 * self.ruudun_koko, 0, False)
        self.mustat_tornit.add(uusi_torni)
        lauta[0][7] = uusi_torni
        uusi_ratsu = Ratsu(1 * self.ruudun_koko, 0, False)
        self.mustat_ratsut.add(uusi_ratsu)
        lauta[0][1] = uusi_ratsu
        uusi_ratsu = Ratsu(6 * self.ruudun_koko, 0, False)
        self.mustat_ratsut.add(uusi_ratsu)
        lauta[0][6] = uusi_ratsu
        uusi_lahetti = Lahetti(2 * self.ruudun_koko, 0, False)
        self.mustat_lahetit.add(uusi_lahetti)
        lauta[0][2] = uusi_lahetti
        uusi_lahetti = Lahetti(5 * self.ruudun_koko, 0, False)
        self.mustat_lahetit.add(uusi_lahetti)
        lauta[0][5] = uusi_lahetti

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