import matplotlib.pyplot as plt
#Balkendiagramm

# Daten
produkte = ['Apfel', 'Banane', 'Kirsche', 'Dattel']
verkaeufe = [50, 75, 30, 45]

# Diagramm erstellen
plt.bar(produkte, verkaeufe, color='green')

# Titel und Beschriftungen
plt.title("Verkäufe pro Produkt")
plt.xlabel("Produkt")
plt.ylabel("Anzahl verkauft")

# Diagramm anzeigen
plt.show()
