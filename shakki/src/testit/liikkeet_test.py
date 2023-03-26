import unittest
import pygame
from pelilauta import Pelilauta
from alustaja import Alustaja

lauta = [[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

ruudun_koko = 125

class TestLiikkeet(unittest.TestCase):

    def setUp(self):
        korkeus_ja_leveys = 8
        nayton_korkeus_ja_leveys = 8*ruudun_koko

    def test_valkoisten_liikkeet_oikein(self):
        pelilauta = Pelilauta(lauta, ruudun_koko, Alustaja(ruudun_koko))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_valkoinen()
        tiedetyt_liikkeet = []
        for sotilas in pelilauta.valkoiset_sotilaat:
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / ruudun_koko), 5)))
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / ruudun_koko), 4)))
        for ratsu in pelilauta.valkoiset_ratsut:
            tiedetyt_liikkeet.append((ratsu, (int(ratsu.rect.x / ruudun_koko) + 1, int(ratsu.rect.y / ruudun_koko) - 2)))
            tiedetyt_liikkeet.append((ratsu, (int(ratsu.rect.x / ruudun_koko) - 1, int(ratsu.rect.y / ruudun_koko) - 2)))
        self.assertCountEqual(tiedetyt_liikkeet, mahdolliset_liikkeet)
    
    def test_mustien_liikkeet_oikein(self):
        pelilauta = Pelilauta(lauta, ruudun_koko, Alustaja(ruudun_koko))
        mahdolliset_liikkeet = pelilauta.tarkista_liikkeet_musta()
        tiedetyt_liikkeet = []
        for sotilas in pelilauta.mustat_sotilaat:
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / ruudun_koko), 2)))
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / ruudun_koko), 3)))
        for ratsu in pelilauta.mustat_ratsut:
            tiedetyt_liikkeet.append((ratsu, (int(ratsu.rect.x / ruudun_koko) + 1, int(ratsu.rect.y / ruudun_koko) + 2)))
            tiedetyt_liikkeet.append((ratsu, (int(ratsu.rect.x / ruudun_koko) - 1, int(ratsu.rect.y / ruudun_koko) + 2)))
        self.assertCountEqual(tiedetyt_liikkeet, mahdolliset_liikkeet)

    