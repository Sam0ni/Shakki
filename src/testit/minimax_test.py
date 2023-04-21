import unittest
from pelilauta import Pelilauta
from minimax import Minimax


class TestMinimax(unittest.TestCase):

    def setUp(self):
        self.ruudun_koko = 125
        self.maxDiff = None

    def test_arviointi_oikein(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,8,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,9,0,7,0,0],
        [0,2,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

        minimax = Minimax(lauta)
        arvio = minimax.arvioi_pelitilanne()

        oikea_arvio = (-120 -500 + 120 + 500 + 335)
        self.assertEqual(arvio, oikea_arvio)

    def test_minimax_palauttaa_oikean_liikkeen_syvyydella_2(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,9,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 1)

        oikea_liike = ((9,2,4), (9,3,2))

        self.assertEqual(liike, oikea_liike)

    def test_minimax_palauttaa_oikean_liikkeen_syvyydella_3(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,9,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 2)

        oikea_liike = ((9,2,4), (9,3,2))

        self.assertEqual(liike, oikea_liike)
