import pygame
from pelilauta import Pelilauta
from pelisilmukka import Pelisilmukka
from alustaja import Alustaja

lauta = [[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

ruudun_koko = 125

def main():
    """alustaa näytön, pelilaudan ja aloittaa pelisilmukan
    """
    korkeus_ja_leveys = 8
    nayton_korkeus_ja_leveys = 8*ruudun_koko
    
    
    
    naytto = pygame.display.set_mode((nayton_korkeus_ja_leveys, nayton_korkeus_ja_leveys))

    pygame.display.set_caption("Shakki")

    pelilauta = Pelilauta(lauta, ruudun_koko, Alustaja(ruudun_koko))
    
    silmukka = Pelisilmukka(pelilauta, ruudun_koko, naytto)

    pygame.init()
    silmukka.aloita()

if __name__ == "__main__":
    main()