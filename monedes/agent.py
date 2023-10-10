""" Mòdul que conté l'agent per jugar al joc de les monedes.

Percepcions:
    ClauPercepcio.MONEDES
Solució:
    " XXXC"
"""

from ia_2022 import agent, entorn

SOLUCIO = " XXXC"


class AgentMoneda(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=0)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def pinta(self, display):
        print(self._posicio_pintar)

    def actua(
        self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        pass

class Estat:
    def __init__(self, accions_previes = None) -> None:
        if accions_previes is None:
            accions_previes = []

        self.monedes = []
        self.accions_previstes = accions_previes
        self.posEspai = self.monedes.index(" ")

    def generar_fills_desplacar(self) -> list:
        lista_botar = []
        for i in self.monedes:
            estatAux = self
            if estatAux.monedes[i] == "C":
                estatAux.monedes[i] = " "
                estatAux[self.posEspai] = "X"
                estatAux.accions_previstes.append("BOTAR")
                lista_botar.append(estatAux)
            elif estatAux.monedes[i] == "X":
                estatAux.monedes[i] = " "
                estatAux[self.posEspai] = "C"
                estatAux.accions_previstes.append("BOTAR")
                lista_botar.append(estatAux)
        return lista_botar

    def generar_fills_botar(self) -> list:
        lista_desplacar = []
        for i in self.monedes:
            estatAux = self
            if estatAux.monedes[i] == "C":
                estatAux.monedes[i], estatAux[self.posEspai] = " ", "X"
                estatAux.accions_previstes.append("BOTAR")
                lista_desplacar.append(estatAux)
            elif estatAux.monedes[i] == "X":
                estatAux.monedes[i], estatAux[self.posEspai] = " ", "C"
                estatAux.accions_previstes.append("BOTAR")
                lista_desplacar.append(estatAux)
        return lista_desplacar

    def generar_fills(self) -> list:
        lista_fills = []
        lista_fills.append(self.generar_fills_botar())
        lista_fills.append(self.generar_fills_desplacar())
        lista_fills.append(self.generar_fills_girar())