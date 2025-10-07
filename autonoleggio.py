import csv
from automobile import Automobile
from noleggio import Noleggio

class Autonoleggio:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._responsabile = responsabile
        self._listaAutomobili = []
        self._listaNoleggi = []
        self._contatoreNoleggi = 0
        
        @property       #getter
        def nome(self):
            return self._nome

        @property
        def responsabile(self):
            return self._responsabile

        @nome.setter    #setter
        def nome(self, nome):
            self._nome = nome

        @responsabile.setter      #setter
        def responsabile(self, responsabile):
            self._responsabile = responsabile

    def __str__(self):
        return f"{self._nome} ({self._responsabile})"

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)

                for row in reader:
                    a = Automobile(row[0], row[1], row[2], row[3], row[4])
                    self._listaAutomobili.append(a)

            print(f"Le automobili caricate risultano essere")

            for automobile in self._listaAutomobili:
                print(automobile.__str__())

        except FileNotFoundError:
            print('File not found')


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        ID = f"A{len(self._listaAutomobili)+1}"
        self._listaAutomobili.append(Automobile(ID, marca, modello, anno, num_posti))

        return self._listaAutomobili[-1]

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        listaAutomobiliOrdinata = sorted(self._listaAutomobili, key=lambda x: x.marca)

        return listaAutomobiliOrdinata

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        for noleggio in self._listaNoleggi:                     #Verifica disponibilità
            if noleggio.IDAuto == id_automobile:
                raise Exception(f"Automobile {id_automobile} gia' prenotata")

        trovata = False                                         #Verifica effettiva presenza
        for automobile in self._listaAutomobili:
            if automobile.ID == id_automobile:
                trovata = True

        if trovata is False:
            raise Exception(f"Automobile {id_automobile} non trovata")

        self._contatoreNoleggi += 1
        ID = f"N{self._contatoreNoleggi}"
        nuovoNoleggio = Noleggio(ID, data, id_automobile, cognome_cliente)
        self._listaNoleggi.append(nuovoNoleggio)
        return nuovoNoleggio

    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        for noleggio in self._listaNoleggi:
            if noleggio.ID == id_noleggio:
                self._listaNoleggi.remove(noleggio)
                break
        else:
            raise ValueError(f"Noleggio con ID {id_noleggio} non trovato")
