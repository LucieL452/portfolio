

def salaire_mensuel(salaire_annuel) :   
 return salaire_annuel/12 

def salaire_hebdomadaire(salaire_mensuel):
 return salaire_mensuel/4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
 return salaire_hebdomadaire/heures_travaillees


def main():
 salaire_annuel = float(input("Saisissez votre salaire annuel :"))
 heures_travaillees = float(input("Saisissez le nombre d'heures travaillees par semaine :"))
 mensuel = salaire_mensuel(salaire_annuel)
 hebdomadaire = salaire_hebdomadaire(mensuel)
 horaire = salaire_horaire(hebdomadaire, heures_travaillees)
 salaire_final = print(f"Votre salaire est de {horaire} euros.")
 

main()