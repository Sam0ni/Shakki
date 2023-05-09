from tarkistaja import Tarkistaja
from copy import deepcopy

class Pelilauta:
    """Luokka joka pitää huolta pelilaudan tilanteesta
    """
    def __init__(self, lauta, ruudun_koko):
        """Luokan konstruktori, jossa määritellään tarvittavat muuttujat

        Args:
            lauta: 2-ulotteinen taulukko joka kuvaa pelilautaa
            ruudun_koko: Yhden pelilaudan ruudun koko
        """
        self.lauta = lauta
        self.ruudun_koko = ruudun_koko 
        self.tarkistaja = Tarkistaja(self.lauta)
        self.tarkistajat = self.tarkistaja.alusta()

    def tarkista_liikkeet(self, nappulat): # pylint: disable=invalid-name
        """Metodi joka tarkistaa nappulan kaikki mahdolliset liikkeet
        ja sen liikkumisen edessä olevat nappulat

        Args:
            nappula (int): Nappulan tyyppi
            y (int): Nappulan y-koordinaatti
            x (int): Nappulan x-koordinaatti

        Returns:
            tuple: neljä listaa joista toinen on nappulan mahdolliset liikkeet,
            toinen nappulan liikkeiden edessä olevien nappuloiden koordinaatit,
            kolmas ja neljäs shakin aiheuttavat nappulat. Myös kaksi totuusarvoa,
            jotka ilmaisevat shakin
        """
        self.tarkistaja.nollaa()
        self.tarkistaja.lauta = self.lauta
        for nappula in nappulat:
            self.tarkistajat[nappula[0]](nappula[0], nappula[1], nappula[2])
        listat = self.tarkistaja.palauta()
        return listat[0], listat[1], listat[2], listat[3], listat[4], listat[5]

    def tarkista_matti(self, liikkeet, edessa, valkoinen, shakkaajat):
        """tarkistaa onko shakkimatti liikkeen seurauksena

        Args:
            liikkeet (list): mahdolliset liikkeet
            edessa (list): edessa olevat nappulat
            valkoinen (bool): onko shakattu valkoinen
            shakkaajat (list): kuninkaan shakkaajat

        Returns:
            bool: onko shakkimatti saavutettu
        """
        kopio_lauta = deepcopy(self.lauta)

        if valkoinen:
            sotilas = 1
            kuningas = 6
            vihollisen_kuningas = 12
        else:
            sotilas = 7
            kuningas = 12
            vihollisen_kuningas = 6
        matissa = False
        for liike in liikkeet:
            if kopio_lauta[liike[1][1]][liike[1][2]] == vihollisen_kuningas:
                matissa = False
                break
            elif sotilas <= liike[0][0] <= kuningas:
                kopio_shakkaajat = deepcopy(shakkaajat)
                uudet_liikkeet, uudet_edessa, valkoinen_shakissa, musta_shakissa, valkoisen_shakkaajat, mustan_shakkaajat = self.liiku(liike[0], liike[1], liikkeet, edessa)
                for shakkaaja in shakkaajat:
                    if liike[1][1] == shakkaaja[1] and liike[1][2] == shakkaaja[2]:
                        kopio_shakkaajat.remove(shakkaaja)
                shakkaajien_tila = self.tarkista_liikkeet(kopio_shakkaajat)
                valkoinen_shakissa = valkoinen_shakissa or shakkaajien_tila[2]
                musta_shakissa = musta_shakissa or shakkaajien_tila[3]
                if valkoinen and valkoinen_shakissa:
                    self.lauta = deepcopy(kopio_lauta)
                    matissa = True
                elif not valkoinen and musta_shakissa:
                    self.lauta = deepcopy(kopio_lauta)
                    matissa = True
                else:
                    matissa = False
                    break
        self.lauta = deepcopy(kopio_lauta)
        return matissa



    def paivita(self, liikkeet, edessa, alku, loppu):
        """Metodi joka päivittää kaikkien nappuloiden, joihin
        edellinen siirto mahdollisesti vaikutti, liikkeet ja
        liikkeiden edessä olevat nappulat

        Args:
            liikkeet (list): lista mahdollista liikkeistä
            edessa (list): lista edessä olevien nappuloiden koordinaateista
            alku (tuple): siirretyn nappulan alkuperäinen paikka
            loppu (tuple): siirretyn nappulan loppupaikka

        Returns:
            tuple: neljä listaa joista toinen on nappulan mahdolliset liikkeet,
            toinen nappulan liikkeiden edessä olevien nappuloiden koordinaatit,
            kolmas ja neljäs shakin aiheuttavat nappulat. Myös kaksi totuusarvoa,
            jotka ilmaisevat shakin
        """
        #alkupaikka jonkun blokkilistalla
        #loppupaikka jonkun blokkilistalla
        #alkupaikka jonkun liikelistalla
        #loppupaikka jonkun liikelistalla
        mahdolliset = [] + liikkeet
        blokit = [] + edessa
        poistettavat = [] #nappulat joiden liikkeet ja blokit poistetaan
        for blokki in edessa:
            if blokki[1] == (alku[1], alku[2]) or blokki[1] == (loppu[1], loppu[2]):
                poistettavat.append(blokki[0])
        for liike in liikkeet:
            if ((liike[1][1], liike[1][2]) == (alku[1], alku[2]) or
                    (liike[1][1], liike[1][2]) == (loppu[1], loppu[2])):
                poistettavat.append(liike[0])
        for blokki in edessa:
            if blokki[0] in poistettavat:
                blokit.remove(blokki)
        for liike in liikkeet:
            if liike[0] in poistettavat:
                mahdolliset.remove(liike)
        poistettavat.append(loppu)
        uudet = list(set(poistettavat))
        tarkistetut = self.tarkista_liikkeet(uudet)
        mahdolliset = mahdolliset + tarkistetut[0]
        blokit = blokit + tarkistetut[1]
        return mahdolliset, blokit, tarkistetut[2], tarkistetut[3], tarkistetut[4], tarkistetut[5]

    def liiku(self, alku, loppu, liikkeet, edessa):
        """Metodi joka liikuttaa nappulaa laudalla

        Args:
            alku (tuple): siirretyn nappulan alkuperäinen paikka
            loppu (tuple): siirretyn nappulan loppupaikka
            liikkeet (list): lista mahdollista liikkeistä
            edessa (list): lista edessä olevien nappuloiden koordinaateista

        Returns:
            tuple: neljä listaa joista toinen on nappulan mahdolliset liikkeet,
            toinen nappulan liikkeiden edessä olevien nappuloiden koordinaatit,
            kolmas ja neljäs shakin aiheuttavat nappulat. Myös kaksi totuusarvoa,
            jotka ilmaisevat shakin
        """
        mahdolliset = [] + liikkeet
        blokit = [] + edessa
        alku_y = alku[1]
        alku_x = alku[2]
        loppu_y = loppu[1]
        loppu_x = loppu[2]
        if self.lauta[loppu_y][loppu_x] != 0:
            for liike in liikkeet: # poista syödyn liikkeet
                if (liike[0][1], liike[0][2]) == (loppu[1], loppu[2]):
                    mahdolliset.remove(liike)
            for blokki in edessa: #poista syödyn blokit
                if (blokki[0][1], blokki[0][2]) == (loppu[1], loppu[2]):
                    blokit.remove(blokki)
        self.lauta[alku_y][alku_x] = 0
        self.lauta[loppu_y][loppu_x] = loppu[0]
        for liike in liikkeet: #poista edelliset liikkeet
            if liike[0] == alku:
                mahdolliset.remove(liike)
        for blokki in edessa: #poista edelliset blokit
            if blokki[0] == alku:
                blokit.remove(blokki)
        # tarkista uudet liikkeet ja blokit
        return self.paivita(mahdolliset, blokit, alku, loppu)

    def alusta(self):
        """Alustaa laudan

        Returns:
            tuple: mahdolliset liikkeet, edessa olevat, shakkaustiedot
        """
        nappulat = []
        for y in range(8):
            for x in range(8):
                if self.lauta[y][x] == 0:
                    continue
                nappulat.append((self.lauta[y][x], y, x))
        return self.tarkista_liikkeet(nappulat)
