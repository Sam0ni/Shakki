import os
import pygame
import copy
from minimax import Minimax


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
        self.mahdolliset_liikkeet = []
        self.edessa = []
        self.tekoaly = tekoaly
        self.tekoaly_kaytossa = tekoaly_kaytossa
        self.v_voitto = False
        self.m_voitto = False

    def aloita(self):
        """Aloittaa pelisilmukan, ja tarkistaa aluksi valkoisen mahdolliset liikkeet
        """
        self.mahdolliset_liikkeet, self.edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = self._pelilauta.alusta()
        while True:
            if self._syotteet() is False:
                break

            if self.v_voitto:
                self._renderoja._renderoi(self.valittu_nappula, self.korotus, True, "voitto_valkoinen")
            elif self.m_voitto:
                self._renderoja._renderoi(self.valittu_nappula, self.korotus, True, "voitto_musta")
            else:
                self._renderoja._renderoi(self.valittu_nappula, self.korotus, False, None)


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
                x, y = pygame.mouse.get_pos()
                x = x // self._ruudun_koko # pylint: disable=invalid-name
                y = y // self._ruudun_koko # pylint: disable=invalid-name
                if x > 7 or y > 7:
                    continue
                if self.valittu_nappula == "":
                    if self._pelilauta.lauta[y][x] != 0:
                        self.valitse_nappula(y, x)
                else:
                    self.validoi_liike(y, x)
            elif syote.type == pygame.KEYDOWN: # pylint: disable=no-member
                if syote.key == pygame.K_d: # pylint: disable=no-member
                    self.valittu_nappula = ""
                elif syote.key == pygame.K_2:
                    self.korotus = 2
                elif syote.key == pygame.K_3:
                    self.korotus = 3
                elif syote.key == pygame.K_4:
                    self.korotus = 4
                elif syote.key == pygame.K_5:
                    self.korotus = 5
            elif syote.type == pygame.QUIT: # pylint: disable=no-member
                return False

    def tekoalyn_vuoro(self):
        kopio_lauta = copy.deepcopy(self._pelilauta.lauta)
        liike = self.tekoaly.aloita(kopio_lauta, self.mahdolliset_liikkeet, self.edessa, 2)
        liikkeet = self._pelilauta.liiku(liike[0],
            liike[1], self.mahdolliset_liikkeet, self.edessa)
        uudet_mahdolliset_liikkeet = liikkeet[0]
        uudet_edessa = liikkeet[1]
        self.mahdolliset_liikkeet = uudet_mahdolliset_liikkeet
        self.edessa = uudet_edessa
        self.vuoro_valkoinen = not self.vuoro_valkoinen
        self.matin_tarkistus(liikkeet[2], liikkeet[3], liikkeet[4], liikkeet[5])

    def valitse_nappula(self, y, x):
        if self._pelilauta.lauta[y][x] != 0:
            if self.vuoro_valkoinen:
                if 1 <= self._pelilauta.lauta[y][x] <= 6:
                    self.valittu_nappula = (self._pelilauta.lauta[y][x], y, x)
            else:
                if 7 <= self._pelilauta.lauta[y][x] <= 12:
                    self.valittu_nappula = (self._pelilauta.lauta[y][x], y, x)

    def validoi_liike(self, y, x):
        if ((self.valittu_nappula, (self.valittu_nappula[0], y, x))
                    in self.mahdolliset_liikkeet):
            liikkeet = self._pelilauta.liiku(self.valittu_nappula,
                (self.valittu_nappula[0], y, x), self.mahdolliset_liikkeet, self.edessa)
            uudet_mahdolliset_liikkeet = liikkeet[0]
            uudet_edessa = liikkeet[1]
            self.mahdolliset_liikkeet = uudet_mahdolliset_liikkeet
            self.edessa = uudet_edessa
            self.vuoro_valkoinen = not self.vuoro_valkoinen
            self.valittu_nappula = ""
            self.matin_tarkistus(liikkeet[2], liikkeet[3], liikkeet[4], liikkeet[5])
        elif ((self.valittu_nappula, (self.korotus, y, x))
                    in self.mahdolliset_liikkeet):
            liikkeet = self._pelilauta.liiku(self.valittu_nappula,
                (self.korotus, y, x), self.mahdolliset_liikkeet, self.edessa)
            uudet_mahdolliset_liikkeet = liikkeet[0]
            uudet_edessa = liikkeet[1]
            self.mahdolliset_liikkeet = uudet_mahdolliset_liikkeet
            self.edessa = uudet_edessa
            self.vuoro_valkoinen = not self.vuoro_valkoinen
            self.valittu_nappula = ""
            self.matin_tarkistus(liikkeet[2], liikkeet[3], liikkeet[4], liikkeet[5])

    def matin_tarkistus(self, v_shakissa, m_shakissa, v_shakkaajat, m_shakkaajat):
        if v_shakissa:
            if not self.vuoro_valkoinen:
                self.m_voitto = True
                return
            if self._pelilauta.tarkista_matti(self.mahdolliset_liikkeet, self.edessa, True, v_shakkaajat):
                self.m_voitto = True
                return
        elif m_shakissa:
            if self.vuoro_valkoinen:
                self.v_voitto = True
                return
            if self._pelilauta.tarkista_matti(self.mahdolliset_liikkeet, self.edessa, False, m_shakkaajat):
                self.v_voitto = True
                return
