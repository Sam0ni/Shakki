Tällä viikolla olen pääasiassa työstänyt minimax-algoritmia. Nyt työ on siinä vaiheessa, että minimax pienen väännön jälkeen saatiin toimimaan, mutta koska ohjelmasta puuttuu vielä shakkimatin tarkistaminen, algoritmi ei osaa vielä tehdä shakkimattia. Olen myös kirjoittanut pari testiä yksinkertaisilla pelitilanteilla, ja näyttäisi siltä, että minimax palauttaa aivan oikean liikkeen. Olen myöskin kirjoitellut hieman dokumentaatiota.

Hieman vaikeuksia tuotti kuitenkin testaus, vaikkakin testausluennolla tuli hyvin asiaa koskien tätä. En ole aivan varma millaisilla pelitilanteilla testausta pitäisi tehdä ja millä laskentasyvyydellä, sillä mikäli laskentasyvyys on liian suuri tai pelitilanteet liian monimutkaisia, voi yhden testin kirjoittamisessa mennä järjettömän paljon aikaa, mikäli käsin alkaa laskea jokaisen siirron arvon. Sitten kun saan shakkimatin tarkistamiseen liittyvän koodin tehtyä, tulee eteen sama ongelma, eli millaisella pelitilanteella kannattaisi algoritmia testata.

Seuraavaksi alan työstämään shakkimatin tarkistamista, ja sen sisällyttämistä minimax-algoritmiin. Myöskin tarkoituksena olisi testien kirjoittaminen ja koodin siistiminen.

Käytetty aika: n. 10h
