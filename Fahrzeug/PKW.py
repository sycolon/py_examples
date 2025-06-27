from Fahrzeug import Fahrzeug

class PKW(Fahrzeug):
    
    def __init__(self, marke, modell, baujahr, anzahl_tueren):
        super().__init__(marke, modell, baujahr)
        self.anzahl_tueren = anzahl_tueren
    
    def zeige_info(self):
        basic_info = super().zeige_info()
        return f"{basic_info}, Türen: {self.anzahl_tueren}"
    
    def ist_familienauto(self):

        return self.anzahl_tueren >= 4
    
    def __str__(self):
        return f"{super().__str__()}, Türen: {self.anzahl_tueren}"
    