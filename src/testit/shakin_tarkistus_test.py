import unittest
from pelilauta import Pelilauta


class TestShakki(unittest.TestCase):

    def setUp(self):
        self.ruudun_koko = 125
        self.maxDiff = None
    
    def test_shakkimatin_tarkistus_toimii(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,8],
        [0,0,0,0,0,0,8,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,6]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        tulos = pelilauta.tarkista_matti(uudet_liikkeet, uudet_edessa, True, valkoisen_shakkaajat)
        self.assertEqual(tulos, True)

        lauta = [[0,0,0,0,0,0,0,0],
        [2,0,0,0,0,0,0,8],
        [0,0,0,0,0,0,8,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,6]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        tulos = pelilauta.tarkista_matti(uudet_liikkeet, uudet_edessa, True, valkoisen_shakkaajat)
        self.assertEqual(tulos, False)

    def test_shakkimatin_tarkistus_toimii_2(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,2,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,12]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        tulos = pelilauta.tarkista_matti(uudet_liikkeet, uudet_edessa, False, mustan_shakkaajat)
        self.assertEqual(tulos, True)

        lauta = [[0,0,0,0,0,0,0,0],
        [8,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,2,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,12]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        tulos = pelilauta.tarkista_matti(uudet_liikkeet, uudet_edessa, False, mustan_shakkaajat)
        self.assertEqual(tulos, False)

    def test_shakki_tarkistetaan_oikein_sotilas(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,12,0,12,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,7,0,0,0],
        [0,0,0,6,0,6,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()

        self.assertEqual(valkoinen_shakissa, True)
        self.assertEqual(musta_shakissa, True)
        self.assertEqual(len(mustan_shakkaajat), 2)
        self.assertEqual(len(valkoisen_shakkaajat), 2)

    def test_shakki_tarkistetaan_oikein_sotilas_korotus(self):
        lauta = [[0,0,12,0,12,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,7,0,0,0],
        [0,0,0,6,0,6,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()

        self.assertEqual(valkoinen_shakissa, True)
        self.assertEqual(musta_shakissa, True)
        self.assertEqual(len(mustan_shakkaajat), 2)
        self.assertEqual(len(valkoisen_shakkaajat), 2)

    def test_shakki_tarkistetaan_oikein_ratsu(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,6,0,0,0,12,0],
        [0,0,0,0,9,0,0,0],
        [0,0,0,0,3,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,6,0,12,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()

        self.assertEqual(valkoinen_shakissa, True)
        self.assertEqual(musta_shakissa, True)
        self.assertEqual(len(mustan_shakkaajat), 1)
        self.assertEqual(len(valkoisen_shakkaajat), 1)

    def test_shakki_tarkistetaan_oikein_vaaka(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,8,0,12,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,6,0,0,0,0,0,0],
        [0,2,0,12,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()

        self.assertEqual(valkoinen_shakissa, True)
        self.assertEqual(musta_shakissa, True)
        self.assertEqual(len(mustan_shakkaajat), 1)
        self.assertEqual(len(valkoisen_shakkaajat), 1)

    def test_shakki_tarkistetaan_oikein_viisto(self):
        lauta = [[0,0,0,0,12,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,4,0],
        [0,0,0,0,0,0,0,6],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,10,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,12,0,0,0,0]]
        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()

        self.assertEqual(valkoinen_shakissa, True)
        self.assertEqual(musta_shakissa, True)
        self.assertEqual(len(mustan_shakkaajat), 1)
        self.assertEqual(len(valkoisen_shakkaajat), 1)
