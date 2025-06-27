# wir haben Autohandel GmbH, dafür werden wir alle Autos im Autohaus erfassen und zählen.

# Autos:
        # Marke
        # farbe
        # Anzahl Sitze
    #wie viele Autos sind vorhanden?

# PascalCase
# camelCase
# snake_case
# kepap-case

class Car:
    __autosAnzahl = 0 #Klassen Attribut
    def __init__(self, farbe = None, anzahlSitze= None, FIN = None):
        #self.marke = marke
        self.farbe = farbe
        self.anzahlSitze = anzahlSitze
        self.FIN = FIN
        Car.__autosAnzahl += 1
    
    def __str__(self):
        return f" Farbe: {self.farbe}, Sitze Anzahl: {self.anzahlSitze}, FIN: {self.FIN}"
    
    def printCarInfo(self):
        return f"Farbe: {self.farbe}, Sitze Anzahl: {self.anzahlSitze}"
    
    @classmethod
    def getAutosAnzahl(cls):
        return cls.__autosAnzahl

    @staticmethod
    def is_valid_FIN(fin):
        """Prüft, ob die FIN gültig ist (17 alphanumerische Zeichen, keine I/O/Q)"""
        if not isinstance(fin, str) or len(fin) != 17:
            return False
        invalid_chars = {'I', 'O', 'Q'}
       #return all(c.isalnum() and c.upper() not in invalid_chars for c in fin)
        for c in fin:
            if not c.isalnum():
                return False
            if c.upper() in invalid_chars:
                return False
        return True

    
class Audi(Car):
    marke = "Audi"
    audiAutosAnzahl = 0 #Klassen Attribut
    def __init__(self, farbe=None, anzahlSitze=None, FIN=None, hasQuattro = None):
        super().__init__(farbe, anzahlSitze, FIN)
        self.hasQuattro = hasQuattro
        Audi.audiAutosAnzahl += 1
    
    def __str__(self):
        return f"Marke: {Audi.marke}" +  super().__str__() + f"has Quattro: {self.hasQuattro}"
    
    def __del__(self):
        Audi.audiAutosAnzahl -= 1

    pass

class VW(Car):
    # Hier werden Klassen Attribute definiert
    marke = "Volkswagen" #Klassen Attribute
    vwAutosAnzahl = 0
    def __init__(self, farbe=None, anzahlSitze=None, FIN=None):
        super().__init__(farbe, anzahlSitze, FIN)
        VW.vwAutosAnzahl += 1
    
    def __str__(self):
        return  f"Marke: {VW.marke}" + super().__str__()
    pass

class Skoda(Car):
    Marke = "Skoda"
    
    pass

class BMW(Car):
    Marke = "BMW"
    
    pass

a3= Audi("Rot", 5, "WAH237423KJHK", True)
print(a3)
c1 = Audi( "Black", 5, "WW03234kjsdkf03o4", False)
print(c1)
#print(c1.autosAnzahl)
c2 = VW()
#print(c2)
c3 = Audi( "Black", 5, "WW4534k453jsdkf03o4",True)
print(c3)
print(c1.printCarInfo())

# print(f"Autos Anzahl im Haus: {c1.autosAnzahl}")
# print(f"Autos Anzahl im Haus: {c2.autosAnzahl}")
# print(f"Autos Anzahl im Haus: {c3.autosAnzahl}")

print(f"Autos Anzahl im Haus: {Car.getAutosAnzahl()}")
print(f"Autos Anzahl im Haus: {Audi.getAutosAnzahl()}")
print(f"Audi Anzahl im Haus: {Audi.audiAutosAnzahl}")
print(f"VW Anzahl im Haus: {VW.vwAutosAnzahl}")

del(c1)

print(f"Audi Anzahl im Haus: {Audi.audiAutosAnzahl}")
print(Car.is_valid_FIN("WDB1234561A654321"))
print(Car.is_valid_FIN("WDB1234561O654321"))
print(Car.is_valid_FIN("WDB1234561t654321"))

cc = Audi("Black", 5,"WW27365418ZH72653",True)

zz = cc # Casting zz wird wie cc behandelt
zz.getAutosAnzahl()

car1 = Car()

cc = Car(car1)


x = 1
y = 2.8
txt = "43"

print(int(x))
print(int(y))
print(int(txt))
