class Person:
    def __init__(self, nome, cognome, eta, capelli, occhi, casa, incantesimo="Non ancora definito"):
        self.nome = nome
        self._cognome = cognome
        self.eta = eta
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.__prova = None
        self.incantesimo = incantesimo

    def __str__(self):
        return f"{self.nome} - {self._cognome}"

    @property
    def cognome(self): #equivale al GETTER
        return self._cognome
    @cognome.setter #equivale al SETTER
    def cognome(self,value):
        #eventuali controlli per verificare che value sia compatibile con cognome
        self._cognome = value

class Student(Person):
    def __init__(self, nome, cognome, eta, capelli, occhi, casa, animale, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.animale = animale

    def __str__(self):
        return f"Studente: {self.nome} - {self._cognome} - {self.casa}"

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
            stringa = f"La casa {self.nome} è vuota"
        stringa =  f"Lista degli studenti iscritti alla casa {self.nome} \n"
        for s in self.studenti:
            stringa += str(s) + "\n"
        return stringa

class Scuola:
    def __init__(self, case):
        self.case = case

        def __str__(self):
            mystr = ""
            for c in self.case:
                mystr += str(c)
            return mystr