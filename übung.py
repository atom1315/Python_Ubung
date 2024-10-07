from tabulate import tabulate

# Erstellen der Daten für eine bessere Kontrolle über die Formatierung
data_land_numeric = [
    ["Bulgarien", 28.7, 32.4, 24.8, 23, 48.5, 10],
    ["Türkei", 27.3, 31.4, 22.1, 25, 35.1, 12],
    ["Griechenland", 27.2, 38.6, 16.9, 19.5, 32.0, 10],
    ["Ungarn", 25.8, 30.7, 21.5, 33, 56.7, 13],
    ["Lettland", 24.9, 26.5, 23.0, 21, 40.8, 11],
    ["Österreich", 22.0, 26.0, 18.0, 20, 29.5, 10],
    ["Deutschland", 18.0, 22.0, 14.0, 21, 27.4, 10],
    ["Schweiz", 27.0, 28.3, 25.6, 19, 25.0, 10],
    ["Schweden", 9.3, 11.0, 7.6, 13, 13.1, 7],
    ["Island", 11.2, 13.5, 9.0, 14, 10.4, 8],
    ["Finnland", 12.5, 14.3, 10.7, 17, 18.2, 9],
    ["Norwegen", 12.9, 15.2, 10.4, 16, 15.5, 9],
    ["Luxemburg", 13.5, 15.0, 11.8, 15, 22.0, 9]
]

# Der Überschriften für die Tabelle
title = [
    "Land", 
    "Raucher (%)",  
    "Männer (%)",   
    "Frauen (%)",   
    "Krebsfälle (%)", 
    "Lungenkrebs",  
    "Verlorene Jahre" 
]

# Verwenden von "tabulate" zum Drucken der Daten in einem übersichtlichen Tabellenformat
print(tabulate(data_land_numeric, title, tablefmt="grid", numalign="center", stralign="center"))


import matplotlib.pyplot as plt

# 1 Daten
länder = ["Bulgarien", "Türkei", "Griechenland", "Ungarn", "Lettland", "Österreich", "Deutschland", "Schweiz", "Schweden", "Island", "Finnland", "Norwegen", "Luxemburg"]
raucher_gesamt = [28.7, 27.3, 27.2, 25.8, 24.9, 22.0, 18.0, 27.0, 9.3, 11.2, 12.5, 12.9, 13.5]  # Spalte mit Daten Raucher
raucher_männer = [32.4, 31.4, 38.6, 30.7, 26.5, 26.0, 22.0, 28.3, 11.0, 13.5, 14.3, 15.2, 15.0] # Spalte mit Daten Männer
raucher_frauen = [24.8, 22.1, 16.9, 21.5, 23.0, 18.0, 14.0, 25.6, 7.6, 9.0, 10.7, 10.4, 11.8]   # Spalte mit Daten Frauen
lungenkrebs = [48.5, 35.1, 32.0, 56.7, 40.8, 29.5, 27.4, 25.0, 13.1, 10.4, 18.2, 15.5, 22.0]    # Spalte mit Daten Lungenkrebs
verlorene_jahre = [10, 12, 10, 13, 11, 10, 10, 10, 7, 8, 9, 9, 9]                               # Spalte mit Daten Verlorene Jahre

# 2 Erste Balkendiagramm der Raucheranteile nach Ländern
plt.figure(figsize=(12, 6))                                                             # Erstellt ein neues Fenster für den erste Diagramm mit den Abmessungen 12 x 6 Zoll

# 3 Streifen rechte seite oben
plt.bar(länder, raucher_gesamt, color='blue', alpha=0.7, label='Gesamtanteil Raucher')  # Blaue Strich rechts oben und Funktion plt.bar zeigt länder auf der Achse X 
plt.bar(länder, raucher_männer, color='red', alpha=0.7, label='Raucher Männer')         # Rote Strich rechts oben
plt.bar(länder, raucher_frauen, color='green', alpha=0.7, label='Raucher Frauen')       # Grüne Strich rechts oben
       

# 4 Diagrammeinstellungen für erste Balkendiagramm
plt.title('Raucheranteile nach Ländern', fontsize=16)                              # Fügt dem Diagramm einen Titel hinzu.
plt.xlabel('Länder', fontsize=12)                                                  # Fügt der X-Achse 'Länder' eine Beschriftung hinzu und Schriftgröße
plt.ylabel('Anteil (%)', fontsize=12)                                              # Fügt der Y-Achse 'Anteil (%)' eine Beschriftung hinzu und Schriftgröße
plt.xticks(rotation=45)                                                            # Dreht Länder um 45 Grad auf der X-Achse
plt.legend()                                                                       # Fügt dem Diagramm eine Legende hinzu, die erklärt, was die Balkenfarben bedeuten

# 5 Anzeige des ersten Diagramm
plt.tight_layout()                                                                 # Passt grafische Elemente für eine bessere Lesbarkeit an
plt.show()                                                                         # Zeigt die Grafik auf dem Console an

# 6 Zweiter Diagramm - Lungenkrebs und verlorene Lebensjahre nach ländern 
plt.figure(figsize=(12, 6))                                                        # Erstellt ein neues Fenster für den zweite Diagramm mit den Abmessungen 12 x 6 Zoll

# 7 Streifen rechte seite oben 
plt.plot(länder, lungenkrebs, color='orange', marker='o', linestyle='-', label='Lungenkrebsfälle')            # Orange Strich rechte seite oben und Fuktion plt.plot zeigt länder auf der Achse X
plt.plot(länder, verlorene_jahre, color='purple', marker='o', linestyle='-', label='Verlorene Lebensjahre')   # Purple Strich rechte seite oben

# 8 Diagrammeinstellungen für zweiter Diagramm
plt.title('Lungenkrebsfälle und verlorene Lebensjahre nach Ländern', fontsize=16)  # Fügt dem Diagramm einen Titel hinzu
plt.xlabel('Länder', fontsize=12)                                                  # Fügt der X-Achse 'Länder' eine Beschriftung hinzu und Schriftgröße
plt.ylabel('Anzahl (pro 100.000 Menschen)', fontsize=12)                           # Fügt der Y-Achse 'Anzahl pro 100.000 Menschen' eine Beschriftung hinzu und Schriftgröße
plt.xticks(rotation=45)                                                            # Dreht Länder um 45 Grad auf der X-Achse
plt.legend()                                                                       # Fügt dem Diagramm eine Legende hinzu

# 9 Anzeige des zweiten Diagramms in Console
plt.tight_layout()                                                                 # Passt grafische Elemente für eine bessere Lesbarkeit an
plt.show()                           


# Bibliotek Pandas 27.09.24 Tabelle

import pandas as pd

# Daten Ländern und Zigarettenpreisen für Tabelle
data = {
    "Land": [
        "Albanien", "Ägypten", "Algerien", "Argentinien", "Armenien", "Australien", "Azerbaidschan", "Bangladesch", 
        "Belarus", "Belgien", "Bolivien", "Bosnien-Herzegowina", "Brasilien", "Bulgarien", "Chile", "China", 
        "Costa Rica", "Dänemark", "Deutschland", "Dubai", "Ecuador", "Estland", "Finnland", "Frankreich", "Georgien", 
        "Griechenland", "Großbritannien", "Hong Kong", "Indien", "Indonesien", "Irak", "Iran", "Irland", 
        "Israel", "Italien", "Japan", "Jordanien", "Kanada", "Kasachstan", "Katar", "Kenia", "Kolumbien", "Kroatien", 
        "Kuba", "Kuwait", "Lettland", "Libyen", "Litauen", "Luxemburg", "Malaysia", "Malta", "Marokko", "Mauritius", 
        "Mexiko", "Moldau", "Montenegro", "Nepal", "Neuseeland", "Niederlande", "Nordmazedonien", "Norwegen", "Oman", 
        "Österreich", "Palästina", "Panama", "Pakistan", "Peru", "Philippinen", "Polen", "Portugal", "Rumänien", 
        "Russland", "Saudi-Arabien", "Schweiz", "Schweden", "Serbien", "Singapur", "Slowakei", "Slowenien", 
        "Sri Lanka", "Südafrika", "Südkorea", "Spanien", "Taiwan", "Thailand", "Tschechien", "Tunesien", "Türkei", 
        "Ukraine", "Ungarn", "Uruguay", "USA", "Usbekistan", "Venezuela", "Vereinigte Arabische Emirate", "Vietnam", "Zypern"
    ],
    "Preis für Packung (EUR)": [
        3.50, 1.10, 2.40, 1.80, 2.35, 27.50, 3.20, 2.45, 1.40, 8.40, 2.62, 3.10, 2.00, 3.10, 4.90, 3.20, 4.40, 8.10, 
        8.10, 0.90, 5.45, 5.50, 10.00, 11.20, 2.68, 4.60, 15.98, 11.90, 3.80, 2.20, 1.82, 1.82, 16.04, 8.80, 6.00, 
        3.70, 3.20, 12.60, 1.60, 5.97, 2.50, 2.25, 4.80, 3.20, 2.95, 4.80, 2.00, 5.00, 5.60, 3.75, 5.70, 3.65, 5.30, 
        3.65, 2.59, 3.70, 2.70, 22.00, 9.00, 2.60, 12.90, 6.20, 6.00, 6.60, 5.00, 1.80, 4.90, 2.50, 4.50, 5.50, 5.05, 
        2.10, 6.80, 9.50, 6.15, 3.60, 11.60, 5.00, 5.00, 8.20, 2.65, 3.10, 5.35, 3.40, 3.82, 5.70, 2.95, 1.80, 2.00, 
        5.60, 4.70, 9.00, 1.84, 3.65, 5.65, 1.20, 5.00
    ]
}

# Bildung DataFrame
df = pd.DataFrame(data)

# Print Tabelle
print(df.to_string(index=False))




# Sortierte die Daten in aufsteigender Reihenfolge nach Zigarettenpreisen
df_sorted = df.sort_values(by="Preis für Packung (EUR)")

# Print Tabelle 
print(df_sorted.to_string(index=False))



# Sortirung daten von teuere bis billigste Preis Diagramm 
df_sorted = df.sort_values(by="Preis für Packung (EUR)")

# Diogramm schrift Achse X, Y beschreibung, farbe
plt.figure(figsize=(10, 16))  
plt.barh(df_sorted["Land"], df_sorted["Preis für Packung (EUR)"], color='skyblue')

# Titel hinzufügen für Achse X, Y
plt.title("Preis Zigaretten (für 20 St., in EUR)", fontsize=16)
plt.xlabel("Preis (EUR)", fontsize=12)
plt.ylabel("Land", fontsize=12)

# Schrift grosse fur Lände
plt.yticks(fontsize=10) 

# Print Diagramm 
plt.tight_layout()
plt.show()




