import dico
import random

# Définition d'une fonction pour générer un numéro aléatoire entre 0 et 36
def generer_numero_aleatoire():
    return random.randint(0, 36)

# Demande la somme de départ
somme_depart = int(input("Entrez la somme de départ : "))
somme = somme_depart
mod=1
victoire=0
defaite=0
suite=0
last=0
maxi=somme_depart

while somme != 0 and somme < 10000:
    if mod==1 :
        numero_aleatoire = generer_numero_aleatoire()
        temp = None

        if temp is None:
            nombre_choisi = input("Choisissez un nombre entre 0 et 36 : ")

            # Vérifie si la saisie contient un "-" et si c'est un nombre négatif
            if '-' in nombre_choisi:
                nombre_choisi = nombre_choisi.replace('-', '')
                mod=2
            try:
                temp = int(nombre_choisi)
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        if temp == numero_aleatoire:
            gain = 5 * 32
            somme += gain
            print(f"Bravo ! Vous avez gagné {gain} €. Votre nouvelle somme est de {somme} €.")
            if somme>maxi :
                maxi=somme
            victoire+=1
            if last==1:
                suite+=1
            last=1
        else:
            somme -= 5
            print(f"Dommage ! Le nombre était {numero_aleatoire}, vous perdez 5 €. Votre nouvelle somme est de {somme} €.")
            print(temp)
            defaite+=1
            last=0
    else :
        numero_aleatoire = generer_numero_aleatoire()
        if temp == numero_aleatoire:
            gain = 5 * 32
            somme += gain
            print(f"Bravo ! Vous avez gagné {gain} €. Votre nouvelle somme est de {somme} €.")
            victoire+=1
            if somme>maxi :
                maxi=somme
            if last==1:
                suite+=1
            last=1

        else:
            somme -= 5
            print(f"Dommage ! Le nombre était {numero_aleatoire}, vous perdez 5 €. Votre nouvelle somme est de {somme} €.")
            print(temp)
            defaite+=1
            last=0


print("Fin de procedure")
print("nombre de Victoire  :", victoire)
print("nombre de Defaite   :", defaite)
print("Victoire à la suite :", suite)
print("")
print("Somme depart        :", somme_depart)
print("Somme max           :", maxi)
print("Somme final : " , somme,"€")
