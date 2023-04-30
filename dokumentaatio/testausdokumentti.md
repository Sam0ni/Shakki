![kattavuusraportti](https://user-images.githubusercontent.com/101888699/235369695-72d9accc-327f-4465-b09a-a319df21e200.png)


Tällä hetkellä on testattuna pelilogiikka, eli se, että nappulat liikkuvat oikein. Käytännössä ohjelmassa ylläpidetään kahta eri listaa, joista toisessa on kaikkien nappuloiden mahdolliset liikkeet sillä hetkellä, ja toisessa on nappuloiden liikkeiden edessä olevat nappulat. Yksikkötesteissä testataan jokaiselle nappulatyypille, että mahdolliset liikkeet ja edessä olevat nappulat tarkistetaan oikein. Myöskin testataan, että nappulat siirtyvät laudalla, ja että siirron jälkeen liikkeet päivittyvät oikein.
Siirtoa tehdessä ja liikkeitä päivittäessä pitää ottaa huomioon neljä eri tapausta:
- Siirron alkukohta on jonkin nappulan edessä
- Siirron loppukohta on jonkin nappulan mahdollisissa liikkeissä
- Siirron alkukohta on jonkin nappulan mahdollisissa liikkeissä
- Siirron loppukohta on jonkin nappulan edessä

Myös minimax-algoritmin oikeellisuustestaus on aloitettu. Testattuna on myös tietenkin pelitilanteen arvioinnin suorittava metodi. Tällä hetkellä minimax-algoritmin testaamisessa on käytössä hyvin yksinkertaiset tilanteet (2 tai 3 nappulaa) laskentasyvyyksille 2 ja 3. Käytännössä näissä tarkistetaan, että algoritmi palauttaa laskentasyvyyden perusteella saatavan parhaan liikkeen. Testattuna on myös se, että minimax-agoritmi osaa tehdä shakkimatin, ja valitsee shakkimatin joka on vähimmillä liikkeillä saavutettavissa

Testit voi toistaa ohjelman juurihakemistossa suorittamalla komennon: `poetry invoke testit`
