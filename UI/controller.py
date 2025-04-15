import flet as ft

from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self._mese = 0

    def handle_umidita_media(self, e):
        self._view.lst_result.clean()
        info = self._model.umiditaMedia(self._mese)
        umiditaTorino = 0
        umiditaMilano = 0
        umiditaGenova = 0
        numInfoTorino = 0
        numInfoMilano = 0
        numInfoGenova = 0
        for situazione in info:
            if situazione.localita == "Torino":
                umiditaTorino += situazione.umidita
                numInfoTorino += 1
            elif situazione.localita == "Milano":
                umiditaMilano += situazione.umidita
                numInfoMilano += 1
            else:
                umiditaGenova += situazione.umidita
                numInfoGenova += 1
        self._view.lst_result.controls.append(ft.Text(f"L'umidità media nel mese selezionato è:"))
        self._view.lst_result.controls.append(ft.Text(f"Genova: {round(umiditaGenova/numInfoGenova, 4)}"))
        self._view.lst_result.controls.append(ft.Text(f"Milano: {round(umiditaMilano/numInfoMilano, 4)}"))
        self._view.lst_result.controls.append(ft.Text(f"Torino: {round(umiditaTorino/numInfoTorino, 4)}"))
        self._view.update_page()


    def handle_sequenza(self, e):
        self._view.lst_result.clean()

    def read_mese(self, e):
        self._mese = int(e.control.value)

