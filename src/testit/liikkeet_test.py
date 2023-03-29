import unittest
import pygame
from pelilauta import Pelilauta
from alustaja import Alustaja
from testi_alustajat.alustaja1 import Alustajatesti1
from testi_alustajat.alustaja2 import Alustajatesti2
from testi_alustajat.alustaja3 import Alustajatesti3
from testi_alustajat.alustaja4 import Alustajatesti4
from testi_alustajat.alustaja5 import Alustajatesti5
from testi_alustajat.alustaja6 import Alustajatesti6


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
        self.assertCountEqual(tiedetyt_liikkeet_valkoinen, mahdolliset_liikkeet)
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        self.assertCountEqual(tiedetyt_liikkeet_musta, mahdolliset_liikkeet)

    def test_torni_toimii_oikein_1(self):
        pelilauta = Pelilauta(self.lauta, self.ruudun_koko, Alustajatesti3(self.ruudun_koko))
        tiedetyt_liikkeet_valkoinen = []
        tiedetyt_liikkeet_musta = []
        for sotilas in pelilauta.valkoiset_sotilaat:
            sotilas.liikutettu = True
            if int(sotilas.rect.y / self.ruudun_koko) == 7:
                continue
            tiedetyt_liikkeet_valkoinen.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko) - 1)))
        for sotilas in pelilauta.mustat_sotilaat:
            sotilas.liikutettu = True
            if int(sotilas.rect.y / self.ruudun_koko) == 0:
                continue
            tiedetyt_liikkeet_musta.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko) + 1)))
        for torni in pelilauta.valkoiset_tornit:
            tiedetyt_liikkeet_valkoinen.append((torni, (6, 2)))
            tiedetyt_liikkeet_valkoinen.append((torni, (6, 0)))
            tiedetyt_liikkeet_valkoinen.append((torni, (5, 1)))
            tiedetyt_liikkeet_valkoinen.append((torni, (7, 1)))
        for torni in pelilauta.mustat_tornit:
            tiedetyt_liikkeet_musta.append((torni, (0, 6)))
            tiedetyt_liikkeet_musta.append((torni, (2, 6)))
            tiedetyt_liikkeet_musta.append((torni, (1, 7)))
            tiedetyt_liikkeet_musta.append((torni, (1, 5)))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_valkoinen()
        self.assertCountEqual(tiedetyt_liikkeet_valkoinen, mahdolliset_liikkeet)
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        self.assertCountEqual(tiedetyt_liikkeet_musta, mahdolliset_liikkeet)

    def test_torni_toimii_oikein_2(self):
        pelilauta = Pelilauta(self.lauta, self.ruudun_koko, Alustajatesti4(self.ruudun_koko))
        tiedetyt_liikkeet_valkoinen = []
        tiedetyt_liikkeet_musta = []
        for sotilas in pelilauta.valkoiset_sotilaat:
            sotilas.liikutettu = True
            if int(sotilas.rect.y / self.ruudun_koko) == 7:
                continue
            tiedetyt_liikkeet_valkoinen.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko) - 1)))
        for sotilas in pelilauta.mustat_sotilaat:
            sotilas.liikutettu = True
            if int(sotilas.rect.y / self.ruudun_koko) == 0:
                continue
            tiedetyt_liikkeet_musta.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko) + 1)))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_valkoinen()
        self.assertCountEqual(tiedetyt_liikkeet_valkoinen, mahdolliset_liikkeet)
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        self.assertCountEqual(tiedetyt_liikkeet_musta, mahdolliset_liikkeet)

    def test_torni_toimii_oikein_3(self):
        pelilauta = Pelilauta(self.lauta, self.ruudun_koko, Alustajatesti5(self.ruudun_koko))
        tiedetyt_liikkeet_valkoinen = []
        tiedetyt_liikkeet_musta = []
        for torni in pelilauta.valkoiset_tornit:
            for i in range(int(torni.rect.x / self.ruudun_koko), 7):
                tiedetyt_liikkeet_valkoinen.append((torni, (i + 1, int(torni.rect.y / self.ruudun_koko))))
            for i in range(int(torni.rect.x / self.ruudun_koko), 0, -1):
                tiedetyt_liikkeet_valkoinen.append((torni, (i - 1, int(torni.rect.y / self.ruudun_koko))))
            for i in range(int(torni.rect.y / self.ruudun_koko), 7):
                tiedetyt_liikkeet_valkoinen.append((torni, (int(torni.rect.x / self.ruudun_koko), i + 1)))
            for i in range(int(torni.rect.y / self.ruudun_koko), 0, -1):
                tiedetyt_liikkeet_valkoinen.append((torni, (int(torni.rect.x / self.ruudun_koko), i - 1)))
        for torni in pelilauta.mustat_tornit:
            for i in range(int(torni.rect.x / self.ruudun_koko), 7):
                tiedetyt_liikkeet_musta.append((torni, (i + 1, int(torni.rect.y / self.ruudun_koko))))
            for i in range(int(torni.rect.x / self.ruudun_koko), 0, -1):
                tiedetyt_liikkeet_musta.append((torni, (i - 1, int(torni.rect.y / self.ruudun_koko))))
            for i in range(int(torni.rect.y / self.ruudun_koko), 7):
                tiedetyt_liikkeet_musta.append((torni, (int(torni.rect.x / self.ruudun_koko), i + 1)))
            for i in range(int(torni.rect.y / self.ruudun_koko), 0, -1):
                tiedetyt_liikkeet_musta.append((torni, (int(torni.rect.x / self.ruudun_koko), i - 1)))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_valkoinen()
        self.assertCountEqual(tiedetyt_liikkeet_valkoinen, mahdolliset_liikkeet)
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        self.assertCountEqual(tiedetyt_liikkeet_musta, mahdolliset_liikkeet)

    def test_ratsu_toimii_oikein(self):
        pelilauta = Pelilauta(self.lauta, self.ruudun_koko, Alustajatesti6(self.ruudun_koko))
        tiedetyt_liikkeet_valkoinen = []
        tiedetyt_liikkeet_musta = []
        for sotilas in pelilauta.valkoiset_sotilaat:
            sotilas.liikutettu = True
        for sotilas in pelilauta.mustat_sotilaat:
            sotilas.liikutettu = True
        nappula = pelilauta.lauta[5][6]
        tiedetyt_liikkeet_valkoinen.append((nappula, (6, 4)))
        nappula = pelilauta.lauta[6][5]
        tiedetyt_liikkeet_valkoinen.append((nappula, (5, 5)))
        nappula = pelilauta.lauta[1][2]
        tiedetyt_liikkeet_valkoinen.append((nappula, (2, 0)))
        nappula = pelilauta.lauta[2][1]
        tiedetyt_liikkeet_valkoinen.append((nappula, (1, 1)))
        nappula = pelilauta.lauta[5][1]
        tiedetyt_liikkeet_musta.append((nappula, (1, 6)))
        nappula = pelilauta.lauta[6][2]
        tiedetyt_liikkeet_musta.append((nappula, (2, 7)))
        nappula = pelilauta.lauta[1][5]
        tiedetyt_liikkeet_musta.append((nappula, (5, 2)))
        nappula = pelilauta.lauta[2][6]
        tiedetyt_liikkeet_musta.append((nappula, (6, 3)))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_valkoinen()
        self.assertCountEqual(tiedetyt_liikkeet_valkoinen, mahdolliset_liikkeet)
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        self.assertCountEqual(tiedetyt_liikkeet_musta, mahdolliset_liikkeet)