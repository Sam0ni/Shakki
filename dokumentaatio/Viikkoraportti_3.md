Tällä viikolla olen tehnyt ohjelman siihen vaiheeseen, että shakki-osuus on nyt valmis, tehnyt testejä kattavasti ja dokumentoinut ja siistinyt hieman koodia.

Tein pelilogiikan mekein kokonaan uudestaan, ja nyt ei enää käytetä pygamen sprite-luokkia nappuloiden esittämiseen, vaan nappuloita esitetään nyt kokonaisnumeroilla, joita säilytetään 2-uloitteisessa taulukossa.
Sen sijaan että tarkistetan joka vuoron alussa kaikki mahdolliset liikkeet, nyt päivitetään siirron yhteydessä listaa jossa on kaikki mahdolliset liikkeet. Liikkeiden päivitystä varten ylläpidetään nyt listaa jossa on jokaiselle nappulalle niiden liikkeiden edessä olevan nappulan koordinaatit
Mahdollisten listassa on tuplena alkupaikka ja loppupaikka, toisin sanoen: ((nappulan_tyyppi, y-koordinaatti, x-koordinaatti), (nappulan_tyyppi, y-koordinaatti, x-koordinaatti)), joista ensimmäinen tuple on alkupaikka, toinen loppupaikka.
Edessä olevien listassa on koordinaatit samalla tavalla, paitsi toisessa tuplessa ei ole nappulan tyyppiä mainittu. Nappulan tyyppi on mahdollisissa liikkeissä mainittu vain sen takia, että sotilaan voi korottaa.

Liikkeiden päivittämismetodin tekeminen tuotti vaikeuksia, enkä meinannut saada sitä millään toimimaan. Lopulta sain se toimimaan, kun kirjasin ylös kaikki tapaukset kommentteina metodin alkuun, jotka pitää ottaa huomioon liikkeitä päivittäessä, ja nyt sen pitäisi toimia.

Seuraavaksi alan tehdä vihdoinkin minimax-algoritmia.

Käytetty aika: n. 13h
