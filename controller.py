from view import View
from voto import *
from voto.voto import Libretto, Voto
from scuola import Student
import flet as ft

class Controller:
    def __init__(self, v:View):
        self._view = v
        self._student = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
        self._model = Libretto(self._student,[])
        self._fillLibretto()

    def handleAggiungi(self,e):
        nome = self._view._txtInNome.value
        if nome == "":
            self._view._txtOut.controls.append(ft.Text("Attenzone il campo nome non può essere vuoto", color = "red"))
            self._view._page.update()
            return

        punti = self._view._ddVoto.value
        if punti is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione, selezionare un voto",color="red"))
            self._view._page.update()
            return

        data = self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione, selezionare una data", color = "red"))
            self._view._page.update()
            return

        if punti == "30L":
           self._model.append(Voto(nome,30,True,f"{data.year}-{data.month}-{data.day}"))
        else:
            self._model.append(Voto(nome,int(punti),False,f"{data.year}-{data.month}-{data.day}"))

        self._view._txtOut.controls.append(ft.Text("Voto correttamente aggiuntivo",color = "green"))
        self._view._page.update()

    def handleStampa(self,e):
        self._view._txtOut.controls.append(ft.Text(str(self._model)))
        self._view._page.update()

    def getStudent(self):
        return str(self._student)

    def _fillLibretto(self):
        v1 = Voto("Difesa contro le arti oscure", 25, False, "2022-04-13")
        v2 = Voto("Babbanologia", 21, False, "2022-02-12")
        v3 = Voto("Pozioni", 21, False, "2022-06-14")
        v4 = Voto("Aritmanzia", 30, False, "2024-04-13")
        self._model.append(v1)
        self._model.append(v2)
        self._model.append(v3)
        self._model.append(v4)



