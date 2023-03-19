# Määrittelydokumentti
Aiheena on Shakki-peli, ja siihen toteutettava tekoäly. Ohjelmointikielenä on Python. En tällä hetkellä osaa muita kieliä siinä määrin, että voisin vertaisarvioida niillä kirjoitettua koodia.

## Toteutettavat algoritmit ja tietorakenteet
Pelin tekoäly toteutetaan alpha-beta-karsinnalla tehostetulla Minimax-algoritmilla.

## syötteet
Ohjelma saa syötteenä pelaajan siirron.

## Aikavaativuus
Koska Minimax on raa'an voiman algoritmi, aikavaativuus on luokkaa O(n^k), jossa n on mahdollisten siirtojen määrä ja k on laskennan syvyys (eli kuinka monta vuoroa katsotaan eteenpäin). Kuitenkin jos alpha-beta-karsinnan saa toteutettua hyvin, aikavaativuus tulee olemaan merkittävästi pienempi.

## Lähteet
- [Tiralabra Minimax-pelit](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf)
- https://www.chessprogramming.org/Minimax
- https://www.chessprogramming.org/Alpha-Beta

## Opinto-ohjelma
Opinto-ohjelmani on tietojenkäsittelytieteen kandidaatti.

## Projektin kieli
Projektin dokumentaatiossa, koodissa ja kommenteissa käytettävä kieli on suomi.
