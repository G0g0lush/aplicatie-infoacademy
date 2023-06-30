import random
from animal import Animal
from proprietar import Proprietar


class Pisica(Animal):
    def __init__(self, nume: str, varsta: int, proprietar: Proprietar, agresiva: bool, rasa: str):
        super().__init__(nume, varsta, proprietar, rasa)
        self._agresiva = agresiva

    def __str__(self):
        return f'Pe aceasta pisica frumoasa o cheama {self.nume} si are {self.varsta} ani.'

    def miauna(self):
        mieunat = random.choice(["Miau!", "Prrr", "Woah-woah"])
        print(self.nume + ": " + mieunat)

    def set_agresiva(self, agresiva: bool):
        self._agresiva = agresiva

    def get_agresiva(self):
        return self._agresiva
