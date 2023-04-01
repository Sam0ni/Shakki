
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

    def tarkista_liikkeet(self, nappula, y, x): # pylint: disable=invalid-name
        """Metodi joka tarkistaa nappulan kaikki mahdolliset liikkeet
        ja sen liikkumisen edessä olevat nappulat

        Args:
            nappula (int): Nappulan tyyppi
            y (int): Nappulan y-koordinaatti
            x (int): Nappulan x-koordinaatti

        Returns:
            list: kaksi listaa joista toinen on nappulan mahdolliset liikkeet
            ja toinen nappulan liikkeiden edessä olevien nappuloiden koordinaatit
        """
        liikkeet = []
        edessa = []

        if nappula == 0:
            return liikkeet, edessa

        if nappula == 1:
            if y > 0:
                if self.lauta[y-1][x] == 0:
                    liikkeet.append(((nappula, y, x), (1, y-1, x)))
                    if y == 6:
                        if self.lauta[y-2][x] == 0:
                            liikkeet.append(((nappula, y, x), (1, y-2, x)))
                        else:
                            edessa.append(((nappula, y, x), (y-2, x)))
                else:
                    edessa.append(((nappula, y, x), (y-1, x)))
                if x > 0:
                    if 7 <= self.lauta[y-1][x-1] <= 12:
                        liikkeet.append(((nappula, y, x), (1, y-1, x-1)))
                    else:
                        edessa.append(((nappula, y, x), (y-1, x-1)))
                if x < 7:
                    if 7 <= self.lauta[y-1][x+1] <= 12:
                        liikkeet.append(((nappula, y, x), (1, y-1, x+1)))
                    else:
                        edessa.append(((nappula, y, x), (y-1, x+1)))

        elif nappula == 7:
            if y < 7:
                if self.lauta[y+1][x] == 0:
                    liikkeet.append(((nappula, y, x), (7, y+1, x)))
                    if y == 1:
                        if self.lauta[y+2][x] == 0:
                            liikkeet.append(((nappula, y, x), (7, y+2, x)))
                        else:
                            edessa.append(((nappula, y, x), (y+2, x)))
                else:
                    edessa.append(((nappula, y, x), (y+1, x)))
                if x > 0:
                    if 1 <= self.lauta[y+1][x-1] <= 6:
                        liikkeet.append(((nappula, y, x), (7, y+1, x-1)))
                    else:
                        edessa.append(((nappula, y, x), (y+1, x-1)))
                if x < 7:
                    if 1 <= self.lauta[y+1][x+1] <= 6:
                        liikkeet.append(((nappula, y, x), (7, y+1, x+1)))
                    else:
                        edessa.append(((nappula, y, x), (y+1, x+1)))

        elif nappula in (2, 8):
            for i in range(y + 1, 8):
                if self.lauta[i][x] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                elif nappula == 2 and 7<= self.lauta[i][x] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    break
                elif nappula == 8 and 1<= self.lauta[i][x] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    break
                else:
                    edessa.append(((nappula, y, x), (i, x)))
                    break
            for i in range(y - 1, -1, -1):
                if self.lauta[i][x] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                elif nappula == 2 and 7<= self.lauta[i][x] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    break
                elif nappula == 8 and 1<= self.lauta[i][x] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    break
                else:
                    edessa.append(((nappula, y, x), (i, x)))
                    break
            for i in range(x + 1, 8):
                if self.lauta[y][i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                elif nappula == 2 and 7<= self.lauta[y][i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    break
                elif nappula == 8 and 1<= self.lauta[y][i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y, i)))
                    break
            for i in range(x - 1, -1, -1):
                if self.lauta[y][i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                elif nappula == 2 and 7<= self.lauta[y][i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    break
                elif nappula == 8 and 1<= self.lauta[y][i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y, i)))
                    break

        elif nappula in (3, 9):
            if y < 6:
                if x < 7:
                    if self.lauta[y+2][x+1] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y+2, x+1)))
                    elif nappula == 3 and 6 <= self.lauta[y+2][x+1] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y+2, x+1)))
                    elif nappula == 9 and 1 <= self.lauta[y+2][x+1] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y+2, x+1)))
                    else:
                        edessa.append(((nappula, y, x), (y+2, x+1)))
                if x > 0:
                    if self.lauta[y+2][x-1] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y+2, x-1)))
                    elif nappula == 3 and 6 <= self.lauta[y+2][x-1] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y+2, x-1)))
                    elif nappula == 9 and 1 <= self.lauta[y+2][x-1] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y+2, x-1)))
                    else:
                        edessa.append(((nappula, y, x), (y+2, x-1)))
            if y > 1:
                if x < 7:
                    if self.lauta[y-2][x+1] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y-2, x+1)))
                    elif nappula == 3 and 6 <= self.lauta[y-2][x+1] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y-2, x+1)))
                    elif nappula == 9 and 1 <= self.lauta[y-2][x+1] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y-2, x+1)))
                    else:
                        edessa.append(((nappula, y, x), (y-2, x+1)))
                if x > 0:
                    if self.lauta[y-2][x-1] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y-2, x-1)))
                    elif nappula == 3 and 6 <= self.lauta[y-2][x-1] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y-2, x-1)))
                    elif nappula == 9 and 1 <= self.lauta[y-2][x-1] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y-2, x-1)))
                    else:
                        edessa.append(((nappula, y, x), (y-2, x-1)))
            if x > 1:
                if y < 7:
                    if self.lauta[y+1][x-2] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x-2)))
                    elif nappula == 3 and 6 <= self.lauta[y+1][x-2] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x-2)))
                    elif nappula == 9 and 1 <= self.lauta[y+1][x-2] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x-2)))
                    else:
                        edessa.append(((nappula, y, x), (y+1, x-2)))
                if y > 0:
                    if self.lauta[y-1][x-2] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x-2)))
                    elif nappula == 3 and 6 <= self.lauta[y-1][x-2] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x-2)))
                    elif nappula == 9 and 1 <= self.lauta[y-1][x-2] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x-2)))
                    else:
                        edessa.append(((nappula, y, x), (y-1, x-2)))
            if x < 6:
                if y < 7:
                    if self.lauta[y+1][x+2] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x+2)))
                    elif nappula == 3 and 6 <= self.lauta[y+1][x+2] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x+2)))
                    elif nappula == 9 and 1 <= self.lauta[y+1][x+2] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x+2)))
                    else:
                        edessa.append(((nappula, y, x), (y+1, x+2)))
                if y > 0:
                    if self.lauta[y-1][x+2] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x+2)))
                    elif nappula == 3 and 6 <= self.lauta[y-1][x+2] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x+2)))
                    elif nappula == 9 and 1 <= self.lauta[y-1][x+2] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x+2)))
                    else:
                        edessa.append(((nappula, y, x), (y-1, x+2)))

        elif nappula in (4, 10):
            if x > y:
                montako = x
            else:
                montako = y
            for i in range(1, 8-montako):
                if self.lauta[y+i][x+i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                elif nappula == 4 and 7 <= self.lauta[y+i][x+i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                    break
                elif nappula == 10 and 1 <= self.lauta[y+i][x+i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y+i, x+i)))
                    break
            if x < 7 - y:
                montako = x
            else:
                montako = 7 - y
            for i in range(1, montako + 1):
                if self.lauta[y+i][x-i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                elif nappula == 4 and 7 <= self.lauta[y+i][x-i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                    break
                elif nappula == 10 and 1 <= self.lauta[y+i][x-i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y+i, x-i)))
                    break
            if x < y:
                montako = x
            else:
                montako = y
            for i in range(1, montako + 1):
                if self.lauta[y-i][x-i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                elif nappula == 4 and 7 <= self.lauta[y-i][x-i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                    break
                elif nappula == 10 and 1 <= self.lauta[y-i][x-i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y-i, x-i)))
                    break
            if 7 - x < y:
                montako = 7 - x
            else:
                montako = y
            for i in range(1, montako + 1):
                if self.lauta[y-i][x+i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                elif nappula == 4 and 7 <= self.lauta[y-i][x+i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                    break
                elif nappula == 10 and 1 <= self.lauta[y-i][x+i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y-i, x+i)))
                    break

        elif nappula in (5, 11):
            for i in range(y + 1, 8):
                if self.lauta[i][x] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                elif nappula == 5 and 7<= self.lauta[i][x] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    break
                elif nappula == 11 and 1<= self.lauta[i][x] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    break
                else:
                    edessa.append(((nappula, y, x), (i, x)))
                    break
            for i in range(y - 1, -1, -1):
                if self.lauta[i][x] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                elif nappula == 5 and 7<= self.lauta[i][x] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    break
                elif nappula == 11 and 1<= self.lauta[i][x] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    break
                else:
                    edessa.append(((nappula, y, x), (i, x)))
                    break
            for i in range(x + 1, 8):
                if self.lauta[y][i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                elif nappula == 5 and 7<= self.lauta[y][i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    break
                elif nappula == 11 and 1<= self.lauta[y][i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y, i)))
                    break
            for i in range(x - 1, -1, -1):
                if self.lauta[y][i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                elif nappula == 5 and 7<= self.lauta[y][i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    break
                elif nappula == 11 and 1<= self.lauta[y][i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y, i)))
                    break
            if x > y:
                montako = x
            else:
                montako = y
            for i in range(1, 8-montako):
                if self.lauta[y+i][x+i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                elif nappula == 5 and 7 <= self.lauta[y+i][x+i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                    break
                elif nappula == 11 and 1 <= self.lauta[y+i][x+i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y+i, x+i)))
                    break
            if x < 7 - y:
                montako = x
            else:
                montako = 7 - y
            for i in range(1, montako + 1):
                if self.lauta[y+i][x-i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                elif nappula == 5 and 7 <= self.lauta[y+i][x-i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                    break
                elif nappula == 11 and 1 <= self.lauta[y+i][x-i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y+i, x-i)))
                    break
            if x < y:
                montako = x
            else:
                montako = y
            for i in range(1, montako + 1):
                if self.lauta[y-i][x-i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                elif nappula == 5 and 7 <= self.lauta[y-i][x-i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                    break
                elif nappula == 11 and 1 <= self.lauta[y-i][x-i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y-i, x-i)))
                    break
            if 7 - x < y:
                montako = 7 - x
            else:
                montako = y
            for i in range(1, montako + 1):
                if self.lauta[y-i][x+i] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                elif nappula == 5 and 7 <= self.lauta[y-i][x+i] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                    break
                elif nappula == 11 and 1 <= self.lauta[y-i][x+i] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                    break
                else:
                    edessa.append(((nappula, y, x), (y-i, x+i)))
                    break

        elif nappula in (6, 12):
            if x < 7:
                if self.lauta[y][x+1] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y, x+1)))
                elif nappula == 6 and 7 <= self.lauta[y][x+1] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y, x+1)))
                elif nappula == 12 and 1 <= self.lauta[y][x+1] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y, x+1)))
                else:
                    edessa.append(((nappula, y, x), (y, x+1)))
                if y < 7:
                    if self.lauta[y+1][x+1] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x+1)))
                    elif nappula == 6 and 7 <= self.lauta[y+1][x+1] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x+1)))
                    elif nappula == 12 and 1 <= self.lauta[y+1][x+1] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x+1)))
                    else:
                        edessa.append(((nappula, y, x), (y+1, x+1)))
                if y > 0:
                    if self.lauta[y-1][x+1] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x+1)))
                    elif nappula == 6 and 7 <= self.lauta[y-1][x+1] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x+1)))
                    elif nappula == 12 and 1 <= self.lauta[y-1][x+1] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x+1)))
                    else:
                        edessa.append(((nappula, y, x), (y-1, x+1)))
            if x > 0:
                if self.lauta[y][x-1] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y, x-1)))
                elif nappula == 6 and 7 <= self.lauta[y][x-1] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y, x-1)))
                elif nappula == 12 and 1 <= self.lauta[y][x-1] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y, x-1)))
                else:
                    edessa.append(((nappula, y, x), (y, x-1)))
                if y < 7:
                    if self.lauta[y+1][x-1] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x-1)))
                    elif nappula == 6 and 7 <= self.lauta[y+1][x-1] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x-1)))
                    elif nappula == 12 and 1 <= self.lauta[y+1][x-1] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y+1, x-1)))
                    else:
                        edessa.append(((nappula, y, x), (y+1, x-1)))
                if y > 0:
                    if self.lauta[y-1][x-1] == 0:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x-1)))
                    elif nappula == 6 and 7 <= self.lauta[y-1][x-1] <= 12:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x-1)))
                    elif nappula == 12 and 1 <= self.lauta[y-1][x-1] <= 6:
                        liikkeet.append(((nappula, y, x), (nappula, y-1, x-1)))
                    else:
                        edessa.append(((nappula, y, x), (y-1, x-1)))
            if y > 0:
                if self.lauta[y-1][x] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y-1, x)))
                elif nappula == 6 and 7 <= self.lauta[y-1][x] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y-1, x)))
                elif nappula == 12 and 1 <= self.lauta[y-1][x] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y-1, x)))
                else:
                    edessa.append(((nappula, y, x), (y-1, x)))
            if y < 7:
                if self.lauta[y+1][x] == 0:
                    liikkeet.append(((nappula, y, x), (nappula, y+1, x)))
                elif nappula == 6 and 7 <= self.lauta[y+1][x] <= 12:
                    liikkeet.append(((nappula, y, x), (nappula, y+1, x)))
                elif nappula == 12 and 1 <= self.lauta[y+1][x] <= 6:
                    liikkeet.append(((nappula, y, x), (nappula, y+1, x)))
                else:
                    edessa.append(((nappula, y, x), (y+1, x)))

        return liikkeet, edessa



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
            list: kaksi listaa joista toinen on nappulan mahdolliset liikkeet
            ja toinen nappulan liikkeiden edessä olevien nappuloiden koordinaatit
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
        uudet = list(set(poistettavat))
        for nappula in uudet:
            liikkeet_ja_blokit = self.tarkista_liikkeet(nappula[0], nappula[1], nappula[2])
            nappulan_uudet_liikkeet = liikkeet_ja_blokit[0]
            nappulan_uudet_blokit = liikkeet_ja_blokit[1]
            mahdolliset = mahdolliset + nappulan_uudet_liikkeet
            blokit = blokit + nappulan_uudet_blokit
        return mahdolliset, blokit

    def liiku(self, alku, loppu, liikkeet, edessa):
        """Metodi joka liikuttaa nappulaa laudalla

        Args:
            alku (tuple): siirretyn nappulan alkuperäinen paikka
            loppu (tuple): siirretyn nappulan loppupaikka
            liikkeet (list): lista mahdollista liikkeistä
            edessa (list): lista edessä olevien nappuloiden koordinaateista

        Returns:
            list: kaksi listaa joista toinen on nappulan mahdolliset liikkeet
            ja toinen nappulan liikkeiden edessä olevien nappuloiden koordinaatit
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
        uudet_liikkeet, uudet_edessa = self.tarkista_liikkeet(loppu[0], loppu[1], loppu[2])
        #lisää mahdollisiin liikkeisiin uudet liikkeet
        mahdolliset = mahdolliset + uudet_liikkeet
        #lisää blokkeihin uudet blokit
        blokit = blokit + uudet_edessa
        return mahdolliset, blokit
