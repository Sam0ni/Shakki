import unittest
from pelilauta import Pelilauta


class TestLiikkuminen(unittest.TestCase):

    def setUp(self):
        self.ruudun_koko = 125
        self.maxDiff = None
    
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        mahdolliset_blokit = mahdolliset_blokit + uudet_edessa

        mahdolliset_liikkeet, mahdolliset_blokit, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.liiku((1, 5, 4), (1, 4, 3), mahdolliset_liikkeet, mahdolliset_blokit)
        
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

        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        mahdolliset_blokit = mahdolliset_blokit + uudet_edessa

        mahdolliset_liikkeet, mahdolliset_blokit, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.liiku((2, 4, 4), (2, 2, 4), mahdolliset_liikkeet, mahdolliset_blokit)
        
        self.assertCountEqual(mahdolliset_liikkeet, tiedetyt_liikkeet)
        self.assertCountEqual(mahdolliset_blokit, tiedetyt_blokit)

        self.assertEqual(lauta_siirron_jalkeen, pelilauta.lauta)
