import csv
from automobile import Automobile

class Autonoleggio:

    listaAutomobili = []

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._responsabile = responsabile
        
        @property       #getter
        def nome(self):
            return self._nome

        def responsabile(self):
            return self._responsabile

        @nome.setter    #setter
        def nome(self, nome):
            self._nome = nome

        @responsabile.setter      #setter
        def responsabile(self, responsabile):
            self._responsabile = responsabile


    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)

                for row in reader:
                    a = Automobile(row[0], row[1], row[2], row[3], row[4])
                    Autonoleggio.listaAutomobili.append(a)

            return Autonoleggio.listaAutomobili

        except FileNotFoundError:
            print('File not found')


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        try:
            ID = f"A{len(Autonoleggio.listaAutomobili)+1}"
            Autonoleggio.listaAutomobili.append(Automobile(ID, marca, modello, anno, num_posti))

            return Autonoleggio.listaAutomobili



    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
