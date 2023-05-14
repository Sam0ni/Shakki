import unittest
from pelilauta import Pelilauta


class TestRatsu(unittest.TestCase):

    def setUp(self):
        self.ruudun_koko = 125
        self.maxDiff = None
    
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
            ((1, 1, 3), (2, 0, 3)),
            ((1, 1, 3), (3, 0, 3)),
            ((1, 1, 3), (4, 0, 3)),
            ((1, 1, 3), (5, 0, 3)),
            ((1, 1, 5), (2, 0, 5)),
            ((1, 1, 5), (3, 0, 5)),
            ((1, 1, 5), (4, 0, 5)),
            ((1, 1, 5), (5, 0, 5)),
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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
            ((3, 3, 4), (3, 5, 5))
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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
            ((1, 1, 3), (2, 0, 3)),
            ((1, 1, 3), (3, 0, 3)),
            ((1, 1, 3), (4, 0, 3)),
            ((1, 1, 3), (5, 0, 3)),
            ((1, 1, 5), (2, 0, 5)),
            ((1, 1, 5), (3, 0, 5)),
            ((1, 1, 5), (4, 0, 5)),
            ((1, 1, 5), (5, 0, 5)),
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        mahdolliset_blokit = mahdolliset_blokit + uudet_edessa
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)
