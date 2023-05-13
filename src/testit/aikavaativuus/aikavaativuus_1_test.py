import unittest
from pelilauta import Pelilauta
from minimax import Minimax


class TestMinimax(unittest.TestCase):

    def setUp(self):
        self.ruudun_koko = 125
        self.maxDiff = None

    def test_syvyys_1(self):
        lauta = [[8,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,12,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,6,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,2]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 1)

        return