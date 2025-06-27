from Fahrzeug import Fahrzeug
from PKW import PKW
import tkinter as tk
from tkinter import messagebox
import json

fahrzeug_liste = [] # Speichern wir die Objekte

def liste_to_dict():
    fahrzeuge_dict= {}
    for index, objekt in enumerate(fahrzeug_liste):
        fahrzeuge_dict[index] = objekt.__dict__
    return fahrzeuge_dict

def write_json_file(filename = "Fahrzeuge.json"):
    data = liste_to_dict()
    with open(filename,"w") as file:
        json.dump(data, file, indent = 4,ensure_ascii=False)

def _get_entry_value_und_leeren(entry_widget):
    value = entry_widget.get()
    entry_widget.delete(0, tk.END)
    return value

def erzeuge_fahrzeug():
    marke = _get_entry_value_und_leeren(marke_entry)
    modell = _get_entry_value_und_leeren(modell_entry)
    baujahr_str = _get_entry_value_und_leeren(baujahr_entry)

    if not all([marke, modell, baujahr_str]):
        messagebox.showerror("Eingaberfehler","Marke, Modell und Baujahr sind erforderlich.")
        return
    
    try:
        baujahr = int(baujahr_str)
        fahrzeug = Fahrzeug(marke, modell, baujahr)
        fahrzeug_liste.append(fahrzeug)
        aktualisiere_fahrzeug_anzeig()
    except ValueError:
        messagebox.showerror("Eingaberfehler","Bitte geben Sie gültige Zahlen für Baujahr ein.")


def erzeuge_pkw():
    marke = _get_entry_value_und_leeren(marke_entry)
    modell = _get_entry_value_und_leeren(modell_entry)
    baujahr_str = _get_entry_value_und_leeren(baujahr_entry)
    tueren_str =  _get_entry_value_und_leeren(tueren_entry)

    if not all([marke, modell, baujahr_str, tueren_str]):
        messagebox.showerror("Eingaberfehler","Marke, Modell und Baujahr sind erforderlich.")
        return
    
    try:
        baujahr = int(baujahr_str)
        tueren = int(tueren_str)
        pkw = PKW(marke, modell, baujahr, tueren)
        fahrzeug_liste.append(pkw)
        aktualisiere_fahrzeug_anzeig()
    except ValueError:
        messagebox.showerror("Eingaberfehler","Bitte geben Sie gültige Zahlen für Baujahr und Türen ein.")

def erzeuge_fahrzeug_aus_string():
    fahrzeug_string = _get_entry_value_und_leeren(fahrzeug_string_entry)
    if not fahrzeug_string:
        messagebox.showerror("Eingaberfehler","Bitte geben Sie einen String für das Fahrzeug ein.")
        return
    fahrzeug = Fahrzeug.fahrzeug_aus_string(fahrzeug_string)
    if fahrzeug:
        fahrzeug_liste.append(fahrzeug)
        aktualisiere_fahrzeug_anzeig()

def aktualisiere_fahrzeug_anzeig():
    fahrzeu_listbox.delete(0, tk.END)
    for i, fahrzeug in enumerate(fahrzeug_liste):
        fahrzeu_listbox.insert(tk.END, f"[{i}] {fahrzeug.marke} {fahrzeug.modell} ({(type(fahrzeug).__name__)})")
    gesamt_fahrzeuge_label.config(text=Fahrzeug.get_anzahl_fahrzeuge())

root = tk.Tk() #Hauptfenster
root.title("Fahrzeugverwaltung")
root.geometry("800x500")

tk.Label(root, text="Marke:").grid(row=0, column=0, sticky="w", pady=2, padx=5)
marke_entry = tk.Entry(root, width=30)
marke_entry.grid(row=0, column=1,pady=2, padx=5)

tk.Label(root, text="Modell:").grid(row=1, column=0, sticky="w", pady=2, padx=5)
modell_entry = tk.Entry(root, width=30)
modell_entry.grid(row=1, column=1,pady=2, padx=5)

tk.Label(root, text="Baujahr:").grid(row=2, column=0, sticky="w", pady=2, padx=5)
baujahr_entry = tk.Entry(root, width=30)
baujahr_entry.grid(row=2, column=1,pady=2, padx=5)

tk.Label(root, text="Anzahl Türen (PKW):").grid(row=3, column=0, sticky="w", pady=2, padx=5)
tueren_entry = tk.Entry(root, width=30)
tueren_entry.grid(row=3, column=1,pady=2, padx=5)

tk.Button(root, text="Fahrzeug Erstellen", command=erzeuge_fahrzeug ).grid(row=0, column=2, columnspan= 2,sticky="w", padx=5, pady=5)
tk.Button(root, text="PKW Erstellen", command=erzeuge_pkw ).grid(row=1, column=2, columnspan= 2,sticky="w", padx=5, pady=5)

tk.Label(root, text="Fahrzeug aus String (Marke-Modell-Baujahr):").grid(row=4, column=0,sticky="w", pady=2, padx=5)
fahrzeug_string_entry = tk.Entry(root, width=30)
fahrzeug_string_entry.grid(row=4, column=1,padx=5,pady=2)
tk.Button(root, text="Aus String Erstellen", command=erzeuge_fahrzeug_aus_string).grid(row=4, column=2, columnspan= 2,sticky="w", padx=5, pady=5)

tk.Button(root, text="Save all as JSON", command=write_json_file).grid(row=5, column=2, columnspan= 2,sticky="w", padx=5, pady=5)
# Fahrzeug liste
fahrzeu_listbox = tk.Listbox(root, height=10, selectmode=tk.SINGLE)
fahrzeu_listbox.grid(row=6, column=0, columnspan=5, pady=6, padx=20,sticky="we")

# Gesamtzahl Fahrzeuge 
gesamt_fahrzeuge_label = tk.Label(root, text=Fahrzeug.get_anzahl_fahrzeuge(), font=("Arial", 10, "bold"))
gesamt_fahrzeuge_label.grid(row=7, column=0, columnspan=2, sticky="e", pady=5)



root.mainloop()