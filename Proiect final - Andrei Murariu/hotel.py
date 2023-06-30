import json
from caine import Caine
from pisica import Pisica
from proprietar import Proprietar


class Hotel:
    def __init__(self, nume: str, numar_pisici_maxim: int, numar_caini_maxim: int, camere_izolate: int):
        self.nume = nume
        self.numar_pisici_maxim = numar_pisici_maxim
        self.numar_caini_maxim = numar_caini_maxim
        self.pisici_cazate = []
        self.caini_cazati = []
        self.camere_izolate = camere_izolate
        self.filename = 'date_hotel.json'
        data = [{"nume": self.nume, "numar_pisici_maxim": self.numar_pisici_maxim,
                 "numar_pisici_cazate": len(self.pisici_cazate), "camere_izolate": self.camere_izolate,
                 "numar_caini_maxim": self.numar_caini_maxim, "numar_caini_cazati": len(self.caini_cazati)}]
        with open(self.filename, "w") as handle:
            json.dump(data, handle)

    def __str__(self):
        return f'Hotelul {self.nume} mai are {self.numar_pisici_maxim - len(self.pisici_cazate)} locuri de pisici si ' \
               f'{self.numar_caini_maxim - len(self.caini_cazati)} locuri de caini disponibile.'

    """
    metoda de cazare pisici; se verifica daca pisica este agresiva sau neagresiva, apoi se verifica locurile disponibile
    si in functie de acest lucru pisica este cazata sau nu. pisicile miauna cand sunt cazate.
    detalile cazarii sunt scrise in fisierul json.
    """
    def cazare_pisica(self, pisica: Pisica):
        if len(self.pisici_cazate) < self.numar_pisici_maxim:
            if pisica.get_agresiva():
                if len([pisica for pisica in self.pisici_cazate if pisica.get_agresiva()]) < self.camere_izolate:
                    self.pisici_cazate.append(pisica)
                    print(f"Pisica {pisica.nume} a fost cazata!")
                    pisica.miauna()
                else:
                    print('Numarul maxim de pisici agresive a fost atins!')
            else:
                self.pisici_cazate.append(pisica)
                print(f"Pisica {pisica.nume} a fost cazata!")
                pisica.miauna()
            with open(self.filename, "r") as f:
                data = json.load(f)
            data[0]["numar_pisici_cazate"] = len(self.pisici_cazate)
            with open(self.filename, "w") as handle:
                json.dump(data, handle)
        else:
            print('Numarul maxim de pisici a fost atins!')

#metoda de decazare pisici; dupa ce pisica a fost decazata, aceasta se sterge din fisierul json
    def decazare_pisica(self, pisica: Pisica):
        self.pisici_cazate.remove(pisica)
        with open(self.filename, "r") as f:
            data = json.load(f)
            data[0]["numar_pisici_cazate"] = len(self.pisici_cazate)
        with open(self.filename, "w") as handle:
            json.dump(data, handle)
        if pisica.get_agresiva:
            pisica.set_agresiva(False)
        print(f"Pisica {pisica.nume} a fost decazata")

    """
    metoda de cazare caini; se verifica daca numarul de caini maxim a fost atins, daca nu cainele este cazat.
    dupa ce cainele a fost cazat se adauga in fisierul json. cainele latra cand este cazat
    """
    def cazare_caine(self, caine: Caine):
        if len(self.caini_cazati) < self.numar_caini_maxim:
            self.caini_cazati.append(caine)
            print(f"Cainele {caine.nume} a fost cazat!")
            caine.latra()
            with open(self.filename, "r") as f:
                data = json.load(f)
                data[0]["numar_caini_cazati"] = len(self.caini_cazati)
            with open(self.filename, "w") as handle:
                json.dump(data, handle)
        else:
            print('Numarul maxim de caini a fost atins!')

#metoda de decazare caini; cand cainii sunt decazati sunt stersi si din fisierul json.
    def decazare_caine(self, caine: Caine):
        self.caini_cazati.remove(caine)
        with open(self.filename, "r") as f:
            data = json.load(f)
            data[0]["numar_caini_cazati"] = len(self.caini_cazati)
        with open(self.filename, "w") as handle:
            json.dump(data, handle)
        print(f"Cainele {caine.nume} a fost decazat.")
        caine.da_din_coada()

#se verifica daca proprietarul are animale cazate la hotel si in functie de acest aspect primeste raspuns
    def raspunde_apel(self, proprietar: Proprietar):
        animale_cazate_proprietar = 0
        for pisica in self.pisici_cazate:
            if pisica.proprietar == proprietar:
                print(f'Pisica {pisica.nume} este bine, sanatoasa')
                animale_cazate_proprietar += 1
        for caine in self.caini_cazati:
            if caine.proprietar == proprietar:
                print(f'Cainele {caine.nume} este bine, sanatoasa')
                animale_cazate_proprietar += 1
        if animale_cazate_proprietar == 0:
            print(f"Nu aveti animale cazate la hotelul {self.nume}")