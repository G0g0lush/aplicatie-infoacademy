class Animal:

    def __init__(self, nume, varsta, proprietar, rasa):
        self.nume = nume
        self.varsta = varsta
        self.proprietar = proprietar
        self.rasa = rasa

    def __str__(self):
        return f'Numele animalului este {self.nume} si are proprietarul {self.proprietar.nume}.'

    def get_nume(self):
        return self.nume

    def get_varsta(self):
        return self.varsta

    def get_proprietar(self):
        return self.proprietar
