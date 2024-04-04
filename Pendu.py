from random import *
import time
#Cela va permettre d'utiliser notre variable "choice" et notre module "time".


liste_mots = ["chien", "maison", "voiture", "arbres", "fleur", "soleil", "lune", "etoile", "pluie", "vent", "mer", "montagne", "riviere", "pont", "ordinateur", "telephone", "table", "chaise", "lampe", "livre", "musique", "film", "peinture", "cuisine", "amour", "amitie", "famille", "bonheur", "tristesse", "joie", "colere", "peur", "courage", "espoir", "reve", "voyage",
              "aventure", "exploration", "decouverte", "science", "technologie", "nature", "environnement", "sante", "education", "travail",
              "reussite", "echec", "creativite","melon", "fromage", "truie", "sortie", "pays", "nuire", "dos", "magie", "jeu", "pendu", "marathon", "brocolis", "chocolat", "framboise", "chaise", "table", "fourniture", "assiette", "commode", "virulant", "chat", "python"]
mot = choice(liste_mots)
#Initialisation: on donne une liste de mots puis grâce à la variable "choice" nous allons pouvoir laisser le système choisir au hasard le mot à deviner.
vies = 10
#On détermine le nombre de chances qu'aura le joueur avant d'avoir perdu la partie.


print("Bienvenue dans le jeu du pendu en format Python.")
time.sleep(1)
print("Le but est simple : trouver le mot avant qu'il ne te reste plus de vies.")
time.sleep(1)
print("Tu démarres avec", vies, "vies")
print ("\n")


time.sleep(2)
#Le module "time" va nous servir à faire attendre le système 2 secondes avant de commencer le jeu.


mot_devine = "_"*len(mot)
print("Votre mot à deviner est", mot_devine,)
#Nous allons déterminer la longueur du mot puis le dire à l'utilisateur en lui mettant des tirets du 8 à la place des lettres.



while mot_devine!=mot and vies > 0 :

    lettre = input("Entrez une lettre : ")   
    print("\n")
    for m in range (len(mot)):
        
        if lettre in mot[m] :
            mot_devine = mot_devine[:m] + lettre + mot_devine[m+1:]
            #Si la lettre proposée se trouve dans le mot à deviner, alors on va remplacer un tiret du 8 par la lettre proposée.
            print(mot_devine) 

    if lettre not in mot :
        vies -= 1
        print("Faux! Il te reste", vies, "vies.")
        #Si la lettre n'est pas dans le mot, alors on enlève une vie à l'utilisateur


    
if mot == mot_devine:
    print ("Gagné! Le mot", mot,"a été trouvé avec succès!")
    #Si le mot proposé correspond au mot à deviner, alors c'est gagné.

if vies == 0 :
    print("\n")
    print("Dommage, tu n'as plus de vies. C'est perdu! Le mot était", mot)
    #Si le nombre de vies atteint 0, alors c'est perdu.





