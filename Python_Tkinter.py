import random
from tkinter import *

def display_label():
 # Ici il faut créer l'objet Label avec texte au choix puis l'afficher
 label = Label(fenetre, text="La jolie fenetre")
 label.pack() 

fenetre = Tk()

# Quand je clique sur le bouton, je dois afficher le texte du label
bouton=Button(fenetre, text="Afficher texte", command=display_label)
bouton.pack()

fenetre.mainloop()




