from datetime import datetime

class Fahrzeug:

    # Klassenattribute
    anzahl_fahrzeuge = 0
    WAHRUNG = "EUR"

    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        Fahrzeug.anzahl_fahrzeuge += 1
    
    def zeige_info(self):

        return f"Marke: {self.marke}, Modell: {self.modell}, Baujahr: {self.baujahr}"

    def __str__(self):
         return f"Marke: {self.marke}, Modell: {self.modell}, Baujahr: {self.baujahr}"

    @classmethod
    def get_anzahl_fahrzeuge(cls):

        return f"Gesamtzahl der Fahrzeuge: {cls.anzahl_fahrzeuge}"
    
    @classmethod
    def fahrzeug_aus_string(cls, fahrzeug_string):
        "BMW-X3-2005"
        marke,modell,baujahr = fahrzeug_string.split('-')
        return cls(marke, modell, int(baujahr))

    @staticmethod
    def ist_aktuelles_jahr(jahr):

        aktuelles_jahr = datetime.now().year
        return jahr == aktuelles_jahr