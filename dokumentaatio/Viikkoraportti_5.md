Tällä viikolla olen vertaisarvioinnin lisäksi toteuttanut shakkimatin tarkistamisen ohjelmassa ja tämän heuristisen arvioinnin minimax-algoritmissa. Olen myös refaktoroinut koodia runsaasti.

Ohjelmassa nyt liikkeiden tarkistamisen yhteydessä tarkistetaan onko kuningas shakissa. Minimax algoritmi hyödyntää tätä kutsuen shakin tapahtuessa metodia, joka tarkistaa onko kuningas shakkimatissa, eli käytännössä pysyykö shakki kaikilla seuraavilla mahdollisilla siirroilla. Mikäli shakkimatti on, arvioidaan pelitilanne heti. Arviointi toimii siten, että jos laskenta on esim. 4 siirtoa eteenpäin, ja shakkimatti löytyy kolmannella siirrolla, arvo on 5-3 * 50000. Käytännössä mikäli kaksi shakkimattia löydetään, ottaa shakkimatti joka saavutetaan vähemmillä siirroilla etusijan arvioinnissa.  Luku 50000 on valittu sillä perusteella, että se on paljon suurempi kuin mikään arvo minkä pelitilanne voi saada ilman shakkimattia. Mikäli shakkimatti on maksimoivaan puoleen kohdistuva, arvio on negatiivinen.
Liikkumisen metodi on nyt päivitetty kutsumaan suoraa sisällään liikkeiden päivittämisen metodia. Liikkeiden tarkistaminen on nyt siirretty omaan luokkaansa, ja koodia on refaktoroitu aika paljon. Liikkeiden tarkistamisen koodi on nyt paljon kompaktimpaa (n.500 riviä -> n.250 riviä).

Seuraavaksi tarkoituksena olisi vielä refaktoroida koodia lisää, sekä tehdä testit shakkimatille ja dokumentoida koodia. Myöskin tarkoituksena olisi muokata hieman käyttöliittymää, esim. näyttämään näppäinkomennot sekä valitun nappulan.

Käytetty aika: n. 10h
