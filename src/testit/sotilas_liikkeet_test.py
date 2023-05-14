import unittest
from pelilauta import Pelilauta


class TestSotilas(unittest.TestCase):

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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)
