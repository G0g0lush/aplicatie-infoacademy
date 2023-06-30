import random
from animal import Animal


class Caine(Animal):
    def __init__(self, nume, varsta, proprietar, rasa):
        super().__init__(nume, varsta, proprietar, rasa)

    def __str__(self):
        return f'Pe acest caine il cheama {self.nume} si are {self.varsta} ani.'

    def latra(self):
        latrat = random.choice(["How-how!", "Ham"])
        print(self.nume + ": " + latrat)

    def da_din_coada(self):
        print(self.nume + " da din coada de fericire.")
