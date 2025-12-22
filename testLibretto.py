from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
myLib = Libretto(Harry)

v1 = Voto("Difesa contro le arti oscure", 25, False, "2022-04-13")
v2 = Voto("Babbanologia", 21, False, "2022-02-12")
myLib.append(v1)
myLib.append(v2)
myLib.append(Voto("Pozioni",21,False, "2022-06-14"))

print(f"La media è {myLib.calcolaMedia()}")

print(f"{myLib.getVotiByPunti(21,False)}")
print(f"{myLib.getVotoByName("Pozioni")}")