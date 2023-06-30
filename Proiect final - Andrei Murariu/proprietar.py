class Proprietar:
    def __init__(self, nume, gen, cnp, nr_telefon):
        self.nume = nume
        self.gen = gen
        self._cnp = cnp
        self.nr_telefon = nr_telefon
        self.animale = []

    def __str__(self):
        return f'Numele proprietarului este {self.nume} si are numarul de telefon: {self.nr_telefon}'

    def get_cnp(self):
        return self._cnp

    def verifica_animal(self, hotel):
        print(f'Proprietarul {self.nume} suna la hotel sa isi verifice animalele.')
        hotel.raspunde_apel(self)
