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

    def generar_fills_botar(self) -> list:
        lista_botar = []
        for i in self.monedes:
            estatAux = self

            if abs(i - self.posEspai) == 2: # Tiene que haber una moneda entre el espacio y la moneda que salta
                # Si la moneda que salta es una C, se cambia por una X y viceversa
                if estatAux.monedes[i] == "C":
                    estatAux.monedes[i], estatAux[self.posEspai] = " ", "X"
                    estatAux.accions_previstes.append("BOTAR")
                    lista_botar.append(estatAux)

                elif estatAux.monedes[i] == "X":
                    estatAux.monedes[i], estatAux[self.posEspai] = " ", "C"
                    estatAux.accions_previstes.append("BOTAR")
                    lista_botar.append(estatAux)

        return lista_botar

    def generar_fills_desplacar(self) -> list:
        lista_desplacar = []
        for i in self.monedes:
            estatAux = self

            if (i-1 == self.posEspai) | (i+1 == self.posEspai): # La moneda tiene que estar adyacente al espacio
                # Se intercambian la moneda y el espacio
                estatAux.monedes[i], estatAux[self.posEspai] = estatAux[self.posEspai], estatAux.monedes[i]
                estatAux.accions_previstes.append("BOTAR")
                lista_desplacar.append(estatAux)

        return lista_desplacar

    def generar_fills_girar(self) -> list:
        lista_girar = []
        for i in self.monedes:
            estatAux = self

            if estatAux.monedes[i] == "C":
                estatAux.monedes[i] = "X"
                estatAux.accions_previstes.append("GIRAR")
                lista_girar.append(estatAux)

            elif estatAux.monedes[i] == "X":
                estatAux.monedes[i] = "C"
                estatAux.accions_previstes.append("GIRAR")
                lista_girar.append(estatAux)
        return lista_girar


    def generar_fills(self) -> list:
        lista_fills = []
        lista_fills.append(self.generar_fills_botar())
        lista_fills.append(self.generar_fills_desplacar())
        lista_fills.append(self.generar_fills_girar())