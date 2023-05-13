# Käyttöohje
## Asennus
Käytettävällä koneella täytyy olla poetry asennettuna!

Kloonaa github repositorio koneellesi, ja suorita ohjelman hakemiston juuressa komento `poetry install`.

## Käynnistys
Ohjelman voi käynnistää parilla eri tavalla:

Tapa 1: `poetry run invoke aloita`

Tapa 2: `poetry run python3 src/Shakki.py`

## Pelaaminen
Pelaaja aloittaa aina valkoisella puolella, ja tekoäly on oletuksena käytössä. Tekoäly pelaa pelkästään mustilla nappuloilla. Käyttöliittymän sivussa lukee kaikki tarvittavat komennot, kuten tekoälyn laskentasyvyyden säätäminen (mitä isompi luku, sen paremmin tekoäly pelaa, mutta jo 4-5 syvyydellä laskenta voi kestää minuutteja, joten oletuksena kannattaa pitää syvyys < 5), tekoälyn pois ja päälle kytkeminen ja sotilaan korotuksen valitseminen.
Nappula valitaan hiirellä, ja loppupaikka samoin. Nappulan valinnan voi poistaa D-näppäimellä.

Pelissä toimii shakin perus säännöt ja ominaisuudet, paitsi ohestalyönti ja linnoittautuminen. Myöskään pelissä ei voi sopia tasapeliä, vaan tasapeli tapahtuu patista johtuen.
