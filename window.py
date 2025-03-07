#window.py file
import tkinter as tk

# Fonctions pour créer des composants graphiques
# Chaque fonction crée un composant et le retourne
def createWindow(title, size):  
    window = tk.Tk()
    window.title(title)
    window.geometry(size)
    window.max_height = 500
    window.max_width = 500
    window.resizable(False, False)
    return window
#Fonction pour créer un label
def createLabel(window, text, font, bg, textColor):
    label = tk.Label(window, text=text, font=font, bg=bg, fg=textColor)  # Correction ici
    label.pack()
    return label
#Fonction pour créer un champ de saisie
def createEntry(window, width, font, bg, textColor):
    entry = tk.Entry(window, width=width, font=font, bg=bg, fg=textColor)  # Correction ici
    entry.pack()
    return entry 
#Fonction pour créer un bouton
def createButton(window, text, font, bg, textColor, command, width, height, border):
    button = tk.Button(window, text=text, font=font, bg=bg, fg=textColor, command=command, width=width, height=height, border=border)  # Correction ici
    button.pack()
    return button
#Fonction pour créer un cadre
def createFrame(window, height, width, bg, bd, relief):
    frame = tk.Frame(window, height=height, width=width, bg=bg, bd=bd, relief=relief)  # Correction ici
    frame.pack(pady=10, fill="x")
    return frame
