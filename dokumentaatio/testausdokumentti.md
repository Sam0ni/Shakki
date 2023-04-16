![kattavuusraportti](https://user-images.githubusercontent.com/101888699/232341316-17cf12bd-4fd9-48f5-92d5-b24c1ca11ba0.png)


Tällä hetkellä on testattuna pelilogiikka, eli se, että nappulat liikkuvat oikein. Käytännössä ohjelmassa ylläpidetään kahta eri listaa, joista toisessa on kaikkien nappuloiden mahdolliset liikkeet sillä hetkellä, ja toisessa on nappuloiden liikkeiden edessä olevat nappulat. Yksikkötesteissä testataan jokaiselle nappulatyypille, että mahdolliset liikkeet ja edessä olevat nappulat tarkistetaan oikein. Myöskin testataan, että nappulat siirtyvät laudalla, ja että siirron jälkeen liikkeet päivittyvät oikein.
Siirtoa tehdessä ja liikkeitä päivittäessä pitää ottaa huomioon neljä eri tapausta:
- Siirron alkukohta on jonkin nappulan edessä
- Siirron loppukohta on jonkin nappulan mahdollisissa liikkeissä
- Siirron alkukohta on jonkin nappulan mahdollisissa liikkeissä
- Siirron loppukohta on jonkin nappulan edessä

Myös minimax-algoritmin oikeellisuustestaus on aloitettu. Testattuna on myös tietenkin pelitilanteen arvioinnin suorittava metodi. Tällä hetkellä minimax-algoritmin testaamisessa on käytössä hyvin yksinkertaiset tilanteet (2 tai 3 nappulaa) laskentasyvyyksille 2 ja 3. Käytännössä näissä tarkistetaan, että algoritmi palauttaa laskentasyvyyden perusteella saatavan parhaan liikkeen. Vielä pitää testata hieman erilaisilla tilanteilla, ja myöskin kun shakkimatti-osuus ohjelmasta saadaan valmiiksi, täytyy testata, että algoritmi osaa tehdä shakkimatin, ja myöskin valita shakkimatin joka on saavutettavissa nopeiten.

Testit voi toistaa ohjelman juurihakemistossa suorittamalla komennon: `poetry invoke testit`
