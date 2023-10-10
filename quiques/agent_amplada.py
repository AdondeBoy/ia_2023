from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca, SENSOR


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def cerca_general(self, estat: Estat):
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
                    # recorrer fills y remove los malos
                    self.__tancats.append(estat)
                    self.__oberts += fills
            else:
                self.__tancats.append(estat)
        return False


    def actua(
            self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat = Estat(percepcio[SENSOR.LLOC], 3, 3)

        if self.__accions is None:
            self.cerca_general(estat)
        if len(self.__accions) == 0:
            return AccionsBarca.ATURAR
        else:
            return AccionsBarca.MOURE, self.__accions.pop()
