import unittest
import pygame
from pelilauta import Pelilauta

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
        self.pelilauta = Pelilauta(lauta, ruudun_koko)

    def test_valkoisten_liikkeet_oikein(self):
        mahdolliset_liikkeet = self.pelilauta.tarkista_liikkeet_valkoinen()
        tiedetyt_liikkeet = []
        for sotilas in self.pelilauta.valkoiset_sotilaat:
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / ruudun_koko), 5)))
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / ruudun_koko), 4)))
        for torni in self.pelilauta.valkoiset_tornit:
            tiedetyt_liikkeet.append((torni, (1, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (2, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (3, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (4, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (5, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (6, int(torni.rect.y / ruudun_koko))))
        self.assertCountEqual(tiedetyt_liikkeet, mahdolliset_liikkeet)
    
    def test_mustien_liikkeet_oikein(self):
        mahdolliset_liikkeet = self.pelilauta.tarkista_liikkeet_musta()
        tiedetyt_liikkeet = []
        for sotilas in self.pelilauta.mustat_sotilaat:
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / ruudun_koko), 2)))
            tiedetyt_liikkeet.append((sotilas, (int(sotilas.rect.x / ruudun_koko), 3)))
        for torni in self.pelilauta.mustat_tornit:
            tiedetyt_liikkeet.append((torni, (1, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (2, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (3, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (4, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (5, int(torni.rect.y / ruudun_koko))))
            tiedetyt_liikkeet.append((torni, (6, int(torni.rect.y / ruudun_koko))))
        self.assertCountEqual(tiedetyt_liikkeet, mahdolliset_liikkeet)