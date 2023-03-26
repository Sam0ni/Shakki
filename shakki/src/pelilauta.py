import pygame
from spritet.sotilas import Sotilas
from spritet.torni import Torni
from spritet.ratsu import Ratsu
from spritet.lahetti import Lahetti


class Pelilauta:
    """Luokka joka pitää huolta pelilaudan tilanteesta
    """
    def __init__(self, lauta, ruudun_koko, alustaja):
        """Luokan konstruktori, jossa määritellään tarvittavat muuttujat ja spritejen ryhmät

        Args:
            lauta: 2-ulotteinen taulukko joka kuvaa pelilautaa
            ruudun_koko: Yhden pelilaudan ruudun koko
            alustaja: Luokka jossa on metodi pelilaudan alustamiselle
        """
        self.lauta = lauta
        self.ruudun_koko = ruudun_koko
        self.alustaja = alustaja
        self.mustat_sotilaat = ""
        self.mustat_tornit = ""
        self.mustat_ratsut = ""
        self.mustat_lahetit = ""
        self.mustat = pygame.sprite.Group()
        self.valkoiset_sotilaat = ""
        self.valkoiset_tornit = ""
        self.valkoiset_ratsut = ""
        self.valkoiset_lahetit = ""
        self.valkoiset = pygame.sprite.Group()
        self.kaikki_spritet = pygame.sprite.Group()
        self._alusta_spritet()

    def _alusta_spritet(self):
        """Metodi joka kutsuu alustajaa, ja määrittää spritejen ryhmät oikeiksi
        """
        spritet = self.alustaja.alusta_spritet(self.lauta)

        self.mustat_sotilaat = spritet[0]
        self.mustat_tornit = spritet[1]
        self.mustat_ratsut = spritet[2]
        self.mustat_lahetit = spritet[3]
        self.valkoiset_sotilaat = spritet[4]
        self.valkoiset_tornit = spritet[5]
        self.valkoiset_ratsut = spritet[6]
        self.valkoiset_lahetit = spritet[7]

        self.mustat.add(
            self.mustat_sotilaat,
            self.mustat_tornit,
            self.mustat_ratsut,
            self.mustat_lahetit
        )
        self.valkoiset.add(
            self.valkoiset_sotilaat,
            self.valkoiset_tornit,
            self.valkoiset_ratsut,
            self.valkoiset_lahetit
        )
        self.kaikki_spritet.add(
            self.mustat_sotilaat,
            self.mustat_tornit,
            self.mustat_ratsut,
            self.mustat_lahetit,
            self.valkoiset_sotilaat,
            self.valkoiset_tornit,
            self.valkoiset_ratsut,
            self.valkoiset_lahetit
        )

    def tarkista_liikkeet_valkoinen(self):
        """Tarkistaa kaikki mahdolliset liikkeet jotka valkoinen voi tehdä senhetkisessä tilanteessa

        Returns:
            List: Siäsltää kaikki mahdolliset liikkeet tupleina jossa on nappula ja loppusijainti
        """
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

        for ratsu in self.valkoiset_ratsut:
            alkup_x = 0 + ratsu.rect.x
            alkup_y = 0 + ratsu.rect.y
            if alkup_y - 2*self.ruudun_koko >=0:
                ratsu.rect.move_ip(0, -self.ruudun_koko * 2)
                if alkup_x + self.ruudun_koko <= 7*self.ruudun_koko:
                    ratsu.rect.move_ip(self.ruudun_koko, 0)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or not self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                    ratsu.rect.move_ip(-self.ruudun_koko, 0)
                if alkup_x - self.ruudun_koko >= 0:
                    ratsu.rect.move_ip(-self.ruudun_koko, 0)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or not self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                ratsu.rect.x = alkup_x
                ratsu.rect.y = alkup_y
            if alkup_y + 2*self.ruudun_koko <= self.ruudun_koko * 7:
                ratsu.rect.move_ip(0, self.ruudun_koko * 2)
                if alkup_x + self.ruudun_koko <= 7*self.ruudun_koko:
                    ratsu.rect.move_ip(self.ruudun_koko, 0)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or not self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                    ratsu.rect.move_ip(-self.ruudun_koko, 0)
                if alkup_x - self.ruudun_koko >= 0:
                    ratsu.rect.move_ip(-self.ruudun_koko, 0)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or not self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                ratsu.rect.x = alkup_x
                ratsu.rect.y = alkup_y
            if alkup_x - 2*self.ruudun_koko >=0:
                ratsu.rect.move_ip(-self.ruudun_koko * 2, 0)
                if alkup_y + self.ruudun_koko <= 7*self.ruudun_koko:
                    ratsu.rect.move_ip(0, self.ruudun_koko)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or not self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                    ratsu.rect.move_ip(0, -self.ruudun_koko)
                if alkup_y - self.ruudun_koko >= 0:
                    ratsu.rect.move_ip(0, -self.ruudun_koko)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or not self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                ratsu.rect.x = alkup_x
                ratsu.rect.y = alkup_y
            if alkup_x + 2*self.ruudun_koko <=7*self.ruudun_koko:
                ratsu.rect.move_ip(self.ruudun_koko * 2, 0)
                if alkup_y + self.ruudun_koko <= 7*self.ruudun_koko:
                    ratsu.rect.move_ip(0, self.ruudun_koko)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or not self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                    ratsu.rect.move_ip(0, -self.ruudun_koko)
                if alkup_y - self.ruudun_koko >= 0:
                    ratsu.rect.move_ip(0, -self.ruudun_koko)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or not self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                ratsu.rect.x = alkup_x
                ratsu.rect.y = alkup_y

        for lahetti in self.valkoiset_lahetit:
            alkup_x = 0 + lahetti.rect.x
            alkup_y = 0 + lahetti.rect.y
            if alkup_x < alkup_y:
                ruutujen_maara = int(alkup_x / self.ruudun_koko)
            else:
                ruutujen_maara = int(alkup_y / self.ruudun_koko)
            for i in range(ruutujen_maara, 0, -1):
                lahetti.rect.move_ip(-self.ruudun_koko, -self.ruudun_koko)
                if self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                elif not self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
                else:
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
            lahetti.rect.x = alkup_x
            lahetti.rect.y = alkup_y
            if 7*self.ruudun_koko - alkup_x < alkup_y:
                ruutujen_maara = int((7*self.ruudun_koko - alkup_x) / self.ruudun_koko)
            else:
                ruutujen_maara = int(alkup_y / self.ruudun_koko)
            for i in range(ruutujen_maara, 0, -1):
                lahetti.rect.move_ip(self.ruudun_koko, -self.ruudun_koko)
                if self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                elif not self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
                else:
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
            lahetti.rect.x = alkup_x
            lahetti.rect.y = alkup_y
            if alkup_x < 7*self.ruudun_koko - alkup_y:
                ruutujen_maara = int(alkup_x / self.ruudun_koko)
            else:
                ruutujen_maara = int((7*self.ruudun_koko - alkup_y) / self.ruudun_koko)
            for i in range(ruutujen_maara, 0, -1):
                lahetti.rect.move_ip(-self.ruudun_koko, self.ruudun_koko)
                if self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                elif not self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
                else:
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
            lahetti.rect.x = alkup_x
            lahetti.rect.y = alkup_y
            if alkup_x > alkup_y:
                ruutujen_maara = int(alkup_x / self.ruudun_koko)
            else:
                ruutujen_maara = int(alkup_y / self.ruudun_koko)
            for i in range(ruutujen_maara, 7):
                lahetti.rect.move_ip(self.ruudun_koko, self.ruudun_koko)
                if self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                elif not self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
                else:
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
            lahetti.rect.x = alkup_x
            lahetti.rect.y = alkup_y
            
        return mahdolliset_liikkeet

    def tarkista_liikkeet_musta(self):
        """Tarkistaa kaikki mahdolliset liikkeet jotka valkoinen voi tehdä senhetkisessä tilanteessa

        Returns:
            List: Siäsltää kaikki mahdolliset liikkeet tupleina jossa on nappula ja loppusijainti
        """
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
                    sotilas.rect.move_ip(0, -self.ruudun_koko)
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

        for ratsu in self.mustat_ratsut:
            alkup_x = 0 + ratsu.rect.x
            alkup_y = 0 + ratsu.rect.y
            if alkup_y - 2*self.ruudun_koko >=0:
                ratsu.rect.move_ip(0, -self.ruudun_koko * 2)
                if alkup_x + self.ruudun_koko <= 7*self.ruudun_koko:
                    ratsu.rect.move_ip(self.ruudun_koko, 0)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                    ratsu.rect.move_ip(-self.ruudun_koko, 0)
                if alkup_x - self.ruudun_koko >= 0:
                    ratsu.rect.move_ip(-self.ruudun_koko, 0)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                ratsu.rect.x = alkup_x
                ratsu.rect.y = alkup_y
            if alkup_y + 2*self.ruudun_koko <= self.ruudun_koko * 7:
                ratsu.rect.move_ip(0, self.ruudun_koko * 2)
                if alkup_x + self.ruudun_koko <= 7*self.ruudun_koko:
                    ratsu.rect.move_ip(self.ruudun_koko, 0)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                    ratsu.rect.move_ip(-self.ruudun_koko, 0)
                if alkup_x - self.ruudun_koko >= 0:
                    ratsu.rect.move_ip(-self.ruudun_koko, 0)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                ratsu.rect.x = alkup_x
                ratsu.rect.y = alkup_y
            if alkup_x - 2*self.ruudun_koko >=0:
                ratsu.rect.move_ip(-self.ruudun_koko * 2, 0)
                if alkup_y + self.ruudun_koko <= 7*self.ruudun_koko:
                    ratsu.rect.move_ip(0, self.ruudun_koko)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                    ratsu.rect.move_ip(0, -self.ruudun_koko)
                if alkup_y - self.ruudun_koko >= 0:
                    ratsu.rect.move_ip(0, -self.ruudun_koko)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                ratsu.rect.x = alkup_x
                ratsu.rect.y = alkup_y
            if alkup_x + 2*self.ruudun_koko <=7*self.ruudun_koko:
                ratsu.rect.move_ip(self.ruudun_koko * 2, 0)
                if alkup_y + self.ruudun_koko <= 7*self.ruudun_koko:
                    ratsu.rect.move_ip(0, self.ruudun_koko)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                    ratsu.rect.move_ip(0, -self.ruudun_koko)
                if alkup_y - self.ruudun_koko >= 0:
                    ratsu.rect.move_ip(0, -self.ruudun_koko)
                    if self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)] == 0 or self.lauta[int(ratsu.rect.y / self.ruudun_koko)][int(ratsu.rect.x / self.ruudun_koko)].valkoinen:
                        mahdolliset_liikkeet.append((ratsu, (int(ratsu.rect.x / self.ruudun_koko), int(ratsu.rect.y / self.ruudun_koko))))
                ratsu.rect.x = alkup_x
                ratsu.rect.y = alkup_y

        for lahetti in self.mustat_lahetit:
            alkup_x = 0 + lahetti.rect.x
            alkup_y = 0 + lahetti.rect.y
            if alkup_x < alkup_y:
                ruutujen_maara = int(alkup_x / self.ruudun_koko)
            else:
                ruutujen_maara = int(alkup_y / self.ruudun_koko)
            for i in range(ruutujen_maara, 0, -1):
                lahetti.rect.move_ip(-self.ruudun_koko, -self.ruudun_koko)
                if self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                elif self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
                else:
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
            lahetti.rect.x = alkup_x
            lahetti.rect.y = alkup_y
            if 7*self.ruudun_koko - alkup_x < alkup_y:
                ruutujen_maara = int((7*self.ruudun_koko - alkup_x) / self.ruudun_koko)
            else:
                ruutujen_maara = int(alkup_y / self.ruudun_koko)
            for i in range(ruutujen_maara, 0, -1):
                lahetti.rect.move_ip(self.ruudun_koko, -self.ruudun_koko)
                if self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                elif self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
                else:
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
            lahetti.rect.x = alkup_x
            lahetti.rect.y = alkup_y
            if alkup_x < 7*self.ruudun_koko - alkup_y:
                ruutujen_maara = int(alkup_x / self.ruudun_koko)
            else:
                ruutujen_maara = int((7*self.ruudun_koko - alkup_y) / self.ruudun_koko)
            for i in range(ruutujen_maara, 0, -1):
                lahetti.rect.move_ip(-self.ruudun_koko, self.ruudun_koko)
                if self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                elif self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
                else:
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
            lahetti.rect.x = alkup_x
            lahetti.rect.y = alkup_y
            if alkup_x > alkup_y:
                ruutujen_maara = int(alkup_x / self.ruudun_koko)
            else:
                ruutujen_maara = int(alkup_y / self.ruudun_koko)
            for i in range(ruutujen_maara, 7):
                lahetti.rect.move_ip(self.ruudun_koko, self.ruudun_koko)
                if self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)] == 0:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                elif self.lauta[int(lahetti.rect.y / self.ruudun_koko)][int(lahetti.rect.x / self.ruudun_koko)].valkoinen:
                    mahdolliset_liikkeet.append((lahetti, (int(lahetti.rect.x / self.ruudun_koko), int(lahetti.rect.y / self.ruudun_koko))))
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
                else:
                    lahetti.rect.x = alkup_x
                    lahetti.rect.y = alkup_y
                    break
            lahetti.rect.x = alkup_x
            lahetti.rect.y = alkup_y
            
        return mahdolliset_liikkeet

    def liiku_valkoinen(self, nappula, ruutu):
        """Liikuttaa valkoista nappulaa laudalla, ja mikäli törmäys tulee mustan nappulan kanssa, poistaa sen.

        Args:
            nappula: Liikutettava nappula
            ruutu: Loppusijainti 
        """
        nappula.liikutettu = True
        alkp_x = int((0 + nappula.rect.x) / self.ruudun_koko)
        alkp_y = int((0 + nappula.rect.y) / self.ruudun_koko)
        nappula.rect.x = ruutu[0] * self.ruudun_koko
        nappula.rect.y = ruutu[1] * self.ruudun_koko
        self.lauta[alkp_y][alkp_x] = 0
        self.lauta[ruutu[1]][ruutu[0]] = nappula
        pygame.sprite.spritecollide(nappula, self.mustat, True)

    def liiku_musta(self, nappula, ruutu):
        """Liikuttaa mustaa nappulaa laudalla, ja mikäli törmäys tulee valkoisen nappulan kanssa, poistaa sen.

        Args:
            nappula: Liikutettava nappula
            ruutu: Loppusijainti 
        """
        nappula.liikutettu = True
        alkp_x = int((0 + nappula.rect.x) / self.ruudun_koko)
        alkp_y = int((0 + nappula.rect.y) / self.ruudun_koko)
        self.lauta[alkp_y][alkp_x] = 0
        self.lauta[ruutu[1]][ruutu[0]] = nappula
        nappula.rect.x = ruutu[0] * self.ruudun_koko
        nappula.rect.y = ruutu[1] * self.ruudun_koko
        pygame.sprite.spritecollide(nappula, self.valkoiset, True)
