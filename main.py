# Harry = ["Harry", "Potter", 11, "Capelli castani", "Occhi azzurri", "Grifondoro", ""]
#
# print("Il nome è: " + Harry[0])
# Harry[6] = "Expecto Patronum"
# print(Harry)
#
# Ron = ["Ron", "Weasley", 11, "Capelli rossi", "Occhi marroni", "Grifondoro", ""]
#
# Grifondoro = [Harry, Ron]

class Person:
    def __init__(self, nome, cognome, eta, capelli, occhi, casa, incantesimo="Non ancora definito"):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.incantesimo = incantesimo

    def __str__(self):
        return f"{self.nome} - {self.cognome}"

class Student(Person):
    def __init__(self, nome, cognome, eta, capelli, occhi, casa, animale, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.animale = animale

    def __str__(self):
        return f"Studente: {self.nome} - {self.cognome} - {self.casa}"

    def __repr__(self):
        return f"Student(nome, cognome, eta, capelli, occhi, casa, animale)"

class Teacher(Person):
    def __init__(self, nome, cognome, eta, capelli, occhi, casa, materia, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.materia = materia

class Casa:
    def __init__(self, nomeCasa, studenti = []):
        self.nome = nomeCasa
        self.studenti = studenti

    def addStudente(self, studente):
        self.studenti.append(studente)

    def __str__(self):
        if len(self.studenti) == 0:
            stringa = "La casa è vuota"
        stringa =  f"Lista degli studenti iscritti alla casa {self.nome} \n"
        for s in self.studenti:
            stringa += str(s) + "\n"
        return stringa


Harry = Person("Harry", "Potter", 11, "castani", "azzurri", "Grifondoro")
Ron = Student("Ron", "Weasley", 11, "Rossi", "Castani", "Grifondoro", "Topo")
Severus = Teacher("Severus", "Snape", 45, "neri","neri", "Serperverde", "Pozioni", "Sectrumsempra")
print(Harry.__str__())
print(Ron.__str__())
print(Severus.__str__())

grinfondoro = Casa("Grinfondoro")
grinfondoro.addStudente(Harry)
grinfondoro.addStudente(Ron)
print(grinfondoro)
print("a")






