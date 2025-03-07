import window as win  # Supposons que ce module existe et contient les bonnes fonctions

# Création de la fenêtre principale
root = win.createWindow("Percentage Calculator", "500x500")
root.configure(bg="black")

def calculate():
    """Calcule le pourcentage et met à jour le label du résultat avec du style."""
    try:
        num = float(entry1.get())  
        percent = float(entry2.get())  
        result_value = (num * percent) / 100  
        finalResult = result_value + num

        # Animation sur le texte du résultat
        result_label.config(text=f"Result: {finalResult}", fg="cyan", font=("Arial", 20, "bold"))

    except ValueError:
        result_label.config(text="Invalid input", fg="red", font=("Arial", 20, "bold"))

def on_enter(e):
    """Change la couleur du bouton au survol."""
    calc_button.config(bg="darkblue", fg="cyan")

def on_leave(e):
    """Rétablit la couleur du bouton lorsqu'on quitte."""
    calc_button.config(bg="blue", fg="white")

def createComponent():
    """Crée les composants de l'interface graphique avec un meilleur style."""
    
    # Titre stylé
    win.createLabel(root, "💡 Percentage Calculator 💡", ("Arial", 26, "bold"), "black", "cyan")

    # Cadre principal
    frame = win.createFrame(root, bg="gray20", width=450, height=300, bd=2, relief="ridge")
    frame.pack(pady=20, padx=10)

    # Premier champ
    win.createLabel(frame, "Enter the Number:", ("Arial", 14, "bold"), "gray20", "white")
    global entry1
    entry1 = win.createEntry(frame, 15, ("Arial", 14), "black", "white")

    # Deuxième champ
    win.createLabel(frame, "Enter the Percentage:", ("Arial", 14, "bold"), "gray20", "white")
    global entry2
    entry2 = win.createEntry(frame, 15, ("Arial", 14), "black", "white")

    # Ligne de séparation
    win.createFrame(frame, height=2, width=380, bg="white", bd=2, relief="ridge")

    # Bouton stylé avec animations
    global calc_button
    calc_button = win.createButton(frame, "Calculate", ("Arial", 15, "bold"), "blue", "white", calculate, width=12, height=1, border=3)
    calc_button.bind("<Enter>", on_enter)
    calc_button.bind("<Leave>", on_leave)

    # Deuxième ligne de séparation
    win.createFrame(frame, height=2, width=380, bg="white", bd=2, relief="ridge")

    # Label du résultat
    global result_label
    result_label = win.createLabel(frame, "Result: --", ("Arial", 20, "bold"), "gray20", "white")

createComponent()
root.mainloop()
