import matplotlib.pyplot as plt
#Tortendiagramm

# Daten
produkte = ['Apfel', 'Banane', 'Kirsche', 'Dattel']
anteile = [30, 45, 15, 10]

# Diagramm erstellen
plt.pie(anteile, labels=produkte, autopct='%1.1f%%', startangle=90)
# autopct='%1.1f%%' zeigt die Prozentwerte im Diagramm.
#startangle=90 dreht das Diagramm, damit es bei 12 Uhr beginnt.
#plt.axis('equal') sorgt dafür, dass der Kreis rund dargestellt wird (nicht oval).

# Titel
plt.title("Marktanteile der Produkte")

# Kreis gleichmäßig darstellen
plt.axis('equal')

# Diagramm anzeigen
plt.show()
