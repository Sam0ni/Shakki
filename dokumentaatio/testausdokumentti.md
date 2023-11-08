![kattavuusraportti](https://github.com/Sam0ni/Shakki/assets/101888699/47561dec-3989-4f84-8a3e-4a80fabd4a92)


Pelilogiikka, eli se että nappulat liikkuvat oikein, on testattu. Käytännössä ohjelmassa ylläpidetään kahta eri listaa, joista toisessa on kaikkien nappuloiden mahdolliset liikkeet sillä hetkellä, ja toisessa on nappuloiden liikkeiden edessä olevat nappulat. Yksikkötesteissä testataan jokaiselle nappulatyypille, että mahdolliset liikkeet ja edessä olevat nappulat tarkistetaan oikein. Myöskin testataan, että nappulat siirtyvät laudalla, ja että siirron jälkeen liikkeet päivittyvät oikein.
Siirtoa tehdessä ja liikkeitä päivittäessä pitää ottaa huomioon neljä eri tapausta:
- Siirron alkukohta on jonkin nappulan edessä
- Siirron loppukohta on jonkin nappulan mahdollisissa liikkeissä
- Siirron alkukohta on jonkin nappulan mahdollisissa liikkeissä
- Siirron loppukohta on jonkin nappulan edessä

Minimax-algoritmille on luotu oikeellisuustestejä. Testattuna on myös tietenkin pelitilanteen arvioinnin suorittava metodi. Tällä hetkellä minimax-algoritmin testaamisessa on käytössä hyvin yksinkertaiset tilanteet (2 tai 3 nappulaa) laskentasyvyyksille 2 ja 3. Käytännössä näissä tarkistetaan, että algoritmi palauttaa laskentasyvyyden perusteella saatavan parhaan liikkeen. Minimax-alogritmia on testattu myös pelkistetyissä pelitilanteissa, joissa on vain kuninkaat ja kaksi tornia. Näillä testeillä testataan löytääkö minimax vähimmillä liikkeillä saavutettavan shakkimatin. Näiden lisäksi on vielä kaksi shakkiharjoitusta jotka on peilattu, koska tämän ohjelman minimax toimii mustana pelaajana. Kyseiset harjoitukset ovat [tämä](https://chesspuzzlesonline.com/solution/ps360/) ja [tämä](https://usefulchess.com/puzzles/chess/mate-moremover.html).

Aikavaativuutta on testattu tekemällä yksikkötesti jokaiselle syvyydelle välillä 1-7 ja ottamalla ylös aika joka kuhunkin testiin kuluu. Tässä ajat, jotka itse sain: 

![Laskenta-ajat](https://github.com/Sam0ni/Shakki/assets/101888699/f784198b-f8a0-49a1-a2fb-8e89736ad6c7)

Tässä näistä tehty kuvaaja:

![kuvaaja](https://github.com/Sam0ni/Shakki/assets/101888699/d2bc5104-1a3f-4643-800d-18488710d425)

Näistä huomaa karkeasti, että kyseessä on ekspontentiaalinen nousu ajassa laskentasyvyyden kasvaessa, joten kyseessä on aikavaativuus O(n)^m.



Testit voi toistaa ohjelman juurihakemistossa suorittamalla komennon: `poetry run invoke testit`

Aikavaativuustestit täytyy suorittaa yksi kerrallaan, jos haluaa nähdä niiden vievän ajan. Testit voi toistaa ohjelman juurihakemistossa suorittamalla komennon: `poetry run pytest src/testit/aikavaativuus/aikavaativuus_laskentasyvyyskokonaislukuna_test`, jossa siis *laskentasyvyyskokonaislukuna* korvataan jollain numeroista 1-7.
