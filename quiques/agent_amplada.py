from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca, SENSOR


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def cerca_general(self):
        X = Estat(0,3,3,)
        self.__oberts = [X]
        self.__tancats = []
        while self.__oberts:
            X = self.__oberts.pop(0)
            if X.es_meta():
                return True, self.__oberts
            else:
                fills = X.genera_fill()
                # recorrer fills y remove los malos
                self.__tancats.append(X)
                self.__oberts += fills
        return False


    def actua(
            self, percepcio: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        return do()
