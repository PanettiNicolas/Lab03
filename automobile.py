class Automobile:
    def __init__(self, ID, marca, modello, annoImmatricolazione, numPosti):
        self.ID = ID
        self.marca = marca
        self.modello = modello
        self.annoImmatricolazione = annoImmatricolazione
        self.numPosti = numPosti

    def __str__(self):
        return f"ID: {self.ID} Marca: {self.marca} Modello: {self.modello} Anno immatricolazione: {self.annoImmatricolazione} Numero posti: {self.numPosti} "

