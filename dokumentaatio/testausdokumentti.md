

Tällä hetkellä on testattuna pelilogiikka, eli se, että nappulat liikkuvat oikein. Käytännössä ohjelmassa ylläpidetään kahta eri listaa, joista toisessa on kaikkien nappuloiden mahdolliset liikkeet sillä hetkellä, ja toisessa on nappuloiden liikkeiden edessä olevat nappulat. Yksikkötesteissä testataan jokaiselle nappulatyypille, että mahdolliset liikkeet ja edessä olevat nappulat tarkistetaan oikein. Myöskin testataan, että nappulat siirtyvät laudalla, ja että siirron jälkeen liikkeet päivittyvät oikein.
Siirtoa tehdessä ja liikkeitä päivittäessä pitää ottaa huomioon neljä eri tapausta:
- Siirron alkukohta on jonkin nappulan edessä
- Siirron loppukohta on jonkin nappulan mahdollisissa liikkeissä
- Siirron alkukohta on jonkin nappulan mahdollisissa liikkeissä
- Siirron loppukohta on jonkin nappulan edessä

Testit voi toistaa ohjelman juurihakemistossa suorittamalla komennon: `poetry invoke testit`
