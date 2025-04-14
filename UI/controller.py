import flet as ft

from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self._mese = 0

    def handle_umidita_media(self, e):
        pass

    def handle_sequenza(self, e):
        pass

    def read_mese(self, e):
        self._mese = int(e.control.value)

