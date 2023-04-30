from pelilauta import Pelilauta
from pelilogiikka.heuristiset_arvot import Heuristiset_arvot
import copy

class Minimax:
    """Luokka joka sisältää metodit minimax-algoritmin toimintaan liittyen
    """

    def __init__(self, lauta):
        """Luokan konstruktori, jossa määritellään pelilaudan tilanteen arviointiin tarvittavat muuttujat
        ja väliaikainen pelilauta liikkumista varten

        Args:
            lauta (list): kopio pelilaudasta
        """
        self.valiaikainen_pelilauta = Pelilauta(lauta, 125)
        heuristiset_arvot = Heuristiset_arvot()
        self.nappula_arvot, self.valkoinen_lauta_arvot, self.musta_lauta_arvot = heuristiset_arvot.hae()

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
        paras_liike = ""
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
                if seuraavat_liikkeet[2]:
                    voitto = self.valiaikainen_pelilauta.tarkista_matti(uudet_mahdolliset_liikkeet, uudet_edessa, True, seuraavat_liikkeet[4])
                elif seuraavat_liikkeet[3]:
                    continue
                liikkeen_arvo = self.minimax(self.valiaikainen_pelilauta.lauta, uudet_mahdolliset_liikkeet, uudet_edessa, syvyys, parhaan_liikkeen_arvo, 99999999, False, voitto)
                if parhaan_liikkeen_arvo < liikkeen_arvo:
                    parhaan_liikkeen_arvo = liikkeen_arvo
                    paras_liike = liike
        return paras_liike

    def minimax(self, lauta, liikkeet, edessa, syvyys, alfa, beta, maksimoiva, voitto):
        """Metodi joka sisältää itse algoritmin

        Args:
            lauta (list): kopio laudasta liikkeen jälkeen
            liikkeet (list): lista mahdollisista liikkeistä
            edessa (list): lista edessä olevista nappuloista
            syvyys (int): laskennan syvyys
            alfa (int): alfa-beta karsinnan alfa-arvo
            beta (int): alfa-beta karsinnan beta-arvo
            maksimoiva (boolean): muuttuja jolla määritellään onko maksimoivan vai minimoivan osan vuoro
            voitto (bool): onko shakkimatti

        Returns:
            int: pelitilanteen arvo
        """
        if syvyys == 0:
            return self.arvioi_pelitilanne()
        elif voitto:
            if maksimoiva:
                return (syvyys + 1) * -50000000000
            else:
                return (syvyys + 1) * 50000000000

        if maksimoiva:
            arvo = -999999999
            for liike in liikkeet:
                if liike[0][0] > 6:
                    voitto = False
                    kopio_lauta = copy.deepcopy(lauta)
                    self.valiaikainen_pelilauta.lauta = kopio_lauta
                    seuraavat_liikkeet = self.valiaikainen_pelilauta.liiku(liike[0],
                                liike[1], liikkeet, edessa)
                    uudet_mahdolliset_liikkeet = seuraavat_liikkeet[0]
                    uudet_edessa = seuraavat_liikkeet[1]
                    if seuraavat_liikkeet[2]:
                        voitto = self.valiaikainen_pelilauta.tarkista_matti(uudet_mahdolliset_liikkeet, uudet_edessa, True, seuraavat_liikkeet[4])
                    elif seuraavat_liikkeet[3]:
                        continue
                    arvo = max(arvo, self.minimax(self.valiaikainen_pelilauta.lauta, uudet_mahdolliset_liikkeet, uudet_edessa, syvyys - 1, alfa, beta, False, voitto))
                    alfa = max(alfa, arvo)
                    if arvo >= beta:
                        break
            return arvo 

        else:
            arvo = 999999999
            for liike in liikkeet:
                if liike[0][0] <= 6:
                    voitto = False
                    kopio_lauta = copy.deepcopy(lauta)
                    self.valiaikainen_pelilauta.lauta = kopio_lauta
                    seuraavat_liikkeet = self.valiaikainen_pelilauta.liiku(liike[0],
                                liike[1], liikkeet, edessa)
                    uudet_mahdolliset_liikkeet = seuraavat_liikkeet[0]
                    uudet_edessa = seuraavat_liikkeet[1]
                    if seuraavat_liikkeet[3]:
                        voitto = self.valiaikainen_pelilauta.tarkista_matti(uudet_mahdolliset_liikkeet, uudet_edessa, False, seuraavat_liikkeet[5])
                    elif seuraavat_liikkeet[2]:
                        continue
                    arvo = min(arvo, self.minimax(self.valiaikainen_pelilauta.lauta, uudet_mahdolliset_liikkeet, uudet_edessa, syvyys - 1, alfa, beta, True, voitto))
                    beta = min(beta, arvo)
                    if arvo <= alfa:
                        break
            return arvo 

    def arvioi_pelitilanne(self):
        """metodi joka arvio pelitilanteen

        Returns:
            int: pelitilanteen arvo
        """
        arvo = 0
        for y in range(8):
            for x in range(8):
                if self.valiaikainen_pelilauta.lauta[y][x] == 0:
                    continue
                elif self.valiaikainen_pelilauta.lauta[y][x] < 7:
                    arvo -= (self.nappula_arvot[self.valiaikainen_pelilauta.lauta[y][x]] + self.valkoinen_lauta_arvot[self.valiaikainen_pelilauta.lauta[y][x]][y][x])
                else:
                    arvo += (self.nappula_arvot[self.valiaikainen_pelilauta.lauta[y][x]] + self.musta_lauta_arvot[self.valiaikainen_pelilauta.lauta[y][x]][y][x])
        return arvo
