import pygame
import os

hakemisto = os.path.dirname(__file__)

class Pelisilmukka:
    def __init__(self, pelilauta, ruudun_koko, naytto):
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
            os.path.join(hakemisto, "assetit", "shakkilauta.png")
        )

    def aloita(self):
        self.mahdolliset_liikkeet = self._pelilauta.tarkista_liikkeet_valkoinen()
        while True:
            if self._syotteet() == False:
                break
            
            self._renderoi()
            
            self._kello.tick(60)

    def _syotteet(self):
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
            elif syote.type == pygame.QUIT:
                return False

    def _renderoi(self):
        self._naytto.blit(self.tausta, (0,0))
        self._pelilauta.kaikki_spritet.draw(self._naytto)
        pygame.display.update()

    
