import pygame

class Komennot:
    def __init__(self):
        self.komennot = self.alusta_komennot()     

    def alusta_komennot(self):
        komennot = {
            pygame.K_d: self.resetoi_valinta,
            pygame.K_2: self.torni_korotus,
            pygame.K_3: self.ratsu_korotus,
            pygame.K_4: self.lahetti_korotus,
            pygame.K_5: self.kuningatar_korotus,
            pygame.K_UP: self.kasvata_syvyytta,
            pygame.K_DOWN: self.pienenna_syvyytta,
            pygame.K_m: self.ai_paalle_pois
        }
        return komennot
    
    def valinta_komento(self, silmukka):
        x, y = pygame.mouse.get_pos()
        x = x // silmukka._ruudun_koko # pylint: disable=invalid-name
        y = y // silmukka._ruudun_koko # pylint: disable=invalid-name
        if x > 7 or y > 7:
            return
        if silmukka.valittu_nappula == "":
            if silmukka._pelilauta.lauta[y][x] != 0:
                silmukka.valitse_nappula(y, x)
        else:
            silmukka.validoi_liike(y, x)

    def resetoi_valinta(self, silmukka):
        silmukka.valittu_nappula = ""

    def torni_korotus(self, silmukka):
        silmukka.korotus = 2
    
    def ratsu_korotus(self, silmukka):
        silmukka.korotus = 3

    def lahetti_korotus(self, silmukka):
        silmukka.korotus = 4

    def kuningatar_korotus(self, silmukka):
        silmukka.korotus = 5

    def kasvata_syvyytta(self, silmukka):
        if silmukka.syvyys < 7:
            silmukka.syvyys += 1

    def pienenna_syvyytta(self, silmukka):
        if silmukka.syvyys > 0:
            silmukka.syvyys -= 1

    def ai_paalle_pois(self, silmukka):
        silmukka.tekoaly_kaytossa = not silmukka.tekoaly_kaytossa

    def suorita_komento(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]
        else:
            return self.dummy

    def dummy(self, silmukka):
        pass