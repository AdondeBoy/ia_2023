""" Fitxer que conté l'agent barca en profunditat.

S'ha d'implementar el mètode:
    actua()
"""
from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca, SENSOR


class BarcaProfunditat(Barca):
    def __init__(self):
        super(BarcaProfunditat, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def actua(
            self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat = Estat(percepcio[SENSOR.LLOC], 3, 3)

        if self.__accions is None:
            self.cerca_profunditat(estat)
        if len(self.__accions) == 0:
            return AccionsBarca.ATURAR
        else:
            return AccionsBarca.MOURE, self.__accions.pop()

    def cerca_profunditat(self, estat: Estat):
        self.__oberts = [estat]
        self.__tancats = []
        while self.__oberts != []:
            estat = self.__oberts.pop(0)
            if estat in self.__tancats:
                continue
            if estat.es_segur():
                if estat.es_meta():
                    self.__accions = estat.accions_previes
                    return True
                else:
                    fills = estat.genera_fill()

                    self.__tancats.append(estat)
                    for fill in fills:
                        if fill not in self.__tancats:
                            self.__oberts.insert(0, fill)
            else:
                self.__tancats.append(estat)
        return False
