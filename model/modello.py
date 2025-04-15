import copy

from database.meteo_dao import MeteoDao

class Model:

    def __init__(self):
        self.costoOttimo = -1
        self.soluzioneOttima = []

    def umiditaMedia(self, mese):
        return MeteoDao.get_all_situazioni(mese)

    def calcola_sequenza(self, mese):
        situazioni = MeteoDao.get_situazioni_meta_mese(mese)
        self._ricorsione([],situazioni)
        return self.soluzioneOttima, self.costoOttimo

    def trova_possibili_step(self, parziale, lista_situazioni):
        giorno = len(parziale) + 1
        candidati = []
        for situazione in lista_situazioni:
            if situazione.data.day == giorno:
                candidati.append(situazione)
        return candidati

    def is_admissible(self, candidate, parziale):
        counter = 0
        for situazione in parziale:
            if situazione.localita == candidate.localita:
                counter += 1
        if counter >= 6:
            return False
        if len(parziale) == 0:
            return True
        if len(parziale) < 3:
            if candidate.localita != parziale[0].localita:
                return False
        else:
            if parziale[-3].localita != parziale[-2].localita or parziale[-3].localita != parziale[-1].localita or parziale[-2].localita != parziale[-1].localita:
                if parziale[-1].localita != candidate.localita:
                    return False

    def _calcolaCosto(self, parziale):
        costo = 0
        for situazione in parziale:
            costo += situazione.umidita
        for i in range(len(parziale)):
            if i >= 2 and (parziale[i - 1].localita != parziale[i].localita or parziale[i - 2].localita != parziale[i].localita):
                costo += 100
        return costo

    def _ricorsione(self, parziale, lista_situazioni):
        if len(parziale) == 15:
            costo = self._calcolaCosto(parziale)
            if self.costoOttimo == -1 or self.costoOttimo > costo:
                self.costoOttimo = costo
                self.soluzioneOttima = copy.deepcopy(parziale)
        else:
            candidates = self.trova_possibili_step(parziale, lista_situazioni)
            for candidate in candidates:
                if self.is_admissible(candidate, parziale):
                    parziale.append(candidate)
                    self._ricorsione(parziale, lista_situazioni)
                    parziale.pop()


if __name__ == "__main__":
    mod = Model()
    print(mod.calcola_sequenza(1))

