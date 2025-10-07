class Noleggio:
    def __init__(self, ID, data, IDAuto, cognomeCliente):
        self.ID = ID
        self.data = data
        self.IDAuto = IDAuto
        self.cognomeCliente = cognomeCliente

    def __str__(self):
        return f"ID: {self.ID} Data: {self.data} ID Auto: {self.IDAuto} Cognome Cliente: {self.cognomeCliente}"
