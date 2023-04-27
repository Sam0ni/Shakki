import os
import dotenv
import ast

hakemisto = os.path.dirname(__file__)
envin_polku = os.path.join(hakemisto, "..", ".env")

class Heuristiset_arvot:
    def hae(self):
        dotenv.load_dotenv(envin_polku)
        nappuloiden_arvot = self.nappulat()
        valkoiset = self.valkoiset_lauta()
        mustat = self.mustat_lauta()
        return nappuloiden_arvot, valkoiset, mustat


    def nappulat(self):
        return ast.literal_eval(os.environ["nappula_arvot"])
        
    def valkoiset_lauta(self):
        return ast.literal_eval(os.environ["valkoinen_lauta_arvot"])

    def mustat_lauta(self):
        return ast.literal_eval(os.environ["musta_lauta_arvot"])