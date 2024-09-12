# Définition de la fonction salaire_mensuel
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12


# Définition de la fonction salaire_hebdomadaire
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4


# Définition de la fonction salaire_horaire
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees


def main():
    salaire_annuel = float(input("Entrez votre salaire annuel : "))
    heures_travaillees = float(input("Entrez le nombre d'heures travaillees par semaine : "))

    # Calcul du salaire horaire
    mensuel = salaire_mensuel(salaire_annuel)
    hebdomadaire = salaire_hebdomadaire(mensuel)
    horaire = salaire_horaire(hebdomadaire, heures_travaillees)

    print(f"Votre salaire horaire est de", horaire ,"euros.")

main()
