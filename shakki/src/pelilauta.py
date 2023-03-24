import pygame
from spritet.sotilas import Sotilas


class Pelilauta:
    def __init__(self, lauta, ruudun_koko):
        self.lauta = lauta
        self.ruudun_koko = ruudun_koko
        self.mustat_sotilaat = pygame.sprite.Group()
        self.valkoiset_sotilaat = pygame.sprite.Group()
        self.kaikki_spritet = pygame.sprite.Group()
        self._alusta_spritet()

    def _alusta_spritet(self):
        for i in range(8):
            uusi_sotilas = Sotilas(i * self.ruudun_koko, 6 * self.ruudun_koko, True)
            self.valkoiset_sotilaat.add(uusi_sotilas)
            self.lauta[6][i] = uusi_sotilas
        for i in range(8):
            uusi_sotilas = Sotilas(i * self.ruudun_koko, 1 * self.ruudun_koko, False)
            self.mustat_sotilaat.add(uusi_sotilas)
            self.lauta[1][i] = uusi_sotilas
        self.kaikki_spritet.add(
            self.mustat_sotilaat,
            self.valkoiset_sotilaat
        )

    def tarkista_liikkeet_valkoinen(self):
        mahdolliset_liikkeet = []
        mones = 1
        for sotilas in self.valkoiset_sotilaat:
            alkup_x = 0 + sotilas.rect.x
            alkup_y = 0 + sotilas.rect.y
            print(f"sotilas: {mones}")
            print(sotilas.rect.x)
            print(sotilas.rect.y)
            mones += 1
            sotilas.rect.move_ip(0, -self.ruudun_koko)
            if self.lauta[int(sotilas.rect.y / self.ruudun_koko)][int(sotilas.rect.x / self.ruudun_koko)] == 0:
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
                if not sotilas.liikutettu:
                    sotilas.rect.move_ip(0, -self.ruudun_koko)
                    if self.lauta[int(sotilas.rect.y / self.ruudun_koko)][int(sotilas.rect.x / self.ruudun_koko)] == 0:
                        mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
                    sotilas.rect.move_ip(0, self.ruudun_koko)
            sotilas.rect.move_ip(self.ruudun_koko, 0)
            if pygame.sprite.spritecollide(sotilas, self.mustat_sotilaat, False):
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
            sotilas.rect.move_ip(-self.ruudun_koko * 2, 0)
            if pygame.sprite.spritecollide(sotilas, self.mustat_sotilaat, False):
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
            sotilas.rect.move_ip(self.ruudun_koko, self.ruudun_koko)

        return mahdolliset_liikkeet

    def tarkista_liikkeet_musta(self):
        mahdolliset_liikkeet = []
        for sotilas in self.mustat_sotilaat:
            alkup_x = 0 + sotilas.rect.x
            alkup_y = 0 + sotilas.rect.y
            sotilas.rect.move_ip(0, self.ruudun_koko)
            if self.lauta[int(sotilas.rect.x / self.ruudun_koko)][int(sotilas.rect.y / self.ruudun_koko)] == 0:
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
                if not sotilas.liikutettu:
                    sotilas.rect.move_ip(0, self.ruudun_koko)
                    print(int(sotilas.rect.x / self.ruudun_koko))
                    print(int(sotilas.rect.y / self.ruudun_koko))
                    if self.lauta[int(sotilas.rect.x / self.ruudun_koko)][int(sotilas.rect.y / self.ruudun_koko)] == 0:
                        mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
                    sotilas.rect.move_ip(0, self.ruudun_koko)
            sotilas.rect.move_ip(self.ruudun_koko, 0)
            if pygame.sprite.spritecollide(sotilas, self.valkoiset_sotilaat, False):
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
            sotilas.rect.move_ip(-self.ruudun_koko * 2, 0)
            if pygame.sprite.spritecollide(sotilas, self.valkoiset_sotilaat, False):
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
            sotilas.rect.x = alkup_x
            sotilas.rect.y = alkup_y
        return mahdolliset_liikkeet

    def liiku_valkoinen(self, nappula, ruutu):
        alkp_x = int((0 + nappula.rect.x) / self.ruudun_koko)
        alkp_y = int((0 + nappula.rect.y) / self.ruudun_koko)
        self.lauta[alkp_y][alkp_x] = 0
        self.lauta[ruutu[1]][ruutu[0]] = nappula
        print(self.lauta)
        pygame.sprite.spritecollide(nappula, self.mustat_sotilaat, True)
        nappula.rect.x = ruutu[0] * self.ruudun_koko
        nappula.rect.y = ruutu[1] * self.ruudun_koko

    def liiku_musta(self, nappula, ruutu):
        alkp_x = int((0 + nappula.rect.x) / self.ruudun_koko)
        alkp_y = int((0 + nappula.rect.y) / self.ruudun_koko)
        self.lauta[alkp_y][alkp_x] = 0
        self.lauta[ruutu[1]][ruutu[0]] = nappula
        pygame.sprite.spritecollide(nappula, self.valkoiset_sotilaat, True)
        