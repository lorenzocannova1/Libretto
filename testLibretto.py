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

print("Verifico metodo hasVoto")
v3 = Voto("Aritmanzia", 30, False, "2024-04-13")
print(myLib.hasVoto(v3))
print("Verifica metodo conflitto")
print(myLib.hasConflitto(Voto("Difesa contro le arti oscureaaaa", 22, False, "2022-04-13")))

print("Test append modificata")
myLib.append(v3)
#myLib.append(v1) si verifica in conflitto

print("-----------------------------------------")
myLib.append(Voto("Divinazione", 27, False, "2021-02-08"))
myLib.append(Voto("Cura delle creature magiche", 26, False, "2021-06-14"))

print(myLib)
print("Libretto migliorato")
print(myLib.creaMigliorato())
print(myLib)

print("-----------------------------------------")
ordinato = myLib.creaLibOrdinatoPerMateria()
print("Libretto ordinato per materia")
print(ordinato)

print("-----------------------------------------")
ordinato2 = myLib.creaLibOrdinatoPerVoto()
print("Libretto ordinato per voto")
print(ordinato2)

print("-----------------------------------------")
print("Libretto a cui ho eliminato i voti inferiori a 24")
ordinato2.cancellaInferiori(24)
print(ordinato2)