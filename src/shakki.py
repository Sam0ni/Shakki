import pygame
from pelilauta import Pelilauta
from pelisilmukkaassetit.renderoja import Renderoja
from pelisilmukkaassetit.kello import Kello
from pelisilmukkaassetit.syotteiden_hakija import Syotteiden_hakija
from minimax import Minimax
from pelisilmukka import Pelisilmukka

lauta = [[8,9,10,11,12,10,9,8],
[7,7,7,7,7,7,7,7],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1],
[2,3,4,5,6,4,3,2]]

lauta = [[12,0,0,0,8,0,0,0],
        [0,0,0,0,0,8,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,6,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

Ruudun_Koko = 125 # pylint: disable=invalid-name

tekoaly_kaytossa = True

def main():
    """alustaa näytön, pelilaudan ja aloittaa pelisilmukan
    """
    nayton_korkeus_ja_leveys = 8*Ruudun_Koko

    pygame.init() # pylint: disable=no-member

    naytto = pygame.display.set_mode((nayton_korkeus_ja_leveys + 500, nayton_korkeus_ja_leveys))

    pygame.display.set_caption("Shakki")

    pelilauta = Pelilauta(lauta, Ruudun_Koko)

    renderoja = Renderoja(naytto, Ruudun_Koko, pelilauta)
    kello = Kello()
    syotteiden_hakija = Syotteiden_hakija()
    tekoaly = Minimax(pelilauta.lauta.copy())


    silmukka = Pelisilmukka(pelilauta, Ruudun_Koko, renderoja, kello, syotteiden_hakija, tekoaly_kaytossa, tekoaly)

    silmukka.aloita()

if __name__ == "__main__":
    main()
