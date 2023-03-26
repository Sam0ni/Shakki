import pygame
import os

hakemisto = os.path.dirname(__file__)

class Pelisilmukka:
    """Luokka joka pitää huolta aikaan sidotuista tapahtumista
    """
    def __init__(self, pelilauta, ruudun_koko, naytto):
        """Luokan konstruktori, jossa määritellään tarvittavat muuttujat

        Args:
            pelilauta: sisältää pelilaudan senhetkisen tilaanteen ja tarvittavat metodit liikkumiselle
            ruudun_koko: Yhden laudan ruudun koko
            naytto: naytto johon lauta ja spritet piirretään
        """
        self._pelilauta = pelilauta
        self._kello = pygame.time.Clock()
        self._ruudun_koko = ruudun_koko
        self._naytto = naytto
        self.hiiri_x = 0
        self.hiiri_y = 0
        self.valittu_nappula = ""
        self.vuoro_valkoinen = True
        self.mahdolliset_liikkeet = []
        self.tausta = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "shakkilauta.png")
        )

    def aloita(self):
        """Aloittaa pelisilmukan, ja tarkistaa aluksi valkoisen mahdolliset liikkeet
        """
        self.mahdolliset_liikkeet = self._pelilauta.tarkista_liikkeet_valkoinen()
        while True:
            if self._syotteet() == False:
                break
            
            self._renderoi()
            
            self._kello.tick(60)

    def _syotteet(self):
        """Tarkistaa hiiren ja näppäimistön syötteet.

        Returns:
            False: Peli suljetaan
        """
        for syote in pygame.event.get():
            if syote.type == pygame.MOUSEBUTTONDOWN:
                self.hiiri_x, self.hiiri_y = pygame.mouse.get_pos()
                x = self.hiiri_x // self._ruudun_koko
                y = self.hiiri_y // self._ruudun_koko
                if self.valittu_nappula == "":
                    if self._pelilauta.lauta[y][x] != 0:
                        if self.vuoro_valkoinen:
                            if self._pelilauta.lauta[y][x].valkoinen:
                                self.valittu_nappula = self._pelilauta.lauta[y][x]
                        else:
                            if not self._pelilauta.lauta[y][x].valkoinen:
                                self.valittu_nappula = self._pelilauta.lauta[y][x]
                else:
                    if (self.valittu_nappula, (x, y)) in self.mahdolliset_liikkeet:
                        if self.valittu_nappula.valkoinen:
                            self._pelilauta.liiku_valkoinen(self.valittu_nappula, (x, y))
                            self.mahdolliset_liikkeet = self._pelilauta.tarkista_liikkeet_musta()
                            self.vuoro_valkoinen = False
                        else:
                            self._pelilauta.liiku_musta(self.valittu_nappula, (x, y))
                            self.mahdolliset_liikkeet = self._pelilauta.tarkista_liikkeet_valkoinen()
                            self.vuoro_valkoinen = True
                        self.valittu_nappula = ""
            elif syote.type == pygame.KEYDOWN:
                if syote.key == pygame.K_d:
                    self.valittu_nappula = ""
            elif syote.type == pygame.QUIT:
                return False

    def _renderoi(self):
        """Piirtää laudan ja spritet näytölle
        """
        self._naytto.blit(self.tausta, (0,0))
        self._pelilauta.kaikki_spritet.draw(self._naytto)
        pygame.display.update()

    
