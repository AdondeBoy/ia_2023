""" Mòdul que conté l'agent per jugar al joc de les monedes.

Percepcions:
    ClauPercepcio.MONEDES
Solució:
    " XXXC"
"""

from ia_2022 import agent, entorn

SOLUCIO = " XXXC"
INICIAL = "CX CX"


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
        estat = Estat()

class Estat:
    def __init__(self, accions_previes = None) -> None:
        if accions_previes is None:
            accions_previes = []

        self.monedes = []
        self.accions_previes = accions_previes
        self.posEspai = self.monedes.index(" ")
        self.cost = 0

    def generar_fills_botar(self) -> list:
        lista_botar = []
        for i in self.monedes:
            estatAux = self
            estatAux.cost += 3

            if abs(i - self.posEspai) == 2: # Tiene que haber una moneda entre el espacio y la moneda que salta
                # Si la moneda que salta es una C, se cambia por una X y viceversa
                if estatAux.monedes[i] == "C":
                    estatAux.monedes[i], estatAux[self.posEspai] = " ", "X"
                    estatAux.accions_previes.append("BOTAR")
                    lista_botar.append(estatAux)

                elif estatAux.monedes[i] == "X":
                    estatAux.monedes[i], estatAux[self.posEspai] = " ", "C"
                    estatAux.accions_previes.append("BOTAR")
                    lista_botar.append(estatAux)

                AgentMoneda.__oberts.put((0, estatAux))
        return lista_botar

    def generar_fills_desplacar(self) -> list:
        lista_desplacar = []
        for i in self.monedes:
            estatAux = self
            estatAux.cost += 1

            if (i-1 == self.posEspai) | (i+1 == self.posEspai): # La moneda tiene que estar adyacente al espacio
                # Se intercambian la moneda y el espacio
                estatAux.monedes[i], estatAux[self.posEspai] = estatAux[self.posEspai], estatAux.monedes[i]
                estatAux.accions_previes.append("BOTAR")
                lista_desplacar.append(estatAux)
                AgentMoneda.__oberts.put((0, estatAux))

        return lista_desplacar

    def generar_fills_girar(self) -> list:
        lista_girar = []
        for i in self.monedes:
            estatAux = self
            estatAux.cost += 2

            if estatAux.monedes[i] == "C":
                estatAux.monedes[i] = "X"
                estatAux.accions_previes.append("GIRAR")
                lista_girar.append(estatAux)
                AgentMoneda.__oberts.put((0, estatAux))

            elif estatAux.monedes[i] == "X":
                estatAux.monedes[i] = "C"
                estatAux.accions_previes.append("GIRAR")
                lista_girar.append(estatAux)
                AgentMoneda.__oberts.put((0, estatAux))

        return lista_girar

    def calcular_heuristica(self) -> int:
        h = abs(self.posEspai - SOLUCIO.index(" ")) # p0
        for i in self.monedes: # vx
            if self.monedes[i] == " ":
                continue
            if self.monedes[i] != SOLUCIO[i]:
                h += 1
        return h

    def generar_fills(self) -> list:
        lista_fills = []
        lista_fills.append(self.generar_fills_desplacar()) # Coste 1
        lista_fills.append(self.generar_fills_girar()) # Coste 2
        lista_fills.append(self.generar_fills_botar()) # Coste 3
        return lista_fills