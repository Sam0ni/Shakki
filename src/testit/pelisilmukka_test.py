import unittest
import pygame
from pelilauta import Pelilauta
from pelisilmukkaassetit.kello import Kello
from pelisilmukkaassetit.renderoja import Renderoja
from testit.stubbIO import StubbIO
from minimax import Minimax
from unittest.mock import Mock
from pelisilmukka import Pelisilmukka


class TestPelisilmukka(unittest.TestCase):
    def setUp(self):
        self.kello_mock = Mock(wraps=Kello())
        self.renderoja_mock = Mock(wraps=Renderoja(None, 125, None))
        self.stubi = StubbIO()
        lauta = [[8,9,10,11,12,10,9,8],
                [7,7,7,7,7,7,7,7],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1],
                [2,3,4,5,6,4,3,2]]
        self.minimax_mock = Mock(wraps=Minimax(lauta))
        pelilauta = Pelilauta(lauta, 125)
        self.silmukka = Pelisilmukka(pelilauta, 125, self.renderoja_mock, self.kello_mock, self.stubi, False, self.minimax_mock)

    def test_IO_komennot_toimivat(self):
        self.silmukka.valittu_nappula = (6, 0, 0)
        self.stubi.lisaa_syote("<Event(769-KeyUp {'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 7, 'window': None})>")
        self.silmukka._syotteet()
        self.assertEqual("", self.silmukka.valittu_nappula)