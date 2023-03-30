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
        self.edessa = []
        self.tausta = ""
        self.spritet = {}
        self._hae_spritet()
        

    def aloita(self):
        """Aloittaa pelisilmukan, ja tarkistaa aluksi valkoisen mahdolliset liikkeet
        """
        for y in range(8):
            for x in range(8):
                uudet_liikkeet, uudet_edessa = self._pelilauta.tarkista_liikkeet(self._pelilauta.lauta[y][x], y, x)
                self.mahdolliset_liikkeet = self.mahdolliset_liikkeet + uudet_liikkeet
                self.edessa = self.edessa + uudet_edessa
        print(len(self.mahdolliset_liikkeet))
        print(len(self.edessa))
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
                            #print("mrhelloust")
                            if 1 <= self._pelilauta.lauta[y][x] <= 6:
                                self.valittu_nappula = (self._pelilauta.lauta[y][x], y, x)
                        else:
                            if 7 <= self._pelilauta.lauta[y][x] <= 12:
                                self.valittu_nappula = (self._pelilauta.lauta[y][x], y, x)
                else:
                    if (self.valittu_nappula, (self.valittu_nappula[0], y, x)) in self.mahdolliset_liikkeet:
                        #print("5/5")
                        uudet_mahdolliset_liikkeet, uudet_edessa = self._pelilauta.liiku(self.valittu_nappula, (self.valittu_nappula[0], y, x), self.mahdolliset_liikkeet, self.edessa)
                        self.mahdolliset_liikkeet = uudet_mahdolliset_liikkeet
                        self.edessa = uudet_edessa
                        self.mahdolliset_liikkeet, self.edessa = self._pelilauta.paivita(self.mahdolliset_liikkeet, self.edessa, self.valittu_nappula, (self.valittu_nappula[0], y, x))
                        self.vuoro_valkoinen = not self.vuoro_valkoinen
                        self.valittu_nappula = ""
                        print("")
                        print("")
                        print("")
                        print("")
                        for i in self.mahdolliset_liikkeet:
                            print(i)
                        #print(self.mahdolliset_liikkeet)
                        print("")
                        print("")
                        print("")
                        print("")
                        #print(self.edessa)
                        for i in self.edessa:
                            print(i)
                        print(len(self.mahdolliset_liikkeet))
                        print(len(self.edessa))
                        #for liike in self.edessa:
                        #    print(liike[0])
            elif syote.type == pygame.KEYDOWN:
                if syote.key == pygame.K_d:
                    self.valittu_nappula = ""
            elif syote.type == pygame.QUIT:
                return False

    def _renderoi(self):
        """Piirtää laudan ja spritet näytölle
        """
        self._naytto.blit(self.tausta, (0,0))
        for y in range(8):
            for x in range(8):
                ruutu = self._pelilauta.lauta[y][x]
                if ruutu != 0:
                    self._naytto.blit(self.spritet[ruutu], (x*self._ruudun_koko,y*self._ruudun_koko))
        pygame.display.update()

    def _hae_spritet(self):
        self.tausta = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "shakkilauta.png")
        )
        valkoinen_sotilas = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "valkoinen_sotilas.png")
        )
        valkoinen_torni = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "valkoinen_torni.png")
        )
        valkoinen_ratsu = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "valkoinen_ratsu.png")
        )
        valkoinen_lahetti = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "valkoinen_lähetti.png")
        )
        valkoinen_kuningatar = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "valkoinen_kuningatar.png")
        )
        valkoinen_kuningas = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "valkoinen_kuningas.png")
        )
        musta_sotilas = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "musta_sotilas.png")
        )
        musta_torni = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "musta_torni.png")
        )
        musta_ratsu = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "musta_ratsu.png")
        )
        musta_lahetti = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "musta_lähetti.png")
        )
        musta_kuningatar = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "musta_kuningatar.png")
        )
        musta_kuningas = pygame.image.load(
            os.path.join(hakemisto, "assetit_isommat", "musta_kuningas.png")
        )

        self.spritet = {
            1:valkoinen_sotilas,
            2:valkoinen_torni,
            3:valkoinen_ratsu,
            4:valkoinen_lahetti,
            5:valkoinen_kuningatar,
            6:valkoinen_kuningas,
            7:musta_sotilas,
            8:musta_torni,
            9:musta_ratsu,
            10:musta_lahetti,
            11:musta_kuningatar,
            12:musta_kuningas
        }