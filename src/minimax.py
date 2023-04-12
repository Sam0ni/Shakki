from pelilauta import Pelilauta
import copy

class Minimax:

    def __init__(self, lauta):
        self.valiaikainen_pelilauta = Pelilauta(lauta, 125)
        self.nappula_arvot = {1: 100, 2: 320, 3: 330, 4: 500, 5: 900, 6: 20000, 7: 100, 8: 320, 9: 330, 10: 500, 11: 900, 12: 20000}

    def aloita(self, lauta, liikkeet, edessa):
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
                liikkeen_arvo = self.minimax(self.valiaikainen_pelilauta.lauta, uudet_mahdolliset_liikkeet, uudet_edessa, 2, -999999999, 999999999, False)
                if parhaan_liikkeen_arvo < liikkeen_arvo:
                    parhaan_liikkeen_arvo = liikkeen_arvo
                    paras_liike = liike
        return paras_liike

    def minimax(self, lauta, liikkeet, edessa, syvyys, alfa, beta, maksimoiva):
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
                            liike[1],)
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
                            liike[1],)
                    arvo = min(arvo, self.minimax(self.valiaikainen_pelilauta.lauta, uudet_mahdolliset_liikkeet, uudet_edessa, syvyys - 1, alfa, beta, True))
                    beta = min(beta, arvo)
                    if arvo <= alfa:
                        break
            return arvo 

    def arvioi_pelitilanne(self):
        arvo = 0
        for y in range(8):
            for x in range(8):
                if self.valiaikainen_pelilauta.lauta[y][x] == 0:
                    continue
                elif self.valiaikainen_pelilauta.lauta[y][x] < 7:
                    arvo -= self.nappula_arvot[self.valiaikainen_pelilauta.lauta[y][x]]
                else:
                    arvo += self.nappula_arvot[self.valiaikainen_pelilauta.lauta[y][x]]
        return arvo
