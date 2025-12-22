from dataclasses import dataclass
from encodings import normalize_encoding


@dataclass
class Voto:
    materia: str
    punteggio: int
    lode: bool
    data: str

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e Lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self,voto):
        self.voti.append(voto)

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    def __len__(self):
        return len(self.voti)

    def calcolaMedia(self):
        """
        restituisce la media dei voti attualmente presenti nel libretto
        :return: restituisce la media dei voti oppure ValueError in caso la lista fosse vuota
        """
        if len(self.voti) == 0:
            raise ValueError("Attenzione, lista esami vuota")
        v = [v1.punteggio for v1 in self.voti]
        return sum(v)/len(v)

    def getVotiByPunti(self,punti, lode):
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode:
                votiFiltrati.append(v)

        return votiFiltrati

    def getVotoByName(self,nome):
        for v in self.voti:
            if v.materia == nome:
                return v

        return None


def testVoto():
        print("Ho usato voto in maniera standalone")
        v1 = Voto("Trasfigurazione", 24, False, "2022-02-13")
        v2 = Voto("Pozioni", 30, True, "2022-02-13")
        v3 = Voto("Difesa contro le arti oscure", 27, False, "2022-04-13")
        myLib = Libretto(None, [v1, v2])
        print(myLib)
        myLib.append(v3)
        print(myLib)

if __name__ == "__main__":
    testVoto()