import os
import pygame
import copy
from pelisilmukkaassetit.komennot import Komennot


hakemisto = os.path.dirname(__file__)

class Pelisilmukka:
    """Luokka joka pitää huolta aikaan sidotuista tapahtumista
    """
    def __init__(self, pelilauta, ruudun_koko, renderoja, kello, syotteiden_hakija, tekoaly_kaytossa, tekoaly): # pylint: disable=too-many-instance-attributes
        """Luokan konstruktori, jossa määritellään tarvittavat muuttujat

        Args:
            pelilauta: sisältää pelilaudan senhetkisen tilaanteen
              ja tarvittavat metodit liikkumiselle
            ruudun_koko: Yhden laudan ruudun koko
            naytto: naytto johon lauta ja spritet piirretään
        """
        self._pelilauta = pelilauta
        self._kello = kello
        self._ruudun_koko = ruudun_koko
        self._renderoja = renderoja
        self._syotteiden_hakija = syotteiden_hakija
        self.valittu_nappula = ""
        self.vuoro_valkoinen = True
        self.korotus = 5
        self.m_korotus = 11
        self.mahdolliset_liikkeet = []
        self.edessa = []
        self.tekoaly = tekoaly
        self.tekoaly_kaytossa = tekoaly_kaytossa
        self.syvyys = 2
        self.v_voitto = False
        self.m_voitto = False
        self.komennot = Komennot()

    def aloita(self):
        """Aloittaa pelisilmukan, ja tarkistaa aluksi mahdolliset liikkeet
        """
        self.mahdolliset_liikkeet, self.edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = self._pelilauta.alusta()
        while True:
            if self._syotteet() is False:
                break

            if self.v_voitto:
                self._renderoja._renderoi(self.valittu_nappula, self.korotus, True, "voitto_valkoinen", self.syvyys, self.tekoaly_kaytossa)
            elif self.m_voitto:
                self._renderoja._renderoi(self.valittu_nappula, self.korotus, True, "voitto_musta", self.syvyys, self.tekoaly_kaytossa)
            else:
                self._renderoja._renderoi(self.valittu_nappula, self.korotus, False, None, self.syvyys, self.tekoaly_kaytossa)


            self._kello.tick(60)

            if not self.vuoro_valkoinen and self.tekoaly_kaytossa and not self.v_voitto and not self.m_voitto:
                self.tekoalyn_vuoro()

    def _syotteet(self):
        """Tarkistaa hiiren ja näppäimistön syötteet.

        Returns:
            False: Peli suljetaan
        """
        for syote in self._syotteiden_hakija.hae():
            if self.v_voitto or self.m_voitto:
                if syote.type == pygame.QUIT:
                    return False
                continue
            if syote.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                self.komennot.valinta_komento(self)
            elif syote.type == pygame.KEYDOWN: # pylint: disable=no-member
                self.komennot.suorita_komento(syote.key)(self)
            elif syote.type == pygame.QUIT: # pylint: disable=no-member
                return False

    def tekoalyn_vuoro(self):
        """Kutsuu minimaxia ja liikuttaa sen palauttaman liikkeen
        """
        kopio_lauta = copy.deepcopy(self._pelilauta.lauta)
        liike = self.tekoaly.aloita(kopio_lauta, self.mahdolliset_liikkeet, self.edessa, self.syvyys)
        if liike == "stalemate":
            pass
        if self._pelilauta.lauta[liike[1][1]][liike[1][2]] == 6:
            self.m_voitto = True
        liikkeet = self._pelilauta.liiku(liike[0],
            liike[1], self.mahdolliset_liikkeet, self.edessa)
        uudet_mahdolliset_liikkeet = liikkeet[0]
        uudet_edessa = liikkeet[1]
        self.mahdolliset_liikkeet = uudet_mahdolliset_liikkeet
        self.edessa = uudet_edessa
        self.vuoro_valkoinen = not self.vuoro_valkoinen
        if not self.m_voitto:
            self.matin_tarkistus(liikkeet[2], liikkeet[3], liikkeet[4], liikkeet[5])

    def valitse_nappula(self, y, x):
        """valitsee nappulan, mikäli hiiren x- ja y-koordinaatit ovat kelvolliset

        Args:
            y (int): hiiren y-koordinaatti
            x (int): hiiren x-koordinaatti
        """
        if self._pelilauta.lauta[y][x] == 0:
            return
        if self.vuoro_valkoinen:
            if 1 <= self._pelilauta.lauta[y][x] <= 6:
                self.valittu_nappula = (self._pelilauta.lauta[y][x], y, x)
        else:
            if 7 <= self._pelilauta.lauta[y][x] <= 12:
                self.valittu_nappula = (self._pelilauta.lauta[y][x], y, x)

    def validoi_liike(self, y, x):
        """tarkistaa onko liike kelvollinen ja liikuttaa mikäli on

        Args:
            y (int): hiiren y-koordinaatti
            x (int): hiiren x-koordinaatti
        """
        if ((self.valittu_nappula, (self.valittu_nappula[0], y, x))
                    in self.mahdolliset_liikkeet):
            if not self.tarkista_liikkeen_laillisuus(self.valittu_nappula, (self.valittu_nappula[0], y, x)):
                return
            if self._pelilauta.lauta[y][x] in (6, 12):
                if self.vuoro_valkoinen:
                    self.v_voitto = True
                else:
                    self.m_voitto = True
            liikkeet = self._pelilauta.liiku(self.valittu_nappula,
                (self.valittu_nappula[0], y, x), self.mahdolliset_liikkeet, self.edessa)
            uudet_mahdolliset_liikkeet = liikkeet[0]
            uudet_edessa = liikkeet[1]
            self.mahdolliset_liikkeet = uudet_mahdolliset_liikkeet
            self.edessa = uudet_edessa
            self.vuoro_valkoinen = not self.vuoro_valkoinen
            self.valittu_nappula = ""
            if not self.v_voitto and not self.m_voitto:
                self.matin_tarkistus(liikkeet[2], liikkeet[3], liikkeet[4], liikkeet[5])
        elif ((self.valittu_nappula, (self.korotus, y, x))
                    in self.mahdolliset_liikkeet):
            if self._pelilauta.lauta[y][x] in (6, 12):
                if self.vuoro_valkoinen:
                    self.v_voitto = True
                else:
                    self.m_voitto = True
            liikkeet = self._pelilauta.liiku(self.valittu_nappula,
                (self.korotus, y, x), self.mahdolliset_liikkeet, self.edessa)
            uudet_mahdolliset_liikkeet = liikkeet[0]
            uudet_edessa = liikkeet[1]
            self.mahdolliset_liikkeet = uudet_mahdolliset_liikkeet
            self.edessa = uudet_edessa
            self.vuoro_valkoinen = not self.vuoro_valkoinen
            self.valittu_nappula = ""
            if not self.v_voitto and not self.m_voitto:
                self.matin_tarkistus(liikkeet[2], liikkeet[3], liikkeet[4], liikkeet[5])

    def matin_tarkistus(self, v_shakissa, m_shakissa, v_shakkaajat, m_shakkaajat):
        """tarkistaa onko shakkimatti

        Args:
            v_shakissa (bool): valkoinen kuningas shakissa
            m_shakissa (bool): musta kuningas shakissa
            v_shakkaajat (list): nappulat jotka uhkaavat valkoista kuningasta
            m_shakkaajat (list): nappulat jotka uhkaavat mustaa kuningasta
        """
        if v_shakissa and self._pelilauta.tarkista_matti(self.mahdolliset_liikkeet, self.edessa, True, v_shakkaajat):
                self.m_voitto = True
                return
        elif m_shakissa and self._pelilauta.tarkista_matti(self.mahdolliset_liikkeet, self.edessa, False, m_shakkaajat):
                self.v_voitto = True
                return

    def tarkista_liikkeen_laillisuus(self, alku, loppu):
        kopio_lauta = copy.deepcopy(self._pelilauta.lauta)
        liikkeet = self._pelilauta.liiku(alku,
            loppu, self.mahdolliset_liikkeet, self.edessa)
        if self.vuoro_valkoinen:
            for liike in liikkeet[0]:
                if self._pelilauta.lauta[liike[1][1]][liike[1][2]] == 6:
                    self._pelilauta.lauta = copy.deepcopy(kopio_lauta)
                    return False
        else:
            for liike in liikkeet[0]:
                if self._pelilauta.lauta[liike[1][1]][liike[1][2]] == 12:
                    self._pelilauta.lauta = copy.deepcopy(kopio_lauta)
                    return False
        self._pelilauta.lauta = copy.deepcopy(kopio_lauta)
        return True
