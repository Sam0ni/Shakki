
class Tarkistaja:

    def __init__(self, lauta):
        self.valkoinen_shakissa = False
        self.musta_shakissa = False
        self.liikkeet = []
        self.edessa = []
        self.lauta = []

    def alusta(self):
        tarkistus_metodit = {
            1: self.tarkista_valkoinen_sotilas,
            2: self.tarkista_torni,
            3: self.tarkista_ratsu,
            4: self.tarkista_lahetti,
            5: self.tarkista_kuningatar,
            6: self.tarkista_kuningas,
            7: self.tarkista_musta_sotilas,
            8: self.tarkista_torni,
            9: self.tarkista_ratsu,
            10: self.tarkista_lahetti,
            11: self.tarkista_kuningatar,
            12: self.tarkista_kuningas
        }

        return tarkistus_metodit

    def nollaa(self):
        self.liikkeet = []
        self.edessa = []
        self.valkoinen_shakissa = False
        self.musta_shakissa = False

    def palauta(self):
        return self.liikkeet, self.edessa, self.valkoinen_shakissa, self.musta_shakissa

    def tarkista_valkoinen_sotilas(self, nappula, y, x):
        if y > 0:
            if y == 1 and self.lauta[y-1][x] == 0:
                for i in range(2, 6):
                    self.liikkeet.append(((nappula, y, x), (i, y-1, x)))
            elif self.lauta[y-1][x] == 0:
                self.liikkeet.append(((nappula, y, x), (1, y-1, x)))
                if y == 6:
                    if self.lauta[y-2][x] == 0:
                        self.liikkeet.append(((nappula, y, x), (1, y-2, x)))
                    else:
                        self.edessa.append(((nappula, y, x), (y-2, x)))
            else:
                self.edessa.append(((nappula, y, x), (y-1, x)))
            if x > 0:
                if y == 1 and (7 <= self.lauta[y-1][x-1] <= 12):
                    for i in range(2, 6):
                        self.liikkeet.append(((nappula, y, x), (i, y-1, x-1)))
                elif 7 <= self.lauta[y-1][x-1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (1, y-1, x-1)))
                else:
                    self.edessa.append(((nappula, y, x), (y-1, x-1)))
            if x < 7:
                if y == 1 and (7 <= self.lauta[y-1][x+1] <= 12):
                    for i in range(2, 6):
                        self.liikkeet.append(((nappula, y, x), (i, y-1, x+1)))
                if 7 <= self.lauta[y-1][x+1] <= 11:
                    self.liikkeet.append(((nappula, y, x), (1, y-1, x+1)))
                elif self.lauta[y-1][x+1] == 12:
                    self.liikkeet.append(((nappula, y, x), (1, y-1, x+1)))
                    self.musta_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y-1, x+1)))
    
    def tarkista_musta_sotilas(self, nappula, y, x):
        if y < 7:
            if y == 6 and self.lauta[y+1][x] == 0:
                for i in range(8, 12):
                    self.liikkeet.append(((nappula, y, x), (i, y+1, x)))
            elif self.lauta[y+1][x] == 0:
                self.liikkeet.append(((nappula, y, x), (7, y+1, x)))
                if y == 1:
                    if self.lauta[y+2][x] == 0:
                        self.liikkeet.append(((nappula, y, x), (7, y+2, x)))
                    else:
                        self.edessa.append(((nappula, y, x), (y+2, x)))
            else:
                self.edessa.append(((nappula, y, x), (y+1, x)))
            
            if x > 0:
                if y == 6 and (1 <= self.lauta[y+1][x-1] <= 6):
                    for i in range(8, 12):
                        self.liikkeet.append(((nappula, y, x), (i, y+1, x-1)))
                elif 1 <= self.lauta[y+1][x-1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (7, y+1, x-1)))
                else:
                    self.edessa.append(((nappula, y, x), (y+1, x-1)))
            if x < 7:
                if y == 6 and (1 <= self.lauta[y+1][x+1] <= 6):
                    for i in range(8, 12):
                        self.liikkeet.append(((nappula, y, x), (i, y+1, x+1)))
                if 1 <= self.lauta[y+1][x+1] <= 5:
                    self.liikkeet.append(((nappula, y, x), (7, y+1, x+1)))
                elif self.lauta[y+1][x+1] == 6:
                    self.liikkeet.append(((nappula, y, x), (7, y+1, x+1)))
                    self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y+1, x+1)))
    
    def tarkista_torni(self, nappula, y, x):
        for i in range(y + 1, 8):
            if self.lauta[i][x] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
            elif nappula == 2 and 7<= self.lauta[i][x] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                if self.lauta[i][x] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 8 and 1<= self.lauta[i][x] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                if self.lauta[i][x] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (i, x)))
                break
        for i in range(y - 1, -1, -1):
            if self.lauta[i][x] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
            elif nappula == 2 and 7<= self.lauta[i][x] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                if self.lauta[i][x] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 8 and 1<= self.lauta[i][x] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                if self.lauta[i][x] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (i, x)))
                break
        for i in range(x + 1, 8):
            if self.lauta[y][i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
            elif nappula == 2 and 7<= self.lauta[y][i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                if self.lauta[y][i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 8 and 1<= self.lauta[y][i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                if self.lauta[y][i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y, i)))
                break
        for i in range(x - 1, -1, -1):
            if self.lauta[y][i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
            elif nappula == 2 and 7<= self.lauta[y][i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                if self.lauta[y][i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 8 and 1<= self.lauta[y][i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                if self.lauta[y][i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y, i)))
                break

    def tarkista_ratsu(self, nappula, y, x):
        if y < 6:
            if x < 7:
                if self.lauta[y+2][x+1] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+2, x+1)))
                elif nappula == 3 and 6 <= self.lauta[y+2][x+1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+2, x+1)))
                    if self.lauta[y+2][x+1] == 12:
                        self.musta_shakissa = True
                elif nappula == 9 and 1 <= self.lauta[y+2][x+1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+2, x+1)))
                    if self.lauta[y+2][x+1] == 6:
                        self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y+2, x+1)))
            if x > 0:
                if self.lauta[y+2][x-1] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+2, x-1)))
                elif nappula == 3 and 6 <= self.lauta[y+2][x-1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+2, x-1)))
                    if self.lauta[y+2][x-1] == 12:
                        self.musta_shakissa = True
                elif nappula == 9 and 1 <= self.lauta[y+2][x-1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+2, x-1)))
                    if self.lauta[y+2][x-1] == 6:
                        self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y+2, x-1)))
        if y > 1:
            if x < 7:
                if self.lauta[y-2][x+1] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-2, x+1)))
                elif nappula == 3 and 6 <= self.lauta[y-2][x+1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-2, x+1)))
                    if self.lauta[y-2][x+1] == 12:
                        self.musta_shakissa = True
                elif nappula == 9 and 1 <= self.lauta[y-2][x+1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-2, x+1)))
                    if self.lauta[y-2][x+1] == 6:
                        self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y-2, x+1)))
            if x > 0:
                if self.lauta[y-2][x-1] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-2, x-1)))
                elif nappula == 3 and 6 <= self.lauta[y-2][x-1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-2, x-1)))
                    if self.lauta[y-2][x-1] == 12:
                        self.musta_shakissa = True
                elif nappula == 9 and 1 <= self.lauta[y-2][x-1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-2, x-1)))
                    if self.lauta[y-2][x-1] == 6:
                        self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y-2, x-1)))
        if x > 1:
            if y < 7:
                if self.lauta[y+1][x-2] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x-2)))
                elif nappula == 3 and 6 <= self.lauta[y+1][x-2] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x-2)))
                    if self.lauta[y+1][x-2] == 12:
                        self.musta_shakissa = True
                elif nappula == 9 and 1 <= self.lauta[y+1][x-2] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x-2)))
                    if self.lauta[y+1][x-2] == 6:
                        self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y+1, x-2)))
            if y > 0:
                if self.lauta[y-1][x-2] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x-2)))
                elif nappula == 3 and 6 <= self.lauta[y-1][x-2] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x-2)))
                    if self.lauta[y-1][x-2] == 12:
                        self.musta_shakissa = True
                elif nappula == 9 and 1 <= self.lauta[y-1][x-2] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x-2)))
                    if self.lauta[y-1][x-2] <= 6:
                        self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y-1, x-2)))
        if x < 6:
            if y < 7:
                if self.lauta[y+1][x+2] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x+2)))
                elif nappula == 3 and 6 <= self.lauta[y+1][x+2] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x+2)))
                    if self.lauta[y+1][x+2] == 12:
                        self.musta_shakissa = True
                elif nappula == 9 and 1 <= self.lauta[y+1][x+2] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x+2)))
                    if self.lauta[y+1][x+2] == 6:
                        self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y+1, x+2)))
            if y > 0:
                if self.lauta[y-1][x+2] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x+2)))
                elif nappula == 3 and 6 <= self.lauta[y-1][x+2] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x+2)))
                    if self.lauta[y-1][x+2] == 12:
                        self.musta_shakissa = True
                elif nappula == 9 and 1 <= self.lauta[y-1][x+2] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x+2)))
                    if self.lauta[y-1][x+2] == 6:
                        self.valkoinen_shakissa = True
                else:
                    self.edessa.append(((nappula, y, x), (y-1, x+2)))

    def tarkista_lahetti(self, nappula, y, x):
        if x > y:
            montako = x
        else:
            montako = y
        for i in range(1, 8-montako):
            if self.lauta[y+i][x+i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
            elif nappula == 4 and 7 <= self.lauta[y+i][x+i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                if self.lauta[y+i][x+i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 10 and 1 <= self.lauta[y+i][x+i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                if self.lauta[y+i][x+i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y+i, x+i)))
                break
        if x < 7 - y:
            montako = x
        else:
            montako = 7 - y
        for i in range(1, montako + 1):
            if self.lauta[y+i][x-i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
            elif nappula == 4 and 7 <= self.lauta[y+i][x-i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                if self.lauta[y+i][x-i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 10 and 1 <= self.lauta[y+i][x-i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                if self.lauta[y+i][x-i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y+i, x-i)))
                break
        if x < y:
            montako = x
        else:
            montako = y
        for i in range(1, montako + 1):
            if self.lauta[y-i][x-i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
            elif nappula == 4 and 7 <= self.lauta[y-i][x-i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                if self.lauta[y-i][x-i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 10 and 1 <= self.lauta[y-i][x-i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                if self.lauta[y-i][x-i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y-i, x-i)))
                break
        if 7 - x < y:
            montako = 7 - x
        else:
            montako = y
        for i in range(1, montako + 1):
            if self.lauta[y-i][x+i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
            elif nappula == 4 and 7 <= self.lauta[y-i][x+i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                if self.lauta[y-i][x+i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 10 and 1 <= self.lauta[y-i][x+i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                if self.lauta[y-i][x+i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y-i, x+i)))
                break

    def tarkista_kuningatar(self, nappula, y, x):
        for i in range(y + 1, 8):
            if self.lauta[i][x] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
            elif nappula == 5 and 7<= self.lauta[i][x] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                if self.lauta[i][x] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 11 and 1<= self.lauta[i][x] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                if self.lauta[i][x] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (i, x)))
                break
        for i in range(y - 1, -1, -1):
            if self.lauta[i][x] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
            elif nappula == 5 and 7<= self.lauta[i][x] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                if self.lauta[i][x] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 11 and 1<= self.lauta[i][x] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                if self.lauta[i][x] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (i, x)))
                break
        for i in range(x + 1, 8):
            if self.lauta[y][i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
            elif nappula == 5 and 7<= self.lauta[y][i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                if self.lauta[y][i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 11 and 1<= self.lauta[y][i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                if self.lauta[y][i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y, i)))
                break
        for i in range(x - 1, -1, -1):
            if self.lauta[y][i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
            elif nappula == 5 and 7<= self.lauta[y][i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                if self.lauta[y][i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 11 and 1<= self.lauta[y][i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                if self.lauta[y][i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y, i)))
                break
        if x > y:
            montako = x
        else:
            montako = y
        for i in range(1, 8-montako):
            if self.lauta[y+i][x+i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
            elif nappula == 5 and 7 <= self.lauta[y+i][x+i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                if self.lauta[y+i][x+i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 11 and 1 <= self.lauta[y+i][x+i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x+i)))
                if self.lauta[y+i][x+i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y+i, x+i)))
                break
        if x < 7 - y:
            montako = x
        else:
            montako = 7 - y
        for i in range(1, montako + 1):
            if self.lauta[y+i][x-i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
            elif nappula == 5 and 7 <= self.lauta[y+i][x-i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                if self.lauta[y+i][x-i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 11 and 1 <= self.lauta[y+i][x-i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y+i, x-i)))
                if self.lauta[y+i][x-i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y+i, x-i)))
                break
        if x < y:
            montako = x
        else:
            montako = y
        for i in range(1, montako + 1):
            if self.lauta[y-i][x-i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
            elif nappula == 5 and 7 <= self.lauta[y-i][x-i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                if self.lauta[y-i][x-i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 11 and 1 <= self.lauta[y-i][x-i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x-i)))
                if self.lauta[y-i][x-i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y-i, x-i)))
                break
        if 7 - x < y:
            montako = 7 - x
        else:
            montako = y
        for i in range(1, montako + 1):
            if self.lauta[y-i][x+i] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
            elif nappula == 5 and 7 <= self.lauta[y-i][x+i] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                if self.lauta[y-i][x+i] == 12:
                    self.musta_shakissa = True
                break
            elif nappula == 11 and 1 <= self.lauta[y-i][x+i] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y-i, x+i)))
                if self.lauta[y-i][x+i] == 6:
                    self.valkoinen_shakissa = True
                break
            else:
                self.edessa.append(((nappula, y, x), (y-i, x+i)))
                break

    def tarkista_kuningas(self, nappula, y, x):
        if x < 7:
            if self.lauta[y][x+1] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y, x+1)))
            elif nappula == 6 and 7 <= self.lauta[y][x+1] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y, x+1)))
            elif nappula == 12 and 1 <= self.lauta[y][x+1] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y, x+1)))
            else:
                self.edessa.append(((nappula, y, x), (y, x+1)))
            if y < 7:
                if self.lauta[y+1][x+1] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x+1)))
                elif nappula == 6 and 7 <= self.lauta[y+1][x+1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x+1)))
                elif nappula == 12 and 1 <= self.lauta[y+1][x+1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x+1)))
                else:
                    self.edessa.append(((nappula, y, x), (y+1, x+1)))
            if y > 0:
                if self.lauta[y-1][x+1] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x+1)))
                elif nappula == 6 and 7 <= self.lauta[y-1][x+1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x+1)))
                elif nappula == 12 and 1 <= self.lauta[y-1][x+1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x+1)))
                else:
                    self.edessa.append(((nappula, y, x), (y-1, x+1)))
        if x > 0:
            if self.lauta[y][x-1] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y, x-1)))
            elif nappula == 6 and 7 <= self.lauta[y][x-1] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y, x-1)))
            elif nappula == 12 and 1 <= self.lauta[y][x-1] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y, x-1)))
            else:
                self.edessa.append(((nappula, y, x), (y, x-1)))
            if y < 7:
                if self.lauta[y+1][x-1] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x-1)))
                elif nappula == 6 and 7 <= self.lauta[y+1][x-1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x-1)))
                elif nappula == 12 and 1 <= self.lauta[y+1][x-1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+1, x-1)))
                else:
                    self.edessa.append(((nappula, y, x), (y+1, x-1)))
            if y > 0:
                if self.lauta[y-1][x-1] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x-1)))
                elif nappula == 6 and 7 <= self.lauta[y-1][x-1] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x-1)))
                elif nappula == 12 and 1 <= self.lauta[y-1][x-1] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y-1, x-1)))
                else:
                    self.edessa.append(((nappula, y, x), (y-1, x-1)))
        if y > 0:
            if self.lauta[y-1][x] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y-1, x)))
            elif nappula == 6 and 7 <= self.lauta[y-1][x] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y-1, x)))
            elif nappula == 12 and 1 <= self.lauta[y-1][x] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y-1, x)))
            else:
                self.edessa.append(((nappula, y, x), (y-1, x)))
        if y < 7:
            if self.lauta[y+1][x] == 0:
                self.liikkeet.append(((nappula, y, x), (nappula, y+1, x)))
            elif nappula == 6 and 7 <= self.lauta[y+1][x] <= 12:
                self.liikkeet.append(((nappula, y, x), (nappula, y+1, x)))
            elif nappula == 12 and 1 <= self.lauta[y+1][x] <= 6:
                self.liikkeet.append(((nappula, y, x), (nappula, y+1, x)))
            else:
                self.edessa.append(((nappula, y, x), (y+1, x)))
