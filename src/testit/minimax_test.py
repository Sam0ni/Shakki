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
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 2)

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
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 3)

        oikea_liike = ((9,2,4), (9,3,2))

        self.assertEqual(liike, oikea_liike)

    def test_minimax_osaa_tehda_1_liikkeen_shakkimatin(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,8,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,8,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,6]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 4)

        oikea_liike = ((8,5,3), (8,5,7))

        self.assertEqual(liike, oikea_liike)

    def test_minimax_osaa_tehda_2_liikkeen_shakkimatin(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,8,0],
        [0,0,0,0,0,0,0,0],
        [2,0,0,8,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,6]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 4)

        oikea_liike = ((8,3,3), (8,3,0))

        self.assertEqual(liike, oikea_liike)

        uudet = pelilauta.liiku((8,3,3), (8,3,0), mahdolliset_liikkeet, edessa)

        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 4)

        oikea_liike = ((8,3,0), (8,3,7))

        self.assertEqual(liike, oikea_liike)

    def test_minimax_osaa_tehda_shakkimatin_1(self):
        lauta = [[12,0,0,0,0,0,0,0],
        [8,0,0,0,0,0,0,0],
        [8,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,6,0],
        [0,0,0,0,0,0,0,0]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 5)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((6, 6, 6), (6, 5, 6), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 5)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((6, 5, 6), (6, 5, 7), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 5)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        matti = pelilauta.tarkista_matti(mahdolliset_liikkeet, edessa, True, uudet[4])

        self.assertEqual(matti, True)

    def test_minimax_osaa_tehdä_shakkimatin_2(self):
        lauta = [[12,8,0,0,0,0,0,0],
        [0,8,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,6,0,0],
        [0,0,0,0,0,0,0,0]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 7)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((6, 6, 5), (6, 5, 5), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 7)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((6, 5, 5), (6, 5, 6), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 7)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((6, 5, 6), (6, 5, 7), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 7)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        matti = pelilauta.tarkista_matti(mahdolliset_liikkeet, edessa, True, uudet[4])

        self.assertEqual(matti, True)

    def test_minimax_osaa_tehda_shakkimatin_3(self):
        lauta = [[0,0,0,0,0,12,0,6],
        [0,0,0,0,0,0,7,7],
        [0,0,0,7,0,0,8,8],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 5)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((1, 6, 7), (1, 4, 7), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 5)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((1, 4, 7), (1, 3, 7), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 5)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        matti = pelilauta.tarkista_matti(mahdolliset_liikkeet, edessa, True, uudet[4])

        self.assertEqual(matti, True)

    def test_minimax_osaa_tehda_shakkimatin_4(self):
        lauta = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [7,0,0,0,0,0,0,0],
        [1,0,7,10,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [6,0,0,12,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,9,0,0,0,0,0]]

        mahdolliset_liikkeet = []
        edessa = []

        pelilauta = Pelilauta(lauta, self.ruudun_koko)
        minimax = Minimax(lauta)
        uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = pelilauta.alusta()
        mahdolliset_liikkeet = mahdolliset_liikkeet + uudet_liikkeet
        edessa = edessa + uudet_edessa
        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 7)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]
        
        uudet = pelilauta.liiku((6, 5, 0), (6, 4, 0), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 7)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((6, 4, 0), (6, 5, 0), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 7)

        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        uudet = pelilauta.liiku((6, 5, 0), (6, 4, 0), mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        liike = minimax.aloita(lauta, mahdolliset_liikkeet, edessa, 7)
        uudet = pelilauta.liiku(liike[0], liike[1], mahdolliset_liikkeet, edessa)
        mahdolliset_liikkeet = uudet[0]
        edessa = uudet[1]

        matti = pelilauta.tarkista_matti(mahdolliset_liikkeet, edessa, True, uudet[4])

        self.assertEqual(matti, True)