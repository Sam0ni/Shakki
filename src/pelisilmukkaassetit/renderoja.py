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


    def _renderoi(self):
        """Piirtää laudan ja spritet näytölle
        """
        self._naytto.blit(self.tausta, (0,0))
        for y in range(8): # pylint: disable=invalid-name
            for x in range(8): # pylint: disable=invalid-name
                ruutu = self._pelilauta.lauta[y][x]
                if ruutu != 0:
                    self._naytto.blit(self.spritet[ruutu],
                        (x*self._ruudun_koko,y*self._ruudun_koko))
        pygame.display.update()

    def _hae_spritet(self):
        """Hakee nappuloiden kuvat ja sijoittaa ne sanakirjaan
        """
        self.tausta = pygame.image.load(
            os.path.join(hakemisto, "..", "assetit_isommat", "shakkilauta.png")
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
