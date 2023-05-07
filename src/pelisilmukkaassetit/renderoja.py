import os
import pygame

hakemisto = os.path.dirname(__file__)

class Renderoja:
    def __init__(self, naytto, ruudun_koko, pelilauta):
        self._naytto = naytto
        self._ruudun_koko = ruudun_koko
        self._pelilauta = pelilauta
        self.spritet = None
        self._hae_spritet()
        self.tekstit = None
        self.alusta_tekstit()


    def _renderoi(self, valittu_nappula, korotus, voitto, voittaja):
        """Piirtää spritet näytölle

        Args:
            valittu_nappula (tuple): valitun nappulan koordinaatit
            korotus (int): nappula joksi korotetaan
            voitto (bool): Onko peli päättynyt
            voittaja (str): kumpi voitti
        """
        self._naytto.fill((0,0,0))
        self._naytto.blit(self.laudan_sivu, (1000,0))
        self._naytto.blit(self.tausta, (0,0))
        self._naytto.blit(self.tekstit[korotus], (8*self._ruudun_koko +35, 200))
        self._naytto.blit(self.tekstit["komennot"], (8*self._ruudun_koko +35, 350))
        self._naytto.blit(self.tekstit["korotus"], (8*self._ruudun_koko +35, 500))
        self._naytto.blit(self.tekstit["vaihto"], (8*self._ruudun_koko +35, 650))
        if valittu_nappula != "":
            self._naytto.blit(self.valittu, (valittu_nappula[2] * self._ruudun_koko + 1, valittu_nappula[1] * self._ruudun_koko + 1))
        for y in range(8): # pylint: disable=invalid-name
            for x in range(8): # pylint: disable=invalid-name
                ruutu = self._pelilauta.lauta[y][x]
                if ruutu != 0:
                    self._naytto.blit(self.spritet[ruutu],
                        (x*self._ruudun_koko,y*self._ruudun_koko))
        if voitto:
            self._naytto.blit(self.tekstit[voittaja], (2* self._ruudun_koko, 3* self._ruudun_koko))
        pygame.display.update()

    def _hae_spritet(self):
        """Hakee nappuloiden kuvat ja sijoittaa ne sanakirjaan
        """
        self.tausta = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "shakkilauta.png")
        )
        self.laudan_sivu = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "laudan_sivu.png")
        )
        self.valittu = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "valittu_rengas.png")
        )
        valkoinen_sotilas = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "valkoinen_sotilas.png")
        )
        valkoinen_torni = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "valkoinen_torni.png")
        )
        valkoinen_ratsu = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "valkoinen_ratsu.png")
        )
        valkoinen_lahetti = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "valkoinen_lähetti.png")
        )
        valkoinen_kuningatar = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "valkoinen_kuningatar.png")
        )
        valkoinen_kuningas = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "valkoinen_kuningas.png")
        )
        musta_sotilas = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "musta_sotilas.png")
        )
        musta_torni = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "musta_torni.png")
        )
        musta_ratsu = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "musta_ratsu.png")
        )
        musta_lahetti = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "musta_lähetti.png")
        )
        musta_kuningatar = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "musta_kuningatar.png")
        )
        musta_kuningas = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "musta_kuningas.png")
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

    def alusta_tekstit(self):
        fontti = pygame.font.Font('freesansbold.ttf', 40)
        fontti_isompi = pygame.font.Font('freesansbold.ttf', 100)
        vari = (0, 160, 80)
        tausta_vari = (0, 0, 190)
        self.tekstit = {
            "voitto_musta": fontti_isompi.render("Musta Voitti!", True, vari, tausta_vari),
            "voitto_valkoinen": fontti_isompi.render("Valkoinen Voitti!", True, vari, tausta_vari),
            2: fontti.render("Korotus = Torni", False, vari),
            3: fontti.render("Korotus = Ratsu", False, vari),
            4: fontti.render("Korotus = Lähetti", False, vari),
            5: fontti.render("Korotus = Kuningatar", False, vari),
            "komennot": fontti.render("Komennot:", False, vari),
            "korotus": fontti.render("Vaihda Korotus: 2-5", False, vari),
            "vaihto": fontti.render("Vaihda nappulaa: D", False, vari)
        }