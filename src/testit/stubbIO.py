

class StubbIO:
    def __init__(self):
        self.syotteet = []

    def hae(self):
        return self.syotteet

    def lisaa_syote(self, syote):
        self.syotteet.append(syote)
