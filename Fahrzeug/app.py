from Fahrzeug import Fahrzeug
from PKW import PKW

f1 = Fahrzeug("Audi","A6", 2020)
f2 = Fahrzeug("VW","Golf", 2020)
f3 = Fahrzeug("VW","Passat", 2021)
f4 = Fahrzeug("Audi","A3", 2024)
f5 = Fahrzeug("Audi","A4", 2023)
print(f1.zeige_info())

auto3 = Fahrzeug.fahrzeug_aus_string("BMW-320d-2003")
print(auto3.zeige_info())

pkw1 = PKW("Fiat","Scudo",2008,4)
pkw2 = PKW("VW","Golf",2009,2)

print(pkw1.zeige_info())
print(pkw2.zeige_info())

print(f"Ist {pkw1.marke} {pkw1.modell} ein Familienauto? {pkw1.ist_familienauto()}")
print(f"Ist {pkw2.marke} {pkw2.modell} ein Familienauto? {pkw2.ist_familienauto()}")

print(f"Ist 2025 das aktuelle Jahr? {Fahrzeug.ist_aktuelles_jahr(2025)}")
print(f"Ist 2021 das aktuelle Jahr? {Fahrzeug.ist_aktuelles_jahr(2021)}")

print(pkw1)

print(Fahrzeug.get_anzahl_fahrzeuge())