import unittest
from pelilauta import Pelilauta


class TestKuningas(unittest.TestCase):

    def setUp(self):
        self.ruudun_koko = 125
        self.maxDiff = None

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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)
