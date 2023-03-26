import unittest
import pygame
from pelilauta import Pelilauta
from alustaja import Alustaja
from testi_alustajat.alustaja1 import Alustajatesti1
from testi_alustajat.alustaja2 import Alustajatesti2


class TestLiikkeet(unittest.TestCase):

    def setUp(self):
        self.lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

        self.ruudun_koko = 125

    def test_valkoisten_liikkeet_oikein(self):
        pelilauta = Pelilauta(self.lauta, self.ruudun_koko, Alustaja(self.ruudun_koko))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_valkoinen()
        tiedetyt_liikkeet = []
        print(mahdolliset_liikkeet)
        for sotilas in pelilauta.valkoiset_sotilaat:
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), 5)))
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), 4)))
        for ratsu in pelilauta.valkoiset_ratsut:
            tiedetyt_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko) + 1, int(ratsu.rect.y / self.ruudun_koko) - 2)))
            tiedetyt_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko) - 1, int(ratsu.rect.y / self.ruudun_koko) - 2)))
        self.assertCountEqual(tiedetyt_liikkeet, mahdolliset_liikkeet)
    
    def test_mustien_liikkeet_oikein(self):
        pelilauta = Pelilauta(self.lauta, self.ruudun_koko, Alustaja(self.ruudun_koko))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        tiedetyt_liikkeet = []
        for sotilas in pelilauta.mustat_sotilaat:
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), 2)))
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), 3)))
        for ratsu in pelilauta.mustat_ratsut:
            tiedetyt_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko) + 1, int(ratsu.rect.y / self.ruudun_koko) + 2)))
            tiedetyt_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko) - 1, int(ratsu.rect.y / self.ruudun_koko) + 2)))
        self.assertCountEqual(tiedetyt_liikkeet, mahdolliset_liikkeet)

    def test_sotilas_toimii_oikein_1(self):
        pelilauta = Pelilauta(self.lauta, self.ruudun_koko, Alustajatesti1(self.ruudun_koko))
        tiedetyt_liikkeet_valkoinen = []
        tiedetyt_liikkeet_musta = []
        for sotilas in pelilauta.valkoiset_sotilaat:
            sotilas.liikutettu = True
            tiedetyt_liikkeet_valkoinen.append((sotilas, (4, 5)))
            tiedetyt_liikkeet_valkoinen.append((sotilas, (5, 5)))
        for sotilas in pelilauta.mustat_sotilaat:
            sotilas.liikutettu = True
            tiedetyt_liikkeet_musta.append((sotilas, (5, 6)))
            tiedetyt_liikkeet_musta.append((sotilas, (4, 6)))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_valkoinen()
        print(mahdolliset_liikkeet)
        self.assertCountEqual(tiedetyt_liikkeet_valkoinen, mahdolliset_liikkeet)
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        print(mahdolliset_liikkeet)
        self.assertCountEqual(tiedetyt_liikkeet_musta, mahdolliset_liikkeet)

    def test_sotilas_toimii_oikein_2(self):
        pelilauta = Pelilauta(self.lauta, self.ruudun_koko, Alustajatesti2(self.ruudun_koko))
        tiedetyt_liikkeet_valkoinen = []
        tiedetyt_liikkeet_musta = []
        for sotilas in pelilauta.valkoiset_sotilaat:
            tiedetyt_liikkeet_valkoinen.append((sotilas, (4, 5)))
            tiedetyt_liikkeet_valkoinen.append((sotilas, (5, 5)))
        for ratsu in pelilauta.valkoiset_ratsut:
            tiedetyt_liikkeet_valkoinen.append((ratsu, (4, 6)))
            tiedetyt_liikkeet_valkoinen.append((ratsu, (6, 6)))
            tiedetyt_liikkeet_valkoinen.append((ratsu, (4, 2)))
            tiedetyt_liikkeet_valkoinen.append((ratsu, (6, 2)))
            tiedetyt_liikkeet_valkoinen.append((ratsu, (3, 3)))
            tiedetyt_liikkeet_valkoinen.append((ratsu, (3, 5)))
            tiedetyt_liikkeet_valkoinen.append((ratsu, (7, 5)))
            tiedetyt_liikkeet_valkoinen.append((ratsu, (7, 3)))
        for sotilas in pelilauta.mustat_sotilaat:
            tiedetyt_liikkeet_musta.append((sotilas, (5, 6)))
            tiedetyt_liikkeet_musta.append((sotilas, (4, 6)))
        for ratsu in pelilauta.mustat_ratsut:
            tiedetyt_liikkeet_musta.append((ratsu, (3, 5)))
            tiedetyt_liikkeet_musta.append((ratsu, (5, 5)))
            tiedetyt_liikkeet_musta.append((ratsu, (2, 6)))
            tiedetyt_liikkeet_musta.append((ratsu, (6, 6)))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_valkoinen()
        print(mahdolliset_liikkeet)
        self.assertCountEqual(tiedetyt_liikkeet_valkoinen, mahdolliset_liikkeet)
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        print(mahdolliset_liikkeet)
        self.assertCountEqual(tiedetyt_liikkeet_musta, mahdolliset_liikkeet)
