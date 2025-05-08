import matplotlib.pyplot as plt
#Liniendiagramm

# Jahre
jahre = [2019, 2020, 2021, 2022, 2023]

# Umsatzdaten für zwei Produkte
umsatz_apfel = [50, 65, 80, 90, 100]
umsatz_banane = [40, 60, 70, 85, 95]

# Linien zeichnen
plt.plot(jahre, umsatz_apfel, label='Apfel', marker='o', color='red')
plt.plot(jahre, umsatz_banane, label='Banane', marker='s', color='blue')

# Titel und Beschriftungen
plt.title("Umsatzentwicklung pro Jahr")
plt.xlabel("Jahr")
plt.ylabel("Umsatz in Tsd. €")
plt.legend()

# Zwei Linien: Eine für Apfel, eine für Banane
# marker='o' bzw. marker='s' zeigen Punkte auf der Linie (Kreis / Quadrat)
# plt.legend() zeigt, welche Linie zu welchem Produkt gehört
# plt.grid(True) fügt ein Gitternetz hinzu

# Diagramm anzeigen
plt.grid(True)
plt.show()
