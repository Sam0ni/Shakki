import pygame
from spritet.sotilas import Sotilas
from spritet.torni import Torni


class Pelilauta:
    def __init__(self, lauta, ruudun_koko):
        self.lauta = lauta
        self.ruudun_koko = ruudun_koko
        self.mustat_sotilaat = pygame.sprite.Group()
        self.mustat_tornit = pygame.sprite.Group()
        self.mustat = pygame.sprite.Group()
        self.valkoiset_sotilaat = pygame.sprite.Group()
        self.valkoiset_tornit = pygame.sprite.Group()
        self.valkoiset = pygame.sprite.Group()
        self.kaikki_spritet = pygame.sprite.Group()
        self._alusta_spritet()

    def _alusta_spritet(self):
        for i in range(8):
            uusi_sotilas = Sotilas(i * self.ruudun_koko, 6 * self.ruudun_koko, True)
            self.valkoiset_sotilaat.add(uusi_sotilas)
            self.lauta[6][i] = uusi_sotilas
        uusi_torni = Torni(0 * self.ruudun_koko, 7 * self.ruudun_koko, True)
        self.valkoiset_tornit.add(uusi_torni)
        self.lauta[7][0] = uusi_torni
        uusi_torni = Torni(7 * self.ruudun_koko, 7 * self.ruudun_koko, True)
        self.valkoiset_tornit.add(uusi_torni)
        self.lauta[7][7] = uusi_torni
        for i in range(8):
            uusi_sotilas = Sotilas(i * self.ruudun_koko, 1 * self.ruudun_koko, False)
            self.mustat_sotilaat.add(uusi_sotilas)
            self.lauta[1][i] = uusi_sotilas
        uusi_torni = Torni(0 * self.ruudun_koko, 0 * self.ruudun_koko, False)
        self.mustat_tornit.add(uusi_torni)
        self.lauta[0][0] = uusi_torni
        uusi_torni = Torni(7 * self.ruudun_koko, 0 * self.ruudun_koko, False)
        self.mustat_tornit.add(uusi_torni)
        self.lauta[0][7] = uusi_torni
        self.mustat.add(
            self.mustat_sotilaat,
            self.mustat_tornit
        )
        self.valkoiset.add(
            self.valkoiset_sotilaat,
            self.valkoiset_tornit
        )
        self.kaikki_spritet.add(
            self.mustat_sotilaat,
            self.mustat_tornit,
            self.valkoiset_sotilaat,
            self.valkoiset_tornit
        )

    def tarkista_liikkeet_valkoinen(self):
        mahdolliset_liikkeet = []
        mones = 1
        for sotilas in self.valkoiset_sotilaat:
            alkup_x = 0 + sotilas.rect.x
            alkup_y = 0 + sotilas.rect.y
            sotilas.rect.move_ip(0, -self.ruudun_koko)
            if self.lauta[int(sotilas.rect.y / self.ruudun_koko)][int(sotilas.rect.x / self.ruudun_koko)] == 0:
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
                if not sotilas.liikutettu:
                    sotilas.rect.move_ip(0, -self.ruudun_koko)
                    if self.lauta[int(sotilas.rect.y / self.ruudun_koko)][int(sotilas.rect.x / self.ruudun_koko)] == 0:
                        mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
                    sotilas.rect.move_ip(0, self.ruudun_koko)
            sotilas.rect.move_ip(self.ruudun_koko, 0)
            if pygame.sprite.spritecollide(sotilas, self.mustat, False):
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
            sotilas.rect.move_ip(-self.ruudun_koko * 2, 0)
            if pygame.sprite.spritecollide(sotilas, self.mustat, False):
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
            sotilas.rect.x = alkup_x
            sotilas.rect.y = alkup_y
        for torni in self.valkoiset_tornit:
            alkup_x = 0 + torni.rect.x
            alkup_y = 0 + torni.rect.y
            for i in range(int(alkup_y / self.ruudun_koko), 0, -1):
                torni.rect.move_ip(0, -self.ruudun_koko)
                if self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                elif not self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                else:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
            torni.rect.x = alkup_x
            torni.rect.y = alkup_y
            for i in range(int(alkup_y / self.ruudun_koko), 7):
                torni.rect.move_ip(0, self.ruudun_koko)
                if self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                elif not self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                else:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
            torni.rect.x = alkup_x
            torni.rect.y = alkup_y
            for i in range(int(alkup_x / self.ruudun_koko), 0, -1):
                torni.rect.move_ip(-self.ruudun_koko, 0)
                if self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                elif not self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                else:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                if i == 0:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
            torni.rect.x = alkup_x
            torni.rect.y = alkup_y
            for i in range(int(alkup_x / self.ruudun_koko), 7):
                torni.rect.move_ip(self.ruudun_koko, 0)
                if self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                elif not self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                else:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
            torni.rect.x = alkup_x
            torni.rect.y = alkup_y

        return mahdolliset_liikkeet

    def tarkista_liikkeet_musta(self):
        mahdolliset_liikkeet = []
        for sotilas in self.mustat_sotilaat:
            alkup_x = 0 + sotilas.rect.x
            alkup_y = 0 + sotilas.rect.y
            sotilas.rect.move_ip(0, self.ruudun_koko)
            if self.lauta[int(sotilas.rect.y / self.ruudun_koko)][int(sotilas.rect.x / self.ruudun_koko)] == 0:
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
                if not sotilas.liikutettu:
                    sotilas.rect.move_ip(0, self.ruudun_koko)
                    if self.lauta[int(sotilas.rect.y / self.ruudun_koko)][int(sotilas.rect.x / self.ruudun_koko)] == 0:
                        mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
                    sotilas.rect.move_ip(0, self.ruudun_koko)
            sotilas.rect.move_ip(self.ruudun_koko, 0)
            if pygame.sprite.spritecollide(sotilas, self.valkoiset, False):
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
            sotilas.rect.move_ip(-self.ruudun_koko * 2, 0)
            if pygame.sprite.spritecollide(sotilas, self.valkoiset, False):
                mahdolliset_liikkeet.append((sotilas, (int(sotilas.rect.x / self.ruudun_koko), int(sotilas.rect.y / self.ruudun_koko))))
            sotilas.rect.x = alkup_x
            sotilas.rect.y = alkup_y
        for torni in self.mustat_tornit:
            alkup_x = 0 + torni.rect.x
            alkup_y = 0 + torni.rect.y
            for i in range(int(alkup_y / self.ruudun_koko), 0, -1):
                torni.rect.move_ip(0, -self.ruudun_koko)
                if self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                elif self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                else:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
            torni.rect.x = alkup_x
            torni.rect.y = alkup_y
            for i in range(int(alkup_y / self.ruudun_koko), 7):
                torni.rect.move_ip(0, self.ruudun_koko)
                if self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                elif self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                else:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
            torni.rect.x = alkup_x
            torni.rect.y = alkup_y
            for i in range(int(alkup_x / self.ruudun_koko), 0, -1):
                torni.rect.move_ip(-self.ruudun_koko, 0)
                if self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                elif self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                else:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                if i == 0:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
            torni.rect.x = alkup_x
            torni.rect.y = alkup_y
            for i in range(int(alkup_x / self.ruudun_koko), 7):
                torni.rect.move_ip(self.ruudun_koko, 0)
                if self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                elif self.lauta[int(torni.rect.y / self.ruudun_koko)][int(torni.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((torni, (int(torni.rect.x / self.ruudun_koko), int(torni.rect.y / self.ruudun_koko))))
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
                else:
                    torni.rect.x = alkup_x
                    torni.rect.y = alkup_y
                    break
            torni.rect.x = alkup_x
            torni.rect.y = alkup_y
        return mahdolliset_liikkeet

    def liiku_valkoinen(self, nappula, ruutu):
        nappula.liikutettu = True
        alkp_x = int((0 + nappula.rect.x) / self.ruudun_koko)
        alkp_y = int((0 + nappula.rect.y) / self.ruudun_koko)
        nappula.rect.x = ruutu[0] * self.ruudun_koko
        nappula.rect.y = ruutu[1] * self.ruudun_koko
        self.lauta[alkp_y][alkp_x] = 0
        self.lauta[ruutu[1]][ruutu[0]] = nappula
        pygame.sprite.spritecollide(nappula, self.mustat, True)

    def liiku_musta(self, nappula, ruutu):
        nappula.liikutettu = True
        alkp_x = int((0 + nappula.rect.x) / self.ruudun_koko)
        alkp_y = int((0 + nappula.rect.y) / self.ruudun_koko)
        self.lauta[alkp_y][alkp_x] = 0
        self.lauta[ruutu[1]][ruutu[0]] = nappula
        nappula.rect.x = ruutu[0] * self.ruudun_koko
        nappula.rect.y = ruutu[1] * self.ruudun_koko
        pygame.sprite.spritecollide(nappula, self.valkoiset, True)