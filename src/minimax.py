from pelilauta import Pelilauta
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
        self.nappula_arvot = {1: 100, 2: 500, 3: 320, 4: 330, 5: 900, 6: 20000, 7: 100, 8: 500, 9: 320, 10: 330, 11: 900, 12: 20000}
        self.valkoinen_lauta_arvot = {
            1: [[0,0,0,0,0,0,0,0],
                [50,50,50,50,50,50,50,50],
                [10,10,20,30,30,20,10,10],
                [5,5,10,25,25,10,5,5],
                [0,0,0,20,20,0,0,0],
                [5,-5,-10,0,0,-10,-5,5],
                [5,10,10,-20,-20,10,10,5],
                [0,0,0,0,0,0,0,0]],
            2: [[0,0,0,0,0,0,0,0],
                [5,10,10,10,10,10,10,5],
                [-5,0,0,0,0,0,0,-5],
                [-5,0,0,0,0,0,0,-5],
                [-5,0,0,0,0,0,0,-5],
                [-5,0,0,0,0,0,0,-5],
                [-5,0,0,0,0,0,0,-5],
                [0,0,0,5,5,0,0,0]],
            3: [[-50,-40,-30,-30,-30,-30,-40,-50],
                [-40,-20,0,0,0,0,-20,-40],
                [-30,0,10,15,15,10,0,-30],
                [-30,5,15,20,20,15,5,-30],
                [-30,0,15,20,20,15,0,-30],
                [-30,5,10,15,15,10,5,-30],
                [-40,-20,0,5,5,0,-20,-40],
                [-50,-40,-30,-30,-30,-30,-40,-50]],
            4: [[-20,-10,-10,-10,-10,-10,-10,-20],
                [-10,0,0,0,0,0,0,-10],
                [-10,0,5,10,10,5,0,-10],
                [-10,5,5,10,10,5,5,-10],
                [-10,0,10,10,10,10,0,-10],
                [-10,10,10,10,10,10,10,-10],
                [-10,5,0,0,0,0,5,-10],
                [-20,-10,-10,-10,-10,-10,-10,-20]],
            5: [[-20,-10,-10,-5,-5,-10,-10,-20],
                [-10,0,0,0,0,0,0,-10],
                [-10,0,5,5,5,5,0,-10],
                [-5,0,5,5,5,5,0,-5],
                [0,0,5,5,5,5,0,-5],
                [-10,5,5,5,5,5,0,-10],
                [-10,0,5,0,0,0,0,-10],
                [-20,-10,-10,-5,-5,-10,-10,-20]],
            6: [[-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-20,-30,-30,-40,-40,-30,-30,-20],
                [-10,-20,-20,-20,-20,-20,-20,-10],
                [20,20,0,0,0,0,20,20],
                [20,30,10,0,0,10,30,20]]
        }
        self.musta_lauta_arvot = {
            7: [[0,0,0,0,0,0,0,0],
                [5,10,10,-20,-20,10,10,5],
                [5,-5,-10,0,0,-10,-5,5],
                [0,0,0,20,20,0,0,0],
                [5,5,10,25,25,10,5,5],
                [10,10,20,30,30,20,10,10],
                [50,50,50,50,50,50,50,50],
                [0,0,0,0,0,0,0,0]],
            8: [[0,0,0,5,5,0,0,0],
                [-5,0,0,0,0,0,0,-5],
                [-5,0,0,0,0,0,0,-5],
                [-5,0,0,0,0,0,0,-5],
                [-5,0,0,0,0,0,0,-5],
                [-5,0,0,0,0,0,0,-5],
                [5,10,10,10,10,10,10,5],
                [0,0,0,0,0,0,0,0]],
            9:  [[-50,-40,-30,-30,-30,-30,-40,-50],
                [-40,-20,0,5,5,0,-20,-40],
                [-30,5,10,15,15,10,5,-30],
                [-30,0,15,20,20,15,0,-30],
                [-30,5,15,20,20,15,5,-30],
                [-30,0,10,15,15,10,0,-30],
                [-40,-20,0,0,0,0,-20,-40],
                [-50,-40,-30,-30,-30,-30,-40,-50]],
            10: [[-20,-10,-10,-10,-10,-10,-10,-20],
                [-10,5,0,0,0,0,5,-10],
                [-10,10,10,10,10,10,10,-10],
                [-10,0,10,10,10,10,0,-10],
                [-10,5,5,10,10,5,5,-10],
                [-10,0,5,10,10,5,0,-10],
                [-10,0,0,0,0,0,0,-10],
                [-20,-10,-10,-10,-10,-10,-10,-20]],
            11: [[-20,-10,-10,-5,-5,-10,-10,-20],
                [-10,0,5,0,0,0,0,-10],
                [-10,5,5,5,5,5,0,-10],
                [0,0,5,5,5,5,0,-5],
                [-5,0,5,5,5,5,0,-5],
                [-10,0,5,5,5,5,0,-10],
                [-10,0,0,0,0,0,0,-10],
                [-20,-10,-10,-5,-5,-10,-10,-20]],
            12: [[20,30,10,0,0,10,30,20],
                [20,20,0,0,0,0,20,20],
                [-10,-20,-20,-20,-20,-20,-20,-10],
                [-20,-30,-30,-40,-40,-30,-30,-20],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30]]
        }

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
        parhaan_liikkeen_arvo = -99999999999
        for liike in liikkeet:
            if liike[0][0] > 6:
                kopio_lauta = copy.deepcopy(lauta)
                self.valiaikainen_pelilauta.lauta = kopio_lauta
                seuraavat_liikkeet = self.valiaikainen_pelilauta.liiku(liike[0],
                            liike[1], liikkeet, edessa)
                uudet_mahdolliset_liikkeet = seuraavat_liikkeet[0]
                uudet_edessa = seuraavat_liikkeet[1]
                uudet_mahdolliset_liikkeet, uudet_edessa = self.valiaikainen_pelilauta.paivita(
                            uudet_mahdolliset_liikkeet,
                            uudet_edessa, liike[0],
                            liike[1])
                liikkeen_arvo = self.minimax(self.valiaikainen_pelilauta.lauta, uudet_mahdolliset_liikkeet, uudet_edessa, syvyys, parhaan_liikkeen_arvo, 99999999, False)
                if parhaan_liikkeen_arvo < liikkeen_arvo:
                    parhaan_liikkeen_arvo = liikkeen_arvo
                    paras_liike = liike
        return paras_liike

    def minimax(self, lauta, liikkeet, edessa, syvyys, alfa, beta, maksimoiva):
        """Metodi joka sisältää itse algoritmin

        Args:
            lauta (list): kopio laudasta liikkeen jälkeen
            liikkeet (list): lista mahdollisista liikkeistä
            edessa (list): lista edessä olevista nappuloista
            syvyys (int): laskennan syvyys
            alfa (int): alfa-beta karsinnan alfa-arvo
            beta (int): alfa-beta karsinnan beta-arvo
            maksimoiva (boolean): muuttuja jolla määritellään onko maksimoivan vai minimoivan osan vuoro

        Returns:
            int: pelitilanteen arvo
        """
        if syvyys == 0:
            return self.arvioi_pelitilanne()
        if maksimoiva:
            arvo = -999999999
            for liike in liikkeet:
                if liike[0][0] > 6:
                    kopio_lauta = copy.deepcopy(lauta)
                    self.valiaikainen_pelilauta.lauta = kopio_lauta
                    seuraavat_liikkeet = self.valiaikainen_pelilauta.liiku(liike[0],
                                liike[1], liikkeet, edessa)
                    uudet_mahdolliset_liikkeet = seuraavat_liikkeet[0]
                    uudet_edessa = seuraavat_liikkeet[1]
                    uudet_mahdolliset_liikkeet, uudet_edessa = self.valiaikainen_pelilauta.paivita(
                            uudet_mahdolliset_liikkeet,
                            uudet_edessa, liike[0],
                            liike[1])
                    arvo = max(arvo, self.minimax(self.valiaikainen_pelilauta.lauta, uudet_mahdolliset_liikkeet, uudet_edessa, syvyys - 1, alfa, beta, False))
                    alfa = max(alfa, arvo)
                    if arvo >= beta:
                        break
            return arvo 
        else:
            arvo = 999999999
            for liike in liikkeet:
                if liike[0][0] <= 6:
                    kopio_lauta = copy.deepcopy(lauta)
                    self.valiaikainen_pelilauta.lauta = kopio_lauta
                    seuraavat_liikkeet = self.valiaikainen_pelilauta.liiku(liike[0],
                                liike[1], liikkeet, edessa)
                    uudet_mahdolliset_liikkeet = seuraavat_liikkeet[0]
                    uudet_edessa = seuraavat_liikkeet[1]
                    uudet_mahdolliset_liikkeet, uudet_edessa = self.valiaikainen_pelilauta.paivita(
                            uudet_mahdolliset_liikkeet,
                            uudet_edessa, liike[0],
                            liike[1])
                    arvo = min(arvo, self.minimax(self.valiaikainen_pelilauta.lauta, uudet_mahdolliset_liikkeet, uudet_edessa, syvyys - 1, alfa, beta, True))
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
