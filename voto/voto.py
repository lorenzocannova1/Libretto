import operator
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

    def copy(self):
        return Voto(self.materia, self.punteggio, self.lode, self.data)

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self,voto):
        if self.hasConflitto(voto) == False and self.hasVoto(voto) == False:
            self.voti.append(voto)
        else:
            raise ValueError("Il voto è già presente")

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

    def hasVoto(self,voto):
        for v in self.voti:
                if v.materia == voto.materia and v.punteggio == voto.punteggio and v.lode == voto.lode:
                    return True
        return False

    def hasConflitto(self,voto):
        for v in self.voti:
            if v.materia == voto.materia and not (v.punteggio == voto.punteggio and v.lode == voto.lode):
                return True
        return False

    def copy(self):
        newLib = Libretto(self.proprietario.copy(), [])
        for v in self.voti:
            newLib.append(v.copy())
        return newLib

    def creaMigliorato(self):
        MyNewLib = self.copy()

        for v in MyNewLib.voti:
            if v.punteggio >= 18 and v.punteggio <= 24:
                v.punteggio += 1
            elif v.punteggio >= 25 and v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio += 1

        return MyNewLib

    def sortByMateria(self):
        #self.voti.sort(key=estraiMateria)
        self.voti.sort(key=operator.attrgetter("materia"))

    def creaLibOrdinatoPerMateria(self):
        nuovo = self.copy()
        nuovo.sortByMateria()
        return nuovo

    def creaLibOrdinatoPerVoto(self):
        #Adesso faccio tutto insieme, il sort e la stampa
        nuovo = self.copy()
        nuovo.voti.sort(key = lambda v: (v.punteggio, v.lode), reverse = True)
        return nuovo

    def cancellaInferiori(self,punteggio):
        nuovo = []
        for v in self.voti:
            if v.punteggio >= punteggio:
                nuovo.append(v)

        self.voti = nuovo

def estraiMateria(voto):
        return voto.materia


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