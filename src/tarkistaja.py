
class Tarkistaja:

    def __init__(self, lauta):
        self.valkoinen_shakissa = False
        self.musta_shakissa = False
        self.liikkeet = []
        self.edessa = []
        self.valkoisen_shakkaajat = []
        self.mustan_shakkaajat = []
        self.lauta = lauta

    def alusta(self):
        tarkistus_metodit = {
            1: self.tarkista_sotilas,
            2: self.tarkista_vaaka_pysty,
            3: self.tarkista_ratsu,
            4: self.tarkista_viisto,
            5: self.tarkista_kuningatar,
            6: self.tarkista_kuningas,
            7: self.tarkista_sotilas,
            8: self.tarkista_vaaka_pysty,
            9: self.tarkista_ratsu,
            10: self.tarkista_viisto,
            11: self.tarkista_kuningatar,
            12: self.tarkista_kuningas
        }

        return tarkistus_metodit

    def nollaa(self):
        self.liikkeet = []
        self.edessa = []
        self.valkoisen_shakkaajat = []
        self.mustan_shakkaajat = []
        self.valkoinen_shakissa = False
        self.musta_shakissa = False

    def palauta(self):
        return self.liikkeet, self.edessa, self.valkoinen_shakissa, self.musta_shakissa, self.valkoisen_shakkaajat, self.mustan_shakkaajat

    def tarkista_sotilas(self, nappula, y, x):
        if nappula == 1:
            korotus_raja = 1
            y_aloitus = 6
            y_liike = -1
            y_liike_alku = -2
            oma_torni = 2
            oma_kuningatar = 6
            vihollisen_sotilas = 7
            vihollisen_kuningatar = 11
            vihollisen_kuningas = 12
        else:
            korotus_raja = 6
            y_aloitus = 1
            y_liike = 1
            y_liike_alku = 2
            oma_torni = 8
            oma_kuningatar = 12
            vihollisen_sotilas = 1
            vihollisen_kuningatar = 5
            vihollisen_kuningas = 6

        if y == korotus_raja and self.lauta[y+y_liike][x] == 0:
            for i in range(oma_torni, oma_kuningatar):
                self.liikkeet.append(((nappula, y, x), (i, y+y_liike, x)))
        elif self.lauta[y+y_liike][x] == 0:
            self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x)))
            if y == y_aloitus:
                if self.lauta[y+y_liike_alku][x] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike_alku, x)))
                else:
                    self.edessa.append(((nappula, y, x), (y+y_liike_alku, x)))
        else:
            self.edessa.append(((nappula, y, x), (y+y_liike, x)))
        if x > 0:
            if y == korotus_raja and (vihollisen_sotilas <= self.lauta[y+y_liike][x-1] <= vihollisen_kuningatar):
                for i in range(oma_torni, oma_kuningatar):
                    self.liikkeet.append(((nappula, y, x), (i, y+y_liike, x-1)))
            elif y == korotus_raja and (self.lauta[y+y_liike][x-1] == vihollisen_kuningas):
                for i in range(oma_torni, oma_kuningatar):
                    self.liikkeet.append(((nappula, y, x), (i, y+y_liike, x-1)))
                if nappula == 1:
                    self.musta_shakissa = True
                    self.mustan_shakkaajat.append((nappula, y, x))
                else:
                    self.valkoinen_shakissa = True
                    self.valkoisen_shakkaajat.append((nappula, y, x))
            elif vihollisen_sotilas <= self.lauta[y+y_liike][x-1] <= vihollisen_kuningatar:
                self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x-1)))
            elif self.lauta[y+y_liike][x-1] == vihollisen_kuningas:
                self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x-1)))
                if nappula == 1:
                    self.musta_shakissa = True
                    self.mustan_shakkaajat.append((nappula, y, x))
                else:
                    self.valkoinen_shakissa = True
                    self.valkoisen_shakkaajat.append((nappula, y, x))
            else:
                self.edessa.append(((nappula, y, x), (y+y_liike, x-1)))
        if x < 7:
            if y == korotus_raja and (vihollisen_sotilas <= self.lauta[y+y_liike][x+1] <= vihollisen_kuningatar):
                for i in range(oma_torni, oma_kuningatar):
                    self.liikkeet.append(((nappula, y, x), (i, y+y_liike, x+1)))
            elif y == korotus_raja and (self.lauta[y+y_liike][x+1] == vihollisen_kuningas):
                for i in range(oma_torni, oma_kuningatar):
                    self.liikkeet.append(((nappula, y, x), (i, y+y_liike, x+1)))
                if nappula == 1:
                    self.musta_shakissa = True
                    self.mustan_shakkaajat.append((nappula, y, x))
                else:
                    self.valkoinen_shakissa = True
                    self.valkoisen_shakkaajat.append((nappula, y, x))
            elif vihollisen_sotilas <= self.lauta[y+y_liike][x+1] <= vihollisen_kuningatar:
                self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x+1)))
            elif self.lauta[y+y_liike][x+1] == vihollisen_kuningas:
                self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x+1)))
                if nappula == 1:
                    self.musta_shakissa = True
                    self.mustan_shakkaajat.append((nappula, y, x))
                else:
                    self.valkoinen_shakissa = True
                    self.valkoisen_shakkaajat.append((nappula, y, x))
            else:
                self.edessa.append(((nappula, y, x), (y+y_liike, x+1)))

    def tarkista_vaaka_pysty(self, nappula, y, x):
        alku = y + 1
        paate = 8
        steppi = 1

        for suunta in range(2):
            for i in range(alku, paate, steppi):
                if self.lauta[i][x] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    if nappula == 6 or nappula == 12:
                        break
                elif 2 <= nappula < 7 and 7<= self.lauta[i][x] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    if self.lauta[i][x] == 12:
                        self.musta_shakissa = True
                        self.mustan_shakkaajat.append((nappula, y, x))
                    break
                elif 8 <= nappula < 13 and 1<= self.lauta[i][x] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, i, x)))
                    if self.lauta[i][x] == 6:
                        self.valkoinen_shakissa = True
                        self.valkoisen_shakkaajat.append((nappula, y, x))
                    break
                else:
                    self.edessa.append(((nappula, y, x), (i, x)))
                    break
            alku = y - 1
            paate = -1
            steppi = -1
        alku = x + 1
        paate = 8
        steppi = 1
        for suunta in range(2):
            for i in range(alku, paate, steppi):
                if self.lauta[y][i] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    if nappula == 6 or nappula == 12:
                        break
                elif 2 <= nappula < 7 and 7<= self.lauta[y][i] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    if self.lauta[y][i] == 12:
                        self.musta_shakissa = True
                        self.mustan_shakkaajat.append((nappula, y, x))
                    break
                elif 8 <= nappula < 13 and 1<= self.lauta[y][i] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y, i)))
                    if self.lauta[y][i] == 6:
                        self.valkoinen_shakissa = True
                        self.valkoisen_shakkaajat.append((nappula, y, x))
                    break
                else:
                    self.edessa.append(((nappula, y, x), (y, i)))
                    break
            alku = x - 1
            paate = -1
            steppi = -1

    def tarkista_viisto(self, nappula, y, x):
        if x > y:
            montako = 8-x
        else:
            montako = 8-y
        x_suunta = 1
        y_suunta = 1
        x_liike = 1
        y_liike = 1
        for suunta in range(4):
            for i in range(1, montako):
                if self.lauta[y+y_liike][x+x_liike] == 0:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x+x_liike)))
                    if nappula == 6 or nappula == 12:
                        break
                elif 4 <= nappula <= 6 and 7 <= self.lauta[y+y_liike][x+x_liike] <= 12:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x+x_liike)))
                    if self.lauta[y+y_liike][x+x_liike] == 12:
                        self.musta_shakissa = True
                        self.mustan_shakkaajat.append((nappula, y, x))
                    break
                elif 10 <= nappula <= 12 and 1 <= self.lauta[y+y_liike][x+x_liike] <= 6:
                    self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x+x_liike)))
                    if self.lauta[y+y_liike][x+x_liike] == 6:
                        self.valkoinen_shakissa = True
                        self.valkoisen_shakkaajat.append((nappula, y, x))
                    break
                else:
                    self.edessa.append(((nappula, y, x), (y+y_liike, x+x_liike)))
                    break
                x_liike += x_suunta
                y_liike += y_suunta
            if suunta == 0:
                if x < y:
                    montako = x + 1
                else:
                    montako = y + 1
                x_suunta = -1
                y_suunta = -1
                x_liike = -1
                y_liike = -1
            elif suunta == 1:
                if x < 7 - y:
                    montako = x + 1
                else:
                    montako = 7 - y + 1
                x_suunta = -1
                y_suunta = 1
                x_liike = -1
                y_liike = 1
            elif suunta == 2:
                if 7 - x < y:
                    montako = 7 - x + 1
                else:
                    montako = y + 1
                x_suunta = 1
                y_suunta = -1
                x_liike = 1
                y_liike = -1

    def tarkista_ratsu(self, nappula, y, x):
        ehto_1 = y < 6
        ehto_2 = x < 7
        ehto_3 = x > 0
        x_liike = 1
        y_liike = 2
        for y_suunta in range(4):
            if ehto_1:
                for x_suunta in range(2):
                    if ehto_2:
                        if self.lauta[y+y_liike][x+x_liike] == 0:
                            self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x+x_liike)))
                        elif nappula == 3 and 6 <= self.lauta[y+y_liike][x+x_liike] <= 12:
                            self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x+x_liike)))
                            if self.lauta[y+y_liike][x+x_liike] == 12:
                                self.musta_shakissa = True
                                self.mustan_shakkaajat.append((nappula, y, x))
                        elif nappula == 9 and 1 <= self.lauta[y+y_liike][x+x_liike] <= 6:
                            self.liikkeet.append(((nappula, y, x), (nappula, y+y_liike, x+x_liike)))
                            if self.lauta[y+y_liike][x+x_liike] == 6:
                                self.valkoinen_shakissa = True
                                self.valkoisen_shakkaajat.append((nappula, y, x))
                        else:
                            self.edessa.append(((nappula, y, x), (y+y_liike, x+x_liike)))
                    ehto_2 = ehto_3
                    if y_suunta < 2:
                        x_liike = -x_liike
                    else:
                        y_liike = -y_liike
            if y_suunta == 0:
                ehto_1 = y > 1
                ehto_2 = x < 7
                ehto_3 = x > 0
                x_liike = 1
                y_liike = -2
            elif y_suunta == 1:
                ehto_1 = x > 1
                ehto_2 = y < 7
                ehto_3 = y > 0
                x_liike = -2
                y_liike = 1
            elif y_suunta == 2:
                ehto_1 = x < 6
                ehto_2 = y < 7
                ehto_3 = y > 0
                x_liike = 2
                y_liike = 1

    def tarkista_kuningatar(self, nappula, y, x):
        self.tarkista_viisto(nappula, y, x)
        self.tarkista_vaaka_pysty(nappula, y, x)

    def tarkista_kuningas(self, nappula, y, x):
        self.tarkista_vaaka_pysty(nappula, y, x)
        self.tarkista_viisto(nappula, y, x)
