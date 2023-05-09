import pygame

class Komennot:
    """luokka joka pitää huolta syötteiden komennoista
    """
    def __init__(self):
        """luokan konstruktori joka alustaa sanakirjan
        näppäimistön komennoista
        """
        self.komennot = self.alusta_komennot()     

    def alusta_komennot(self):
        """alustaa komennot sanakirjaan

        Returns:
            dict: näppäimistön syötteiden komennot
        """
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
        """nappulan valinta hiiren paikan perusteella

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
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
        """resetoi nappulan valinnan

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        silmukka.valittu_nappula = ""

    def torni_korotus(self, silmukka):
        """valitsee tornin korotuksen tulokseksi

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        silmukka.korotus = 2
        silmukka.m_korotus = 8
    
    def ratsu_korotus(self, silmukka):
        """valitsee ratsun korotuksen tulokseksi

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        silmukka.korotus = 3
        silmukka.m_korotus = 9

    def lahetti_korotus(self, silmukka):
        """valitsee lähetin korotuksen tulokseksi

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        silmukka.korotus = 4
        silmukka.m_korotus = 10

    def kuningatar_korotus(self, silmukka):
        """valitsee kuningattaren korotuksen tulokseksi

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        silmukka.korotus = 5
        silmukka.m_korotus = 11

    def kasvata_syvyytta(self, silmukka):
        """kasvattaa laskennan syvyyttä,
        mikäli syvyys on alle 7

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        if silmukka.syvyys < 7:
            silmukka.syvyys += 1

    def pienenna_syvyytta(self, silmukka):
        """pienentää laskennan syvyyttä,
        mikäli syvyys on yli 0

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        if silmukka.syvyys > 0:
            silmukka.syvyys -= 1

    def ai_paalle_pois(self, silmukka):
        """laittaa tekoälyn käyttöön/pois käytöstä

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        silmukka.tekoaly_kaytossa = not silmukka.tekoaly_kaytossa

    def suorita_komento(self, komento):
        """hakee komennon syötteen perusteella

        Args:
            komento (pygame.key): näppäimistön syöte

        Returns:
            method: jos syötettä vastaava komento sanakirjassa,
            palautetaan komento-metodi. Muuten palautetaan
            dummy-metodi
        """
        if komento in self.komennot:
            return self.komennot[komento]
        else:
            return self.dummy

    def dummy(self, silmukka):
        """Ei tee mitään. Välttää virhetilanteet
        komennon suorituksessa

        Args:
            silmukka (class): pelisilmukka joka kutsuu komentoa
        """
        pass