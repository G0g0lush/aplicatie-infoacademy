"""
Main-ul aplicatiei, unde verificam functionalitatea acesteia.
In primul rand se importa cele 4 clase: Hotel, Caine, Pisica si Proprietar.
Pentru a crea un hotel folosim: nume = Hotel("nume_hotel, numar maxim pisici, numar maxim caini, camere izolate \
(pentru pisici agresive))
Pentru a crea o pisica folosim: nume = Pisica("nume_pisica", varsta, proprietar, True/False(agresiva/neagresiva), rasa)
Pentru a crea un caine folosim: nume = Caine("nume_caine", varsta, proprietar, rasa)
Pentru a crea un proprietar folosim: nume = Proprietar("nume_proprietar", "geb", "cnp", "nr telefon")

Dupa ce cream aceste elemente, putem folosi urmatoarele actiuni:
1. Sa cazam pisicile sau cainii cu urmatoarele comenzi: nume_hotel.cazare_pisica(nume_pisica) \
nume_hotel.cazare_caine(nume_caine)
2. Sa decazam pisicile sau cainii cu urmatoarele comenzi: nume_hotel.decazare_pisica(nume_pisica) \
nume_hotel.decazare_caine(nume_caine)
3. Sa verificam animalutul de companie cu comanda: nume_proprietar.verifica_animal(nume_hotel)

Aplicatia va crea un fisier json care va cuprinde detalii despre hotel
"""

from caine import Caine
from hotel import Hotel
from pisica import Pisica
from proprietar import Proprietar


if __name__ == '__main__':
    hotel = Hotel("Tipton", 4, 5, 2)
    andrei = Proprietar("Andrei", "masculin", "1953953035", "0723364456")
    mufasa = Pisica("Mufasa", 3, andrei, False, "tomberonez")
    leia = Pisica("Leia", 2, andrei, True, "tomberonez")
    toto = Pisica("Toto", 3, andrei, True, "tomberonez")
    kiti = Pisica("Kiti", 2, andrei, True, "tomberonez")
    george = Proprietar("George", "masculin", "192522553", "0742422552")
    azorel = Caine("Azorel", "7", george, "husky")
    gicu = Caine("Gicu", "13", george, "bichon")
    deliuta = Proprietar("Deliuta", "feminin", "2964646464", "0724252664")
    hotel.cazare_pisica(mufasa)
    hotel.cazare_pisica(leia)
    hotel.cazare_pisica(toto)
    hotel.cazare_pisica(kiti)
    hotel.cazare_caine(azorel)
    hotel.cazare_caine(gicu)
    andrei.verifica_animal(hotel)
    deliuta.verifica_animal(hotel)
    hotel.decazare_pisica(toto)
    hotel.decazare_caine(gicu)
    print(mufasa)
    print(deliuta)
    print(azorel)
    print(hotel)
