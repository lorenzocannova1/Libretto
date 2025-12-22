from voto.voto import Voto, Libretto

v1 = Voto("Trasfigurazione", 24, False, "2022-02-13")
v2 = Voto("Pozioni", 30, True, "2022-02-13")
v3 = Voto("Difesa contro le arti oscure", 27, False, "2022-04-13")

myLib = Libretto(None, [v1,v2])
print(myLib)
myLib.append(v3)
print(myLib)
