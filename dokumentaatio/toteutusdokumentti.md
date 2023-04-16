### Ohjelman yleisrakenne:

Ohjelman käyttöliittymä on toteutettu pygame-kirjastolla. Shakki.py tiedostossa määritellään shakkilaudan alkutilanne, jonka jälkeen se annetaan Pelilauta-luokalle, joka pitää huolta pelilogiikasta, eli käytännössä laudan tilanteesta.

Tämän jälkeen aloitetaan pelisilmukka, joka hoitaa visuaalisen käyttöliittymän ja syötteet. Pelilauta puolestaan sisältää metodit liikkumiselle ja liikkeiden päivittämiselle. Liikkeiden päivittäminen perustuu kahteen listaan, joista toinen sisältää senhetkiset mahdolliset liikkeet, ja toinen jokaisen nappulan liikkeiden edessä olevat nappulat.

Liikkumisen metodi päivittää liikkuvan nappulan paikan laudalla, sekä uudet mahdolliset liikkeet ja edessä olevat nappulat. Mikäli jokin nappula tulee lyödyksi, listoista poistetaan tähän liittyvä tieto. Tämän jälkeen päivittämis-metodia kutsutaan, joka siirron perusteella päivittää liikkeiden ja edessä olevien listoja. Metodi poistaa listoista ensin kaikkiin nappuloihin, joihin siirto mahdollisesti vaikuttaa, tiedot, ja päivittää listat.

Kun valkoinen liikuttaa nappulaa laudalla, pelisilmukka kutsuu minimax-algoritmia, joka palauttaa pelisilmukalle laskentasyvyyden perusteella parhaimman mahdollisen liikkeen. Minimax-algoritmi aloittaa metodista "aloita", joka on käytännössä vain kopio maksimoivasta puolesta, mutta se pitää muuttujassa kirjaa parhaasta löydetystä liikkeestä. "aloita" kutsuu itse minimax-algoritmia, joka, kun on päästy laskentasyvyydessä pohjaan, kutsuu metodia "arvioi_pelitilanne", joka taas arvioi numeerisesti laudan perusteella pelitilanteen. Tilanteen arvio perustuu seuraavaan: [Simplified Evaluation Function](https://www.chessprogramming.org/Simplified_Evaluation_Function). Minimax-algoritmin toimintaa on myös tehostettu alpha-beta-karsinnalla, joka nopeuttaa hieman algoritmin laskentaa.

### Puutteet ja parannusehdotukset:

Ohjelmasta puuttuu vielä tärkeä ominaisuus, eli shakkimatti. Tämä ominaisuus kuitenkin on se jota aletaan seuraavaksi työstämään. Myöskin muita ominaisuuksia puuttuu, kuten ohestalyönti ja linnoittautuminen. Testejä pitää myös kirjoitella lisää ja koodia refaktoroida.

### Lähteet:

https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf

https://www.chess.com/fi/shakki#rules

https://www.chessprogramming.org/Simplified_Evaluation_Function
