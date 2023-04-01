import pygame
from pelilauta import Pelilauta
from pelisilmukka import Pelisilmukka

lauta = [[8,9,10,11,12,10,9,8],
[7,7,7,7,7,7,7,7],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1],
[2,3,4,5,6,4,3,2]]

Ruudun_Koko = 125 # pylint: disable=invalid-name

def main():
    """alustaa näytön, pelilaudan ja aloittaa pelisilmukan
    """
    nayton_korkeus_ja_leveys = 8*Ruudun_Koko

    naytto = pygame.display.set_mode((nayton_korkeus_ja_leveys, nayton_korkeus_ja_leveys))

    pygame.display.set_caption("Shakki")

    pelilauta = Pelilauta(lauta, Ruudun_Koko)

    silmukka = Pelisilmukka(pelilauta, Ruudun_Koko, naytto)

    pygame.init() # pylint: disable=no-member
    silmukka.aloita()

if __name__ == "__main__":
    main()
