import unittest
from pelilauta import Pelilauta


class TestLahetti(unittest.TestCase):

    def setUp(self):
        self.ruudun_koko = 125
        self.maxDiff = None
    
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)
