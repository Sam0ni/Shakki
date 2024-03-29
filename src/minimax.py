import copy
from pelilauta import Pelilauta
from pelilogiikka.heuristiset_arvot import HeuristisetArvot

class Minimax:
    """Luokka joka sisältää metodit minimax-algoritmin toimintaan liittyen
    """

    def __init__(self, lauta):
        """Luokan konstruktori, jossa määritellään pelilaudan tilanteen 
        arviointiin tarvittavat muuttujat
        ja väliaikainen pelilauta liikkumista varten

        Args:
            lauta (list): kopio pelilaudasta
        """
        self.valiaikainen_pelilauta = Pelilauta(lauta, 125)
        heuristiset_arvot = HeuristisetArvot()
        arvot = heuristiset_arvot.hae()
        self.nappula_arvot = arvot[0]
        self.valkoinen_lauta_arvot = arvot[1]
        self.musta_lauta_arvot = arvot[2]

    def aloita(self, lauta, liikkeet, edessa, syvyys):
        """aloita algoritmin suorittaminen

        Args:
            lauta (list): kopio senhetkisestä laudasta
            liikkeet (list): lista kaikista liikkeistä
            edessa (list): lista kaikista edessä olevista nappuloista
            syvyys (int): laskennan syvyys

        Returns:
            tuple: paras mahdollinen liike
        """
        paras_liike = None
        parhaan_liikkeen_arvo = -9999999999999
        for liike in liikkeet:
            if liike[0][0] > 6:
                voitto = False
                kopio_lauta = copy.deepcopy(lauta)
                self.valiaikainen_pelilauta.lauta = kopio_lauta
                seuraavat_liikkeet = self.valiaikainen_pelilauta.liiku(liike[0],
                            liike[1], liikkeet, edessa)
                uudet_mahdolliset_liikkeet = seuraavat_liikkeet[0]
                uudet_edessa = seuraavat_liikkeet[1]
                shakissa = False
                if seuraavat_liikkeet[3]: # oma shakissa laiton liike
                    continue
                for mahis in uudet_mahdolliset_liikkeet:
                    if self.valiaikainen_pelilauta.lauta[mahis[1][1]][mahis[1][2]] == 12:
                        shakissa = True
                        break
                if shakissa:
                    continue
                if seuraavat_liikkeet[2]: # valkoinen shakissa, tarkistetaan matti
                    voitto = self.valiaikainen_pelilauta.tarkista_matti(
                        uudet_mahdolliset_liikkeet, uudet_edessa, True, seuraavat_liikkeet[4])
                liikkeen_arvo = self.minimax(self.valiaikainen_pelilauta.lauta, # kutsutaan minimaxia
                    uudet_mahdolliset_liikkeet, uudet_edessa, syvyys - 1,
                    parhaan_liikkeen_arvo, 999999999999, False, voitto)
                if parhaan_liikkeen_arvo < liikkeen_arvo:
                    parhaan_liikkeen_arvo = liikkeen_arvo # uusi paras liike
                    paras_liike = liike
        if parhaan_liikkeen_arvo == -9999999999999: # pattitilanne
            return "stalemate"
        return paras_liike

    def minimax(self, lauta, liikkeet, edessa, syvyys, alfa, beta, maksimoiva, voitto): # pylint: disable=too-many-statements
        """Metodi joka sisältää itse algoritmin

        Args:
            lauta (list): kopio laudasta liikkeen jälkeen
            liikkeet (list): lista mahdollisista liikkeistä
            edessa (list): lista edessä olevista nappuloista
            syvyys (int): laskennan syvyys
            alfa (int): alfa-beta karsinnan alfa-arvo
            beta (int): alfa-beta karsinnan beta-arvo
            maksimoiva (boolean): muuttuja jolla määritellään onko 
                            maksimoivan vai minimoivan osan vuoro
            voitto (bool): onko shakkimatti

        Returns:
            int: pelitilanteen arvo
        """
        if voitto:
            if maksimoiva: # musta shakkimatissa
                return (syvyys + 1) * -50000000
            return (syvyys + 1) * 50000000 # valkoinen shakkimatissa
        elif syvyys == 0:
            return self.arvioi_pelitilanne()

        elif maksimoiva:
            arvo = -999999999999
            for liike in liikkeet:
                if liike[0][0] > 6:
                    voitto = False
                    kopio_lauta = copy.deepcopy(lauta)
                    self.valiaikainen_pelilauta.lauta = kopio_lauta
                    seuraavat_liikkeet = self.valiaikainen_pelilauta.liiku(liike[0],
                                liike[1], liikkeet, edessa)
                    uudet_mahdolliset_liikkeet = seuraavat_liikkeet[0]
                    uudet_edessa = seuraavat_liikkeet[1]
                    if seuraavat_liikkeet[3]: # oma shakissa, laiton liike
                        continue
                    if seuraavat_liikkeet[2]: # valkoinen shakissa, tarkistetaan matti
                        voitto = self.valiaikainen_pelilauta.tarkista_matti(
                            uudet_mahdolliset_liikkeet, uudet_edessa, True, seuraavat_liikkeet[4])
                    arvo = max(arvo, self.minimax(self.valiaikainen_pelilauta.lauta,
                        uudet_mahdolliset_liikkeet,
                        uudet_edessa, syvyys - 1, alfa, beta, False, voitto))
                    alfa = max(alfa, arvo)
                    if arvo >= beta:
                        break
            if arvo == -999999999999: #pattitilanne
                return 0
            return arvo

        else:
            arvo = 999999999999
            for liike in liikkeet:
                if liike[0][0] <= 6:
                    voitto = False
                    kopio_lauta = copy.deepcopy(lauta)
                    self.valiaikainen_pelilauta.lauta = kopio_lauta
                    seuraavat_liikkeet = self.valiaikainen_pelilauta.liiku(liike[0],
                                liike[1], liikkeet, edessa)
                    uudet_mahdolliset_liikkeet = seuraavat_liikkeet[0]
                    uudet_edessa = seuraavat_liikkeet[1]
                    if seuraavat_liikkeet[2]: # oma shakissa, laiton liike
                        continue
                    if seuraavat_liikkeet[3]: # musta shakissa, tarkistetaan matti
                        voitto = self.valiaikainen_pelilauta.tarkista_matti(
                            uudet_mahdolliset_liikkeet, uudet_edessa, False, seuraavat_liikkeet[5])
                    arvo = min(arvo, self.minimax(self.valiaikainen_pelilauta.lauta,
                        uudet_mahdolliset_liikkeet,
                        uudet_edessa, syvyys - 1, alfa, beta, True, voitto))
                    beta = min(beta, arvo)
                    if arvo <= alfa:
                        break
            if arvo == 999999999999: #pattitilanne
                return 0
            return arvo

    def arvioi_pelitilanne(self):
        """metodi joka arvio pelitilanteen

        Returns:
            int: pelitilanteen arvo
        """
        arvo = 0
        for y in range(8): # pylint: disable=invalid-name
            for x in range(8): # pylint: disable=invalid-name
                if self.valiaikainen_pelilauta.lauta[y][x] == 0:
                    continue
                if self.valiaikainen_pelilauta.lauta[y][x] < 7:
                    arvo -= (self.nappula_arvot[self.valiaikainen_pelilauta.lauta[y][x]]
                        + self.valkoinen_lauta_arvot[self.valiaikainen_pelilauta.lauta[y][x]][y][x])
                else:
                    arvo += (self.nappula_arvot[self.valiaikainen_pelilauta.lauta[y][x]]
                        + self.musta_lauta_arvot[self.valiaikainen_pelilauta.lauta[y][x]][y][x])
        return arvo
