import unittest
from pelilautarework import Pelilauta


class TestLiikkeet(unittest.TestCase):

    def setUp(self):
        self.ruudun_koko = 125
        self.maxDiff = None

    def test_sotilas_liikkeet_oikein_1(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,7,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,7,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((1, 6, 5), (1, 5, 5)),
            ((1, 6, 5), (1, 4, 5)),
            ((1, 6, 5), (1, 5, 6)),
            ((1, 2, 2), (1, 1, 2)),
            ((1, 2, 2), (1, 1, 1)),
            ((7, 1, 1), (7, 2, 1)),
            ((7, 1, 1), (7, 3, 1)),
            ((7, 1, 1), (7, 2, 2)),
            ((7, 5, 6), (7, 6, 6)),
            ((7, 5, 6), (7, 6, 5))
        ]
        tiedetyt_blokit = [
            ((7, 5, 6), (6, 7)),
            ((1, 6, 5), (5, 4)),
            ((1, 2, 2), (1, 3)),
            ((7, 1, 1), (2, 0))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_sotilas_liikkeet_oikein_2(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,7],
        [7,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((1, 6, 0), (1, 5, 0)),
            ((1, 5, 7), (1, 4, 7)),
            ((7, 1, 0), (7, 2, 0)),
            ((7, 2, 7), (7, 3, 7))
        ]
        tiedetyt_blokit = [
            ((7, 1, 0), (3, 0)),
            ((1, 6, 0), (4, 0)),
            ((1, 5, 7), (4, 6)),
            ((7, 2, 7), (3, 6)),
            ((7, 1, 0), (2, 1)),
            ((7, 3, 0), (4, 1)),
            ((1, 6, 0), (5, 1)),
            ((1, 4, 0), (3, 1)),
            ((7, 3, 0), (4, 0)),
            ((1, 4, 0), (3, 0))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_torni_liikkeet_oikein_1(self):
        lauta = [[8,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [2,0,0,0,0,0,0,8]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((2, 0, 7), (2, 1, 7)),
            ((2, 0, 7), (2, 2, 7)),
            ((2, 0, 7), (2, 3, 7)),
            ((2, 0, 7), (2, 4, 7)),
            ((2, 0, 7), (2, 5, 7)),
            ((2, 0, 7), (2, 6, 7)),
            ((2, 0, 7), (2, 7, 7)),
            ((2, 0, 7), (2, 0, 6)),
            ((2, 0, 7), (2, 0, 5)),
            ((2, 0, 7), (2, 0, 4)),
            ((2, 0, 7), (2, 0, 3)),
            ((2, 0, 7), (2, 0, 2)),
            ((2, 0, 7), (2, 0, 1)),
            ((2, 0, 7), (2, 0, 0)),
            ((2, 7, 0), (2, 7, 1)),
            ((2, 7, 0), (2, 7, 2)),
            ((2, 7, 0), (2, 7, 3)),
            ((2, 7, 0), (2, 7, 4)),
            ((2, 7, 0), (2, 7, 5)),
            ((2, 7, 0), (2, 7, 6)),
            ((2, 7, 0), (2, 7, 7)),
            ((2, 7, 0), (2, 6, 0)),
            ((2, 7, 0), (2, 5, 0)),
            ((2, 7, 0), (2, 4, 0)),
            ((2, 7, 0), (2, 3, 0)),
            ((2, 7, 0), (2, 2, 0)),
            ((2, 7, 0), (2, 1, 0)),
            ((2, 7, 0), (2, 0, 0)),
            ((8, 0, 0), (8, 0, 1)),
            ((8, 0, 0), (8, 0, 2)),
            ((8, 0, 0), (8, 0, 3)),
            ((8, 0, 0), (8, 0, 4)),
            ((8, 0, 0), (8, 0, 5)),
            ((8, 0, 0), (8, 0, 6)),
            ((8, 0, 0), (8, 0, 7)),
            ((8, 0, 0), (8, 1, 0)),
            ((8, 0, 0), (8, 2, 0)),
            ((8, 0, 0), (8, 3, 0)),
            ((8, 0, 0), (8, 4, 0)),
            ((8, 0, 0), (8, 5, 0)),
            ((8, 0, 0), (8, 6, 0)),
            ((8, 0, 0), (8, 7, 0)),
            ((8, 7, 7), (8, 7, 6)),
            ((8, 7, 7), (8, 7, 5)),
            ((8, 7, 7), (8, 7, 4)),
            ((8, 7, 7), (8, 7, 3)),
            ((8, 7, 7), (8, 7, 2)),
            ((8, 7, 7), (8, 7, 1)),
            ((8, 7, 7), (8, 7, 0)),
            ((8, 7, 7), (8, 6, 7)),
            ((8, 7, 7), (8, 5, 7)),
            ((8, 7, 7), (8, 4, 7)),
            ((8, 7, 7), (8, 3, 7)),
            ((8, 7, 7), (8, 2, 7)),
            ((8, 7, 7), (8, 1, 7)),
            ((8, 7, 7), (8, 0, 7)),
        ]
        tiedetyt_blokit = [
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_torni_liikkeet_oikein_2(self):
        lauta = [[2,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [2,0,0,0,0,0,0,2]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((2, 0, 7), (2, 1, 7)),
            ((2, 0, 7), (2, 2, 7)),
            ((2, 0, 7), (2, 3, 7)),
            ((2, 0, 7), (2, 4, 7)),
            ((2, 0, 7), (2, 5, 7)),
            ((2, 0, 7), (2, 6, 7)),
            ((2, 0, 7), (2, 0, 6)),
            ((2, 0, 7), (2, 0, 5)),
            ((2, 0, 7), (2, 0, 4)),
            ((2, 0, 7), (2, 0, 3)),
            ((2, 0, 7), (2, 0, 2)),
            ((2, 0, 7), (2, 0, 1)),
            ((2, 7, 0), (2, 7, 1)),
            ((2, 7, 0), (2, 7, 2)),
            ((2, 7, 0), (2, 7, 3)),
            ((2, 7, 0), (2, 7, 4)),
            ((2, 7, 0), (2, 7, 5)),
            ((2, 7, 0), (2, 7, 6)),
            ((2, 7, 0), (2, 6, 0)),
            ((2, 7, 0), (2, 5, 0)),
            ((2, 7, 0), (2, 4, 0)),
            ((2, 7, 0), (2, 3, 0)),
            ((2, 7, 0), (2, 2, 0)),
            ((2, 7, 0), (2, 1, 0)),
            ((2, 0, 0), (2, 0, 1)),
            ((2, 0, 0), (2, 0, 2)),
            ((2, 0, 0), (2, 0, 3)),
            ((2, 0, 0), (2, 0, 4)),
            ((2, 0, 0), (2, 0, 5)),
            ((2, 0, 0), (2, 0, 6)),
            ((2, 0, 0), (2, 1, 0)),
            ((2, 0, 0), (2, 2, 0)),
            ((2, 0, 0), (2, 3, 0)),
            ((2, 0, 0), (2, 4, 0)),
            ((2, 0, 0), (2, 5, 0)),
            ((2, 0, 0), (2, 6, 0)),
            ((2, 7, 7), (2, 7, 6)),
            ((2, 7, 7), (2, 7, 5)),
            ((2, 7, 7), (2, 7, 4)),
            ((2, 7, 7), (2, 7, 3)),
            ((2, 7, 7), (2, 7, 2)),
            ((2, 7, 7), (2, 7, 1)),
            ((2, 7, 7), (2, 6, 7)),
            ((2, 7, 7), (2, 5, 7)),
            ((2, 7, 7), (2, 4, 7)),
            ((2, 7, 7), (2, 3, 7)),
            ((2, 7, 7), (2, 2, 7)),
            ((2, 7, 7), (2, 1, 7)),
        ]
        tiedetyt_blokit = [
            ((2, 0, 7), (7, 7)),
            ((2, 0, 7), (0, 0)),
            ((2, 7, 0), (7, 7)),
            ((2, 7, 0), (0, 0)),
            ((2, 0, 0), (0, 7)),
            ((2, 0, 0), (7, 0)),
            ((2, 7, 7), (7, 0)),
            ((2, 7, 7), (0, 7))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_torni_liikkeet_oikein_3(self):
        lauta = [[8,0,0,0,0,0,0,8],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [8,0,0,0,0,0,0,8]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((8, 0, 7), (8, 1, 7)),
            ((8, 0, 7), (8, 2, 7)),
            ((8, 0, 7), (8, 3, 7)),
            ((8, 0, 7), (8, 4, 7)),
            ((8, 0, 7), (8, 5, 7)),
            ((8, 0, 7), (8, 6, 7)),
            ((8, 0, 7), (8, 0, 6)),
            ((8, 0, 7), (8, 0, 5)),
            ((8, 0, 7), (8, 0, 4)),
            ((8, 0, 7), (8, 0, 3)),
            ((8, 0, 7), (8, 0, 2)),
            ((8, 0, 7), (8, 0, 1)),
            ((8, 7, 0), (8, 7, 1)),
            ((8, 7, 0), (8, 7, 2)),
            ((8, 7, 0), (8, 7, 3)),
            ((8, 7, 0), (8, 7, 4)),
            ((8, 7, 0), (8, 7, 5)),
            ((8, 7, 0), (8, 7, 6)),
            ((8, 7, 0), (8, 6, 0)),
            ((8, 7, 0), (8, 5, 0)),
            ((8, 7, 0), (8, 4, 0)),
            ((8, 7, 0), (8, 3, 0)),
            ((8, 7, 0), (8, 2, 0)),
            ((8, 7, 0), (8, 1, 0)),
            ((8, 0, 0), (8, 0, 1)),
            ((8, 0, 0), (8, 0, 2)),
            ((8, 0, 0), (8, 0, 3)),
            ((8, 0, 0), (8, 0, 4)),
            ((8, 0, 0), (8, 0, 5)),
            ((8, 0, 0), (8, 0, 6)),
            ((8, 0, 0), (8, 1, 0)),
            ((8, 0, 0), (8, 2, 0)),
            ((8, 0, 0), (8, 3, 0)),
            ((8, 0, 0), (8, 4, 0)),
            ((8, 0, 0), (8, 5, 0)),
            ((8, 0, 0), (8, 6, 0)),
            ((8, 7, 7), (8, 7, 6)),
            ((8, 7, 7), (8, 7, 5)),
            ((8, 7, 7), (8, 7, 4)),
            ((8, 7, 7), (8, 7, 3)),
            ((8, 7, 7), (8, 7, 2)),
            ((8, 7, 7), (8, 7, 1)),
            ((8, 7, 7), (8, 6, 7)),
            ((8, 7, 7), (8, 5, 7)),
            ((8, 7, 7), (8, 4, 7)),
            ((8, 7, 7), (8, 3, 7)),
            ((8, 7, 7), (8, 2, 7)),
            ((8, 7, 7), (8, 1, 7)),
        ]
        tiedetyt_blokit = [
            ((8, 0, 7), (7, 7)),
            ((8, 0, 7), (0, 0)),
            ((8, 7, 0), (7, 7)),
            ((8, 7, 0), (0, 0)),
            ((8, 0, 0), (0, 7)),
            ((8, 0, 0), (7, 0)),
            ((8, 7, 7), (7, 0)),
            ((8, 7, 7), (0, 7))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_lahetti_liikkeet_oikein_1(self):
        lauta = [[10,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [4,0,0,0,0,0,0,10]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((4, 0, 7), (4, 1, 6)),
            ((4, 0, 7), (4, 2, 5)),
            ((4, 0, 7), (4, 3, 4)),
            ((4, 0, 7), (4, 4, 3)),
            ((4, 0, 7), (4, 5, 2)),
            ((4, 0, 7), (4, 6, 1)),
            ((4, 7, 0), (4, 6, 1)),
            ((4, 7, 0), (4, 5, 2)),
            ((4, 7, 0), (4, 4, 3)),
            ((4, 7, 0), (4, 3, 4)),
            ((4, 7, 0), (4, 2, 5)),
            ((4, 7, 0), (4, 1, 6)),
            ((10, 0, 0), (10, 1, 1)),
            ((10, 0, 0), (10, 2, 2)),
            ((10, 0, 0), (10, 3, 3)),
            ((10, 0, 0), (10, 4, 4)),
            ((10, 0, 0), (10, 5, 5)),
            ((10, 0, 0), (10, 6, 6)),
            ((10, 7, 7), (10, 6, 6)),
            ((10, 7, 7), (10, 5, 5)),
            ((10, 7, 7), (10, 4, 4)),
            ((10, 7, 7), (10, 3, 3)),
            ((10, 7, 7), (10, 2, 2)),
            ((10, 7, 7), (10, 1, 1))
        ]
        tiedetyt_blokit = [
            ((10, 7, 7), (0, 0)),
            ((10, 0, 0), (7, 7)),
            ((4, 0, 7), (7, 0)),
            ((4, 7, 0), (0, 7))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_lahetti_liikkeet_oikein_2(self):
        lauta = [[4,0,0,0,0,0,0,10],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [10,0,0,0,0,0,0,4]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((10, 0, 7), (10, 1, 6)),
            ((10, 0, 7), (10, 2, 5)),
            ((10, 0, 7), (10, 3, 4)),
            ((10, 0, 7), (10, 4, 3)),
            ((10, 0, 7), (10, 5, 2)),
            ((10, 0, 7), (10, 6, 1)),
            ((10, 7, 0), (10, 6, 1)),
            ((10, 7, 0), (10, 5, 2)),
            ((10, 7, 0), (10, 4, 3)),
            ((10, 7, 0), (10, 3, 4)),
            ((10, 7, 0), (10, 2, 5)),
            ((10, 7, 0), (10, 1, 6)),
            ((4, 0, 0), (4, 1, 1)),
            ((4, 0, 0), (4, 2, 2)),
            ((4, 0, 0), (4, 3, 3)),
            ((4, 0, 0), (4, 4, 4)),
            ((4, 0, 0), (4, 5, 5)),
            ((4, 0, 0), (4, 6, 6)),
            ((4, 7, 7), (4, 6, 6)),
            ((4, 7, 7), (4, 5, 5)),
            ((4, 7, 7), (4, 4, 4)),
            ((4, 7, 7), (4, 3, 3)),
            ((4, 7, 7), (4, 2, 2)),
            ((4, 7, 7), (4, 1, 1))
        ]
        tiedetyt_blokit = [
            ((4, 7, 7), (0, 0)),
            ((4, 0, 0), (7, 7)),
            ((10, 0, 7), (7, 0)),
            ((10, 7, 0), (0, 7))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_lahetti_liikkeet_oikein_3(self):
        lauta = [[4,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [10,0,0,0,0,0,0,10]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((4, 0, 7), (4, 1, 6)),
            ((4, 0, 7), (4, 2, 5)),
            ((4, 0, 7), (4, 3, 4)),
            ((4, 0, 7), (4, 4, 3)),
            ((4, 0, 7), (4, 5, 2)),
            ((4, 0, 7), (4, 6, 1)),
            ((4, 0, 7), (4, 7, 0)),
            ((10, 7, 0), (10, 6, 1)),
            ((10, 7, 0), (10, 5, 2)),
            ((10, 7, 0), (10, 4, 3)),
            ((10, 7, 0), (10, 3, 4)),
            ((10, 7, 0), (10, 2, 5)),
            ((10, 7, 0), (10, 1, 6)),
            ((10, 7, 0), (10, 0, 7)),
            ((4, 0, 0), (4, 1, 1)),
            ((4, 0, 0), (4, 2, 2)),
            ((4, 0, 0), (4, 3, 3)),
            ((4, 0, 0), (4, 4, 4)),
            ((4, 0, 0), (4, 5, 5)),
            ((4, 0, 0), (4, 6, 6)),
            ((4, 0, 0), (4, 7, 7)),
            ((10, 7, 7), (10, 6, 6)),
            ((10, 7, 7), (10, 5, 5)),
            ((10, 7, 7), (10, 4, 4)),
            ((10, 7, 7), (10, 3, 3)),
            ((10, 7, 7), (10, 2, 2)),
            ((10, 7, 7), (10, 1, 1)),
            ((10, 7, 7), (10, 0, 0))
        ]
        tiedetyt_blokit = [
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_lahetti_liikkeet_oikein_4(self):
        lauta = [[10,0,0,0,0,0,0,10],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [4,0,0,0,0,0,0,4]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((10, 0, 7), (10, 1, 6)),
            ((10, 0, 7), (10, 2, 5)),
            ((10, 0, 7), (10, 3, 4)),
            ((10, 0, 7), (10, 4, 3)),
            ((10, 0, 7), (10, 5, 2)),
            ((10, 0, 7), (10, 6, 1)),
            ((10, 0, 7), (10, 7, 0)),
            ((4, 7, 0), (4, 6, 1)),
            ((4, 7, 0), (4, 5, 2)),
            ((4, 7, 0), (4, 4, 3)),
            ((4, 7, 0), (4, 3, 4)),
            ((4, 7, 0), (4, 2, 5)),
            ((4, 7, 0), (4, 1, 6)),
            ((4, 7, 0), (4, 0, 7)),
            ((10, 0, 0), (10, 1, 1)),
            ((10, 0, 0), (10, 2, 2)),
            ((10, 0, 0), (10, 3, 3)),
            ((10, 0, 0), (10, 4, 4)),
            ((10, 0, 0), (10, 5, 5)),
            ((10, 0, 0), (10, 6, 6)),
            ((10, 0, 0), (10, 7, 7)),
            ((4, 7, 7), (4, 6, 6)),
            ((4, 7, 7), (4, 5, 5)),
            ((4, 7, 7), (4, 4, 4)),
            ((4, 7, 7), (4, 3, 3)),
            ((4, 7, 7), (4, 2, 2)),
            ((4, 7, 7), (4, 1, 1)),
            ((4, 7, 7), (4, 0, 0))
        ]
        tiedetyt_blokit = [
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_ratsu_liikkeet_oikein_1(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,1,0,1,0,0],
        [0,0,1,0,0,0,1,0],
        [0,0,0,0,3,0,0,0],
        [0,0,1,0,0,0,1,0],
        [0,0,0,1,0,1,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((1, 1, 3), (1, 0, 3)),
            ((1, 1, 5), (1, 0, 5)),
            ((1, 2, 2), (1, 1, 2)),
            ((1, 2, 6), (1, 1, 6)),
            ((1, 4, 2), (1, 3, 2)),
            ((1, 4, 6), (1, 3, 6)),
            ((1, 5, 3), (1, 4, 3)),
            ((1, 5, 5), (1, 4, 5))
        ]
        tiedetyt_blokit = [
            ((3, 3, 4), (1, 3)),
            ((3, 3, 4), (1, 5)),
            ((3, 3, 4), (2, 2)),
            ((3, 3, 4), (2, 6)),
            ((3, 3, 4), (4, 2)),
            ((3, 3, 4), (4, 6)),
            ((3, 3, 4), (5, 3)),
            ((3, 3, 4), (5, 5)),
            ((1, 1, 3), (0, 4)),
            ((1, 1, 3), (0, 2)),
            ((1, 1, 5), (0, 4)),
            ((1, 1, 5), (0, 6)),
            ((1, 2, 2), (1, 3)),
            ((1, 2, 2), (1, 1)),
            ((1, 2, 6), (1, 5)),
            ((1, 2, 6), (1, 7)),
            ((1, 4, 2), (3, 3)),
            ((1, 4, 2), (3, 1)),
            ((1, 4, 6), (3, 5)),
            ((1, 4, 6), (3, 7)),
            ((1, 5, 3), (4, 4)),
            ((1, 5, 3), (4, 2)),
            ((1, 5, 5), (4, 4)),
            ((1, 5, 5), (4, 6))

        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_ratsu_liikkeet_oikein_2(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,7,0,7,0,0],
        [0,0,7,0,0,0,7,0],
        [0,0,0,0,3,0,0,0],
        [0,0,7,0,0,0,7,0],
        [0,0,0,7,0,7,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((7, 1, 3), (7, 3, 3)),
            ((7, 1, 5), (7, 3, 5)),
            ((7, 1, 3), (7, 2, 3)),
            ((7, 1, 5), (7, 2, 5)),
            ((7, 2, 2), (7, 3, 2)),
            ((7, 2, 6), (7, 3, 6)),
            ((7, 4, 2), (7, 5, 2)),
            ((7, 4, 6), (7, 5, 6)),
            ((7, 5, 3), (7, 6, 3)),
            ((7, 5, 5), (7, 6, 5)),
            ((3, 3, 4), (3, 1, 3)),
            ((3, 3, 4), (3, 1, 5)),
            ((3, 3, 4), (3, 2, 2)),
            ((3, 3, 4), (3, 2, 6)),
            ((3, 3, 4), (3, 4, 2)),
            ((3, 3, 4), (3, 4, 6)),
            ((3, 3, 4), (3, 5, 3)),
            ((3, 3, 4), (3, 5, 5)),
        ]
        tiedetyt_blokit = [
            ((7, 1, 3), (2, 4)),
            ((7, 1, 3), (2, 2)),
            ((7, 1, 5), (2, 4)),
            ((7, 1, 5), (2, 6)),
            ((7, 2, 2), (3, 3)),
            ((7, 2, 2), (3, 1)),
            ((7, 2, 6), (3, 5)),
            ((7, 2, 6), (3, 7)),
            ((7, 4, 2), (5, 3)),
            ((7, 4, 2), (5, 1)),
            ((7, 4, 6), (5, 5)),
            ((7, 4, 6), (5, 7)),
            ((7, 5, 3), (6, 4)),
            ((7, 5, 3), (6, 2)),
            ((7, 5, 5), (6, 4)),
            ((7, 5, 5), (6, 6))

        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_ratsu_liikkeet_oikein_3(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,7,0,7,0,0],
        [0,0,7,0,0,0,7,0],
        [0,0,0,0,9,0,0,0],
        [0,0,7,0,0,0,7,0],
        [0,0,0,7,0,7,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((7, 1, 3), (7, 3, 3)),
            ((7, 1, 5), (7, 3, 5)),
            ((7, 1, 3), (7, 2, 3)),
            ((7, 1, 5), (7, 2, 5)),
            ((7, 2, 2), (7, 3, 2)),
            ((7, 2, 6), (7, 3, 6)),
            ((7, 4, 2), (7, 5, 2)),
            ((7, 4, 6), (7, 5, 6)),
            ((7, 5, 3), (7, 6, 3)),
            ((7, 5, 5), (7, 6, 5)),
        ]
        tiedetyt_blokit = [
            ((7, 1, 3), (2, 4)),
            ((7, 1, 3), (2, 2)),
            ((7, 1, 5), (2, 4)),
            ((7, 1, 5), (2, 6)),
            ((7, 2, 2), (3, 3)),
            ((7, 2, 2), (3, 1)),
            ((7, 2, 6), (3, 5)),
            ((7, 2, 6), (3, 7)),
            ((7, 4, 2), (5, 3)),
            ((7, 4, 2), (5, 1)),
            ((7, 4, 6), (5, 5)),
            ((7, 4, 6), (5, 7)),
            ((7, 5, 3), (6, 4)),
            ((7, 5, 3), (6, 2)),
            ((7, 5, 5), (6, 4)),
            ((7, 5, 5), (6, 6)),
            ((9, 3, 4), (1, 3)),
            ((9, 3, 4), (1, 5)),
            ((9, 3, 4), (2, 2)),
            ((9, 3, 4), (2, 6)),
            ((9, 3, 4), (4, 2)),
            ((9, 3, 4), (4, 6)),
            ((9, 3, 4), (5, 3)),
            ((9, 3, 4), (5, 5))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_ratsu_liikkeet_oikein_4(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,1,0,1,0,0],
        [0,0,1,0,0,0,1,0],
        [0,0,0,0,9,0,0,0],
        [0,0,1,0,0,0,1,0],
        [0,0,0,1,0,1,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((1, 1, 3), (1, 0, 3)),
            ((1, 1, 5), (1, 0, 5)),
            ((1, 2, 2), (1, 1, 2)),
            ((1, 2, 6), (1, 1, 6)),
            ((1, 4, 2), (1, 3, 2)),
            ((1, 4, 6), (1, 3, 6)),
            ((1, 5, 3), (1, 4, 3)),
            ((1, 5, 5), (1, 4, 5)),
            ((9, 3, 4), (9, 1, 3)),
            ((9, 3, 4), (9, 1, 5)),
            ((9, 3, 4), (9, 2, 2)),
            ((9, 3, 4), (9, 2, 6)),
            ((9, 3, 4), (9, 4, 2)),
            ((9, 3, 4), (9, 4, 6)),
            ((9, 3, 4), (9, 5, 3)),
            ((9, 3, 4), (9, 5, 5))
        ]
        tiedetyt_blokit = [
            ((1, 1, 3), (0, 4)),
            ((1, 1, 3), (0, 2)),
            ((1, 1, 5), (0, 4)),
            ((1, 1, 5), (0, 6)),
            ((1, 2, 2), (1, 3)),
            ((1, 2, 2), (1, 1)),
            ((1, 2, 6), (1, 5)),
            ((1, 2, 6), (1, 7)),
            ((1, 4, 2), (3, 3)),
            ((1, 4, 2), (3, 1)),
            ((1, 4, 6), (3, 5)),
            ((1, 4, 6), (3, 7)),
            ((1, 5, 3), (4, 4)),
            ((1, 5, 3), (4, 2)),
            ((1, 5, 5), (4, 4)),
            ((1, 5, 5), (4, 6))

        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_ratsu_liikkeet_oikein_5(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,3,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((3, 3, 4), (3, 1, 3)),
            ((3, 3, 4), (3, 1, 5)),
            ((3, 3, 4), (3, 2, 2)),
            ((3, 3, 4), (3, 2, 6)),
            ((3, 3, 4), (3, 4, 2)),
            ((3, 3, 4), (3, 4, 6)),
            ((3, 3, 4), (3, 5, 3)),
            ((3, 3, 4), (3, 5, 5)),
        ]
        tiedetyt_blokit = [
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_ratsu_liikkeet_oikein_6(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,9,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((9, 3, 4), (9, 1, 3)),
            ((9, 3, 4), (9, 1, 5)),
            ((9, 3, 4), (9, 2, 2)),
            ((9, 3, 4), (9, 2, 6)),
            ((9, 3, 4), (9, 4, 2)),
            ((9, 3, 4), (9, 4, 6)),
            ((9, 3, 4), (9, 5, 3)),
            ((9, 3, 4), (9, 5, 5))
        ]
        tiedetyt_blokit = [
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_ratsu_liikkeet_oikein_7(self):
        lauta = [[3,0,0,0,0,0,0,3],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [3,0,0,0,0,0,0,3]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((3, 0, 0), (3, 1, 2)),
            ((3, 0, 0), (3, 2, 1)),
            ((3, 0, 7), (3, 1, 5)),
            ((3, 0, 7), (3, 2, 6)),
            ((3, 7, 0), (3, 5, 1)),
            ((3, 7, 0), (3, 6, 2)),
            ((3, 7, 7), (3, 5, 6)),
            ((3, 7, 7), (3, 6, 5))
        ]
        tiedetyt_blokit = [
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_ratsu_liikkeet_oikein_8(self):
        lauta = [[9,0,0,0,0,0,0,9],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [9,0,0,0,0,0,0,9]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((9, 0, 0), (9, 1, 2)),
            ((9, 0, 0), (9, 2, 1)),
            ((9, 0, 7), (9, 1, 5)),
            ((9, 0, 7), (9, 2, 6)),
            ((9, 7, 0), (9, 5, 1)),
            ((9, 7, 0), (9, 6, 2)),
            ((9, 7, 7), (9, 5, 6)),
            ((9, 7, 7), (9, 6, 5))
        ]
        tiedetyt_blokit = [
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_kuningatar_liikkeet_oikein_1(self):
        lauta = [[5,0,0,0,0,0,0,5],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [5,0,0,0,0,0,0,5]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((5, 0, 7), (5, 1, 6)),
            ((5, 0, 7), (5, 2, 5)),
            ((5, 0, 7), (5, 3, 4)),
            ((5, 0, 7), (5, 4, 3)),
            ((5, 0, 7), (5, 5, 2)),
            ((5, 0, 7), (5, 6, 1)),
            ((5, 7, 0), (5, 6, 1)),
            ((5, 7, 0), (5, 5, 2)),
            ((5, 7, 0), (5, 4, 3)),
            ((5, 7, 0), (5, 3, 4)),
            ((5, 7, 0), (5, 2, 5)),
            ((5, 7, 0), (5, 1, 6)),
            ((5, 0, 0), (5, 1, 1)),
            ((5, 0, 0), (5, 2, 2)),
            ((5, 0, 0), (5, 3, 3)),
            ((5, 0, 0), (5, 4, 4)),
            ((5, 0, 0), (5, 5, 5)),
            ((5, 0, 0), (5, 6, 6)),
            ((5, 7, 7), (5, 6, 6)),
            ((5, 7, 7), (5, 5, 5)),
            ((5, 7, 7), (5, 4, 4)),
            ((5, 7, 7), (5, 3, 3)),
            ((5, 7, 7), (5, 2, 2)),
            ((5, 7, 7), (5, 1, 1)),
            ((5, 0, 7), (5, 1, 7)),
            ((5, 0, 7), (5, 2, 7)),
            ((5, 0, 7), (5, 3, 7)),
            ((5, 0, 7), (5, 4, 7)),
            ((5, 0, 7), (5, 5, 7)),
            ((5, 0, 7), (5, 6, 7)),
            ((5, 0, 7), (5, 0, 6)),
            ((5, 0, 7), (5, 0, 5)),
            ((5, 0, 7), (5, 0, 4)),
            ((5, 0, 7), (5, 0, 3)),
            ((5, 0, 7), (5, 0, 2)),
            ((5, 0, 7), (5, 0, 1)),
            ((5, 7, 0), (5, 7, 1)),
            ((5, 7, 0), (5, 7, 2)),
            ((5, 7, 0), (5, 7, 3)),
            ((5, 7, 0), (5, 7, 4)),
            ((5, 7, 0), (5, 7, 5)),
            ((5, 7, 0), (5, 7, 6)),
            ((5, 7, 0), (5, 6, 0)),
            ((5, 7, 0), (5, 5, 0)),
            ((5, 7, 0), (5, 4, 0)),
            ((5, 7, 0), (5, 3, 0)),
            ((5, 7, 0), (5, 2, 0)),
            ((5, 7, 0), (5, 1, 0)),
            ((5, 0, 0), (5, 0, 1)),
            ((5, 0, 0), (5, 0, 2)),
            ((5, 0, 0), (5, 0, 3)),
            ((5, 0, 0), (5, 0, 4)),
            ((5, 0, 0), (5, 0, 5)),
            ((5, 0, 0), (5, 0, 6)),
            ((5, 0, 0), (5, 1, 0)),
            ((5, 0, 0), (5, 2, 0)),
            ((5, 0, 0), (5, 3, 0)),
            ((5, 0, 0), (5, 4, 0)),
            ((5, 0, 0), (5, 5, 0)),
            ((5, 0, 0), (5, 6, 0)),
            ((5, 7, 7), (5, 7, 6)),
            ((5, 7, 7), (5, 7, 5)),
            ((5, 7, 7), (5, 7, 4)),
            ((5, 7, 7), (5, 7, 3)),
            ((5, 7, 7), (5, 7, 2)),
            ((5, 7, 7), (5, 7, 1)),
            ((5, 7, 7), (5, 6, 7)),
            ((5, 7, 7), (5, 5, 7)),
            ((5, 7, 7), (5, 4, 7)),
            ((5, 7, 7), (5, 3, 7)),
            ((5, 7, 7), (5, 2, 7)),
            ((5, 7, 7), (5, 1, 7)),
        ]
        tiedetyt_blokit = [
            ((5, 7, 7), (0, 0)),
            ((5, 7, 7), (0, 7)),
            ((5, 7, 7), (7, 0)),
            ((5, 7, 0), (7, 7)),
            ((5, 7, 0), (0, 7)),
            ((5, 7, 0), (0, 0)),
            ((5, 0, 7), (0, 0)),
            ((5, 0, 7), (7, 7)),
            ((5, 0, 7), (7, 0)),
            ((5, 0, 0), (7, 7)),
            ((5, 0, 0), (0, 7)),
            ((5, 0, 0), (7, 0)),
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_kuningatar_liikkeet_oikein_2(self):
        lauta = [[11,0,0,0,0,0,0,11],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [5,0,0,0,0,0,0,5]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((11, 0, 7), (11, 1, 6)),
            ((11, 0, 7), (11, 2, 5)),
            ((11, 0, 7), (11, 3, 4)),
            ((11, 0, 7), (11, 4, 3)),
            ((11, 0, 7), (11, 5, 2)),
            ((11, 0, 7), (11, 6, 1)),
            ((11, 0, 7), (11, 7, 0)),

            ((5, 7, 0), (5, 6, 1)),
            ((5, 7, 0), (5, 5, 2)),
            ((5, 7, 0), (5, 4, 3)),
            ((5, 7, 0), (5, 3, 4)),
            ((5, 7, 0), (5, 2, 5)),
            ((5, 7, 0), (5, 1, 6)),
            ((5, 7, 0), (5, 0, 7)),

            ((11, 0, 0), (11, 1, 1)),
            ((11, 0, 0), (11, 2, 2)),
            ((11, 0, 0), (11, 3, 3)),
            ((11, 0, 0), (11, 4, 4)),
            ((11, 0, 0), (11, 5, 5)),
            ((11, 0, 0), (11, 6, 6)),
            ((11, 0, 0), (11, 7, 7)),

            ((5, 7, 7), (5, 6, 6)),
            ((5, 7, 7), (5, 5, 5)),
            ((5, 7, 7), (5, 4, 4)),
            ((5, 7, 7), (5, 3, 3)),
            ((5, 7, 7), (5, 2, 2)),
            ((5, 7, 7), (5, 1, 1)),
            ((5, 7, 7), (5, 0, 0)),

            ((11, 0, 7), (11, 1, 7)),
            ((11, 0, 7), (11, 2, 7)),
            ((11, 0, 7), (11, 3, 7)),
            ((11, 0, 7), (11, 4, 7)),
            ((11, 0, 7), (11, 5, 7)),
            ((11, 0, 7), (11, 6, 7)),
            ((11, 0, 7), (11, 7, 7)),
            ((11, 0, 7), (11, 0, 6)),
            ((11, 0, 7), (11, 0, 5)),
            ((11, 0, 7), (11, 0, 4)),
            ((11, 0, 7), (11, 0, 3)),
            ((11, 0, 7), (11, 0, 2)),
            ((11, 0, 7), (11, 0, 1)),

            ((5, 7, 0), (5, 7, 1)),
            ((5, 7, 0), (5, 7, 2)),
            ((5, 7, 0), (5, 7, 3)),
            ((5, 7, 0), (5, 7, 4)),
            ((5, 7, 0), (5, 7, 5)),
            ((5, 7, 0), (5, 7, 6)),
            ((5, 7, 0), (5, 6, 0)),
            ((5, 7, 0), (5, 5, 0)),
            ((5, 7, 0), (5, 4, 0)),
            ((5, 7, 0), (5, 3, 0)),
            ((5, 7, 0), (5, 2, 0)),
            ((5, 7, 0), (5, 1, 0)),
            ((5, 7, 0), (5, 0, 0)),

            ((11, 0, 0), (11, 0, 1)),
            ((11, 0, 0), (11, 0, 2)),
            ((11, 0, 0), (11, 0, 3)),
            ((11, 0, 0), (11, 0, 4)),
            ((11, 0, 0), (11, 0, 5)),
            ((11, 0, 0), (11, 0, 6)),
            ((11, 0, 0), (11, 1, 0)),
            ((11, 0, 0), (11, 2, 0)),
            ((11, 0, 0), (11, 3, 0)),
            ((11, 0, 0), (11, 4, 0)),
            ((11, 0, 0), (11, 5, 0)),
            ((11, 0, 0), (11, 6, 0)),
            ((11, 0, 0), (11, 7, 0)),

            ((5, 7, 7), (5, 7, 6)),
            ((5, 7, 7), (5, 7, 5)),
            ((5, 7, 7), (5, 7, 4)),
            ((5, 7, 7), (5, 7, 3)),
            ((5, 7, 7), (5, 7, 2)),
            ((5, 7, 7), (5, 7, 1)),
            ((5, 7, 7), (5, 6, 7)),
            ((5, 7, 7), (5, 5, 7)),
            ((5, 7, 7), (5, 4, 7)),
            ((5, 7, 7), (5, 3, 7)),
            ((5, 7, 7), (5, 2, 7)),
            ((5, 7, 7), (5, 1, 7)),
            ((5, 7, 7), (5, 0, 7)),
        ]
        tiedetyt_blokit = [
            ((5, 7, 7), (7, 0)),
            ((5, 7, 0), (7, 7)),
            ((11, 0, 7), (0, 0)),
            ((11, 0, 0), (0, 7))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_kuningatar_liikkeet_oikein_3(self):
        lauta = [[5,0,0,0,0,0,0,5],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [11,0,0,0,0,0,0,11]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((5, 0, 7), (5, 1, 6)),
            ((5, 0, 7), (5, 2, 5)),
            ((5, 0, 7), (5, 3, 4)),
            ((5, 0, 7), (5, 4, 3)),
            ((5, 0, 7), (5, 5, 2)),
            ((5, 0, 7), (5, 6, 1)),
            ((5, 0, 7), (5, 7, 0)),

            ((11, 7, 0), (11, 6, 1)),
            ((11, 7, 0), (11, 5, 2)),
            ((11, 7, 0), (11, 4, 3)),
            ((11, 7, 0), (11, 3, 4)),
            ((11, 7, 0), (11, 2, 5)),
            ((11, 7, 0), (11, 1, 6)),
            ((11, 7, 0), (11, 0, 7)),

            ((5, 0, 0), (5, 1, 1)),
            ((5, 0, 0), (5, 2, 2)),
            ((5, 0, 0), (5, 3, 3)),
            ((5, 0, 0), (5, 4, 4)),
            ((5, 0, 0), (5, 5, 5)),
            ((5, 0, 0), (5, 6, 6)),
            ((5, 0, 0), (5, 7, 7)),

            ((11, 7, 7), (11, 6, 6)),
            ((11, 7, 7), (11, 5, 5)),
            ((11, 7, 7), (11, 4, 4)),
            ((11, 7, 7), (11, 3, 3)),
            ((11, 7, 7), (11, 2, 2)),
            ((11, 7, 7), (11, 1, 1)),
            ((11, 7, 7), (11, 0, 0)),

            ((5, 0, 7), (5, 1, 7)),
            ((5, 0, 7), (5, 2, 7)),
            ((5, 0, 7), (5, 3, 7)),
            ((5, 0, 7), (5, 4, 7)),
            ((5, 0, 7), (5, 5, 7)),
            ((5, 0, 7), (5, 6, 7)),
            ((5, 0, 7), (5, 7, 7)),
            ((5, 0, 7), (5, 0, 6)),
            ((5, 0, 7), (5, 0, 5)),
            ((5, 0, 7), (5, 0, 4)),
            ((5, 0, 7), (5, 0, 3)),
            ((5, 0, 7), (5, 0, 2)),
            ((5, 0, 7), (5, 0, 1)),

            ((11, 7, 0), (11, 7, 1)),
            ((11, 7, 0), (11, 7, 2)),
            ((11, 7, 0), (11, 7, 3)),
            ((11, 7, 0), (11, 7, 4)),
            ((11, 7, 0), (11, 7, 5)),
            ((11, 7, 0), (11, 7, 6)),
            ((11, 7, 0), (11, 6, 0)),
            ((11, 7, 0), (11, 5, 0)),
            ((11, 7, 0), (11, 4, 0)),
            ((11, 7, 0), (11, 3, 0)),
            ((11, 7, 0), (11, 2, 0)),
            ((11, 7, 0), (11, 1, 0)),
            ((11, 7, 0), (11, 0, 0)),

            ((5, 0, 0), (5, 0, 1)),
            ((5, 0, 0), (5, 0, 2)),
            ((5, 0, 0), (5, 0, 3)),
            ((5, 0, 0), (5, 0, 4)),
            ((5, 0, 0), (5, 0, 5)),
            ((5, 0, 0), (5, 0, 6)),
            ((5, 0, 0), (5, 1, 0)),
            ((5, 0, 0), (5, 2, 0)),
            ((5, 0, 0), (5, 3, 0)),
            ((5, 0, 0), (5, 4, 0)),
            ((5, 0, 0), (5, 5, 0)),
            ((5, 0, 0), (5, 6, 0)),
            ((5, 0, 0), (5, 7, 0)),

            ((11, 7, 7), (11, 7, 6)),
            ((11, 7, 7), (11, 7, 5)),
            ((11, 7, 7), (11, 7, 4)),
            ((11, 7, 7), (11, 7, 3)),
            ((11, 7, 7), (11, 7, 2)),
            ((11, 7, 7), (11, 7, 1)),
            ((11, 7, 7), (11, 6, 7)),
            ((11, 7, 7), (11, 5, 7)),
            ((11, 7, 7), (11, 4, 7)),
            ((11, 7, 7), (11, 3, 7)),
            ((11, 7, 7), (11, 2, 7)),
            ((11, 7, 7), (11, 1, 7)),
            ((11, 7, 7), (11, 0, 7)),
        ]
        tiedetyt_blokit = [
            ((11, 7, 7), (7, 0)),
            ((11, 7, 0), (7, 7)),
            ((5, 0, 7), (0, 0)),
            ((5, 0, 0), (0, 7))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    
    def test_kuningatar_liikkeet_oikein_4(self):
        lauta = [[11,0,0,0,0,0,0,5],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [5,0,0,0,0,0,0,11]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((5, 0, 7), (5, 1, 6)),
            ((5, 0, 7), (5, 2, 5)),
            ((5, 0, 7), (5, 3, 4)),
            ((5, 0, 7), (5, 4, 3)),
            ((5, 0, 7), (5, 5, 2)),
            ((5, 0, 7), (5, 6, 1)),
            ((5, 0, 7), (5, 0, 0)),

            ((5, 7, 0), (5, 6, 1)),
            ((5, 7, 0), (5, 5, 2)),
            ((5, 7, 0), (5, 4, 3)),
            ((5, 7, 0), (5, 3, 4)),
            ((5, 7, 0), (5, 2, 5)),
            ((5, 7, 0), (5, 1, 6)),
            ((5, 7, 0), (5, 7, 7)),

            ((11, 0, 0), (11, 1, 1)),
            ((11, 0, 0), (11, 2, 2)),
            ((11, 0, 0), (11, 3, 3)),
            ((11, 0, 0), (11, 4, 4)),
            ((11, 0, 0), (11, 5, 5)),
            ((11, 0, 0), (11, 6, 6)),
            ((11, 0, 0), (11, 7, 0)),

            ((11, 7, 7), (11, 6, 6)),
            ((11, 7, 7), (11, 5, 5)),
            ((11, 7, 7), (11, 4, 4)),
            ((11, 7, 7), (11, 3, 3)),
            ((11, 7, 7), (11, 2, 2)),
            ((11, 7, 7), (11, 1, 1)),
            ((11, 7, 7), (11, 7, 0)),

            ((5, 0, 7), (5, 1, 7)),
            ((5, 0, 7), (5, 2, 7)),
            ((5, 0, 7), (5, 3, 7)),
            ((5, 0, 7), (5, 4, 7)),
            ((5, 0, 7), (5, 5, 7)),
            ((5, 0, 7), (5, 6, 7)),
            ((5, 0, 7), (5, 7, 7)),
            ((5, 0, 7), (5, 0, 6)),
            ((5, 0, 7), (5, 0, 5)),
            ((5, 0, 7), (5, 0, 4)),
            ((5, 0, 7), (5, 0, 3)),
            ((5, 0, 7), (5, 0, 2)),
            ((5, 0, 7), (5, 0, 1)),

            ((5, 7, 0), (5, 7, 1)),
            ((5, 7, 0), (5, 7, 2)),
            ((5, 7, 0), (5, 7, 3)),
            ((5, 7, 0), (5, 7, 4)),
            ((5, 7, 0), (5, 7, 5)),
            ((5, 7, 0), (5, 7, 6)),
            ((5, 7, 0), (5, 6, 0)),
            ((5, 7, 0), (5, 5, 0)),
            ((5, 7, 0), (5, 4, 0)),
            ((5, 7, 0), (5, 3, 0)),
            ((5, 7, 0), (5, 2, 0)),
            ((5, 7, 0), (5, 1, 0)),
            ((5, 7, 0), (5, 0, 0)),

            ((11, 0, 0), (11, 0, 1)),
            ((11, 0, 0), (11, 0, 2)),
            ((11, 0, 0), (11, 0, 3)),
            ((11, 0, 0), (11, 0, 4)),
            ((11, 0, 0), (11, 0, 5)),
            ((11, 0, 0), (11, 0, 6)),
            ((11, 0, 0), (11, 1, 0)),
            ((11, 0, 0), (11, 2, 0)),
            ((11, 0, 0), (11, 3, 0)),
            ((11, 0, 0), (11, 4, 0)),
            ((11, 0, 0), (11, 5, 0)),
            ((11, 0, 0), (11, 6, 0)),
            ((11, 0, 0), (11, 0, 7)),

            ((11, 7, 7), (11, 7, 6)),
            ((11, 7, 7), (11, 7, 5)),
            ((11, 7, 7), (11, 7, 4)),
            ((11, 7, 7), (11, 7, 3)),
            ((11, 7, 7), (11, 7, 2)),
            ((11, 7, 7), (11, 7, 1)),
            ((11, 7, 7), (11, 6, 7)),
            ((11, 7, 7), (11, 5, 7)),
            ((11, 7, 7), (11, 4, 7)),
            ((11, 7, 7), (11, 3, 7)),
            ((11, 7, 7), (11, 2, 7)),
            ((11, 7, 7), (11, 1, 7)),
            ((11, 7, 7), (11, 0, 7)),
        ]
        tiedetyt_blokit = [
            ((11, 7, 7), (0, 0)),
            ((5, 7, 0), (0, 7)),
            ((5, 0, 7), (7, 0)),
            ((11, 0, 0), (7, 7))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_kuningas_liikkeet_oikein_1(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,0,1,6,1,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((1, 3, 2), (1, 2, 2)),
            ((1, 3, 3), (1, 2, 3)),
            ((1, 3, 4), (1, 2, 4))
        ]
        tiedetyt_blokit = [
            ((6, 4, 3), (4, 2)),
            ((6, 4, 3), (4, 4)),
            ((6, 4, 3), (3, 2)),
            ((6, 4, 3), (5, 2)),
            ((6, 4, 3), (3, 4)),
            ((6, 4, 3), (5, 4)),
            ((6, 4, 3), (3, 3)),
            ((6, 4, 3), (5, 3)),
            ((1, 3, 2), (2, 1)),
            ((1, 3, 2), (2, 3)),
            ((1, 3, 3), (2, 2)),
            ((1, 3, 3), (2, 4)),
            ((1, 3, 4), (2, 3)),
            ((1, 3, 4), (2, 5)),
            ((1, 4, 2), (3, 1)),
            ((1, 4, 2), (3, 2)),
            ((1, 4, 2), (3, 3)),
            ((1, 4, 4), (3, 5)),
            ((1, 4, 4), (3, 4)),
            ((1, 4, 4), (3, 3)),
            ((1, 5, 2), (4, 1)),
            ((1, 5, 2), (4, 2)),
            ((1, 5, 2), (4, 3)),
            ((1, 5, 3), (4, 2)),
            ((1, 5, 3), (4, 3)),
            ((1, 5, 3), (4, 4)),
            ((1, 5, 4), (4, 3)),
            ((1, 5, 4), (4, 4)),
            ((1, 5, 4), (4, 5))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_kuningas_liikkeet_oikein_2(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,7,7,7,0,0,0],
        [0,0,7,6,7,0,0,0],
        [0,0,7,7,7,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((7, 3, 2), (7, 4, 3)),
            ((7, 3, 4), (7, 4, 3)),
            ((7, 5, 2), (7, 6, 2)),
            ((7, 5, 3), (7, 6, 3)),
            ((7, 5, 4), (7, 6, 4)),
            ((6, 4, 3), (6, 5, 4)),
            ((6, 4, 3), (6, 5, 3)),
            ((6, 4, 3), (6, 5, 2)),
            ((6, 4, 3), (6, 4, 2)),
            ((6, 4, 3), (6, 4, 4)),
            ((6, 4, 3), (6, 3, 2)),
            ((6, 4, 3), (6, 3, 3)),
            ((6, 4, 3), (6, 3, 4))
        ]
        tiedetyt_blokit = [
            ((7, 3, 2), (4, 1)),
            ((7, 3, 2), (4, 2)),
            ((7, 3, 3), (4, 2)),
            ((7, 3, 3), (4, 4)),
            ((7, 3, 3), (4, 3)),
            ((7, 3, 4), (4, 5)),
            ((7, 3, 4), (4, 4)),
            ((7, 4, 2), (5, 1)),
            ((7, 4, 2), (5, 2)),
            ((7, 4, 2), (5, 3)),
            ((7, 4, 4), (5, 5)),
            ((7, 4, 4), (5, 4)),
            ((7, 4, 4), (5, 3)),
            ((7, 5, 2), (6, 1)),
            ((7, 5, 2), (6, 3)),
            ((7, 5, 3), (6, 2)),
            ((7, 5, 3), (6, 4)),
            ((7, 5, 4), (6, 3)),
            ((7, 5, 4), (6, 5))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_kuningas_liikkeet_oikein_3(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,0,1,12,1,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((1, 5, 2), (1, 4, 3)),
            ((1, 5, 4), (1, 4, 3)),
            ((1, 3, 2), (1, 2, 2)),
            ((1, 3, 3), (1, 2, 3)),
            ((1, 3, 4), (1, 2, 4)),
            ((12, 4, 3), (12, 5, 4)),
            ((12, 4, 3), (12, 5, 3)),
            ((12, 4, 3), (12, 5, 2)),
            ((12, 4, 3), (12, 4, 2)),
            ((12, 4, 3), (12, 4, 4)),
            ((12, 4, 3), (12, 3, 2)),
            ((12, 4, 3), (12, 3, 3)),
            ((12, 4, 3), (12, 3, 4))
        ]
        tiedetyt_blokit = [
            ((1, 5, 2), (4, 1)),
            ((1, 5, 2), (4, 2)),
            ((1, 5, 3), (4, 2)),
            ((1, 5, 3), (4, 4)),
            ((1, 5, 3), (4, 3)),
            ((1, 5, 4), (4, 5)),
            ((1, 5, 4), (4, 4)),
            ((1, 4, 2), (3, 1)),
            ((1, 4, 2), (3, 2)),
            ((1, 4, 2), (3, 3)),
            ((1, 4, 4), (3, 5)),
            ((1, 4, 4), (3, 4)),
            ((1, 4, 4), (3, 3)),
            ((1, 3, 2), (2, 1)),
            ((1, 3, 2), (2, 3)),
            ((1, 3, 3), (2, 2)),
            ((1, 3, 3), (2, 4)),
            ((1, 3, 4), (2, 3)),
            ((1, 3, 4), (2, 5))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_kuningas_liikkeet_oikein_4(self):
        lauta = [[12,0,0,0,0,0,0,12],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [12,0,0,0,0,0,0,12]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        tiedetyt_liikkeet = [
            ((12, 0, 0), (12, 0, 1)),
            ((12, 0, 0), (12, 1, 1)),
            ((12, 0, 0), (12, 1, 0)),
            ((12, 0, 7), (12, 0, 6)),
            ((12, 0, 7), (12, 1, 6)),
            ((12, 0, 7), (12, 1, 7)),
            ((12, 7, 0), (12, 6, 0)),
            ((12, 7, 0), (12, 6, 1)),
            ((12, 7, 0), (12, 7, 1)),
            ((12, 7, 7), (12, 6, 7)),
            ((12, 7, 7), (12, 6, 6)),
            ((12, 7, 7), (12, 7, 6))
        ]
        tiedetyt_blokit = [
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

    def test_liikkuminen_toimii(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,7,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        lauta_siirron_jalkeen = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

        tiedetyt_liikkeet = [
            ((1, 4, 3), (1, 3, 3))
        ]
        tiedetyt_blokit = [
            ((1, 4, 3), (3, 4)),
            ((1, 4, 3), (3, 2))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa

        mahdolliset_liikkeet, mahdolliset_blokit = pelilauta.liiku((1, 5, 4), (1, 4, 3), mahdolliset_liikkeet, mahdolliset_blokit)
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)
        self.assertEqual(lauta_siirron_jalkeen, pelilauta.lauta)
    
    def test_liikkeiden_paivitys_toimii(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,7,0,0,0],
        [2,0,0,0,7,0,0,0],
        [0,0,0,0,0,7,0,0],
        [0,0,0,0,2,0,0,0],
        [0,0,0,4,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)

        lauta_siirron_jalkeen = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,7,0,0,0],
        [2,0,0,0,2,0,0,0],
        [0,0,0,0,0,7,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,4,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

        tiedetyt_liikkeet = [
            ((2, 2, 0), (2, 2, 1)),
            ((2, 2, 0), (2, 2, 2)),
            ((2, 2, 0), (2, 2, 3)),
            ((2, 2, 0), (2, 3, 0)),
            ((2, 2, 0), (2, 4, 0)),
            ((2, 2, 0), (2, 5, 0)),
            ((2, 2, 0), (2, 6, 0)),
            ((2, 2, 0), (2, 7, 0)),
            ((2, 2, 0), (2, 1, 0)),
            ((2, 2, 0), (2, 0, 0)),
            ((7, 3, 5), (7, 4, 5)),
            ((4, 5, 3), (4, 4, 4)),
            ((4, 5, 3), (4, 3, 5)),
            ((4, 5, 3), (4, 6, 2)),
            ((4, 5, 3), (4, 7, 1)),
            ((4, 5, 3), (4, 6, 4)),
            ((4, 5, 3), (4, 7, 5)),
            ((4, 5, 3), (4, 4, 2)),
            ((4, 5, 3), (4, 3, 1)),
            ((2, 2, 4), (2, 2, 3)),
            ((2, 2, 4), (2, 2, 2)),
            ((2, 2, 4), (2, 2, 1)),
            ((2, 2, 4), (2, 2, 5)),
            ((2, 2, 4), (2, 2, 6)),
            ((2, 2, 4), (2, 2, 7)),
            ((2, 2, 4), (2, 3, 4)),
            ((2, 2, 4), (2, 4, 4)),
            ((2, 2, 4), (2, 5, 4)),
            ((2, 2, 4), (2, 6, 4)),
            ((2, 2, 4), (2, 7, 4)),
            ((2, 2, 4), (2, 1, 4)),
        ]
        tiedetyt_blokit = [
            ((2, 2, 0), (2, 4)),
            ((2, 2, 4), (2, 0)),
            ((7, 1, 4), (2, 4)),
            ((7, 1, 4), (2, 5)),
            ((7, 1, 4), (2, 3)),
            ((7, 3, 5), (4, 4)),
            ((7, 3, 5), (4, 6)),
            ((4, 5, 3), (2, 0))
        ]

        mahdolliset_liikkeet = []
        mahdolliset_blokit = []

        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = pelilauta.tarkista_liikkeet(pelilauta.lauta[y][x], y, x)
                mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
                mahdolliset_blokit = mahdolliset_blokit + uudet_edessa

        mahdolliset_liikkeet, mahdolliset_blokit = pelilauta.liiku((2, 4, 4), (2, 2, 4), mahdolliset_liikkeet, mahdolliset_blokit)
    
        mahdolliset_liikkeet, mahdolliset_blokit = pelilauta.paivita(mahdolliset_liikkeet, mahdolliset_blokit, (2, 4, 4), (2, 2, 4))
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

        self.assertEqual(lauta_siirron_jalkeen, pelilauta.lauta)