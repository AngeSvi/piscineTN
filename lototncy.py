## Le LOTO de TNCY

#Lors de la rentrée, un loto est organisé à TNCY. Pour cela, à chaque tirage, un joueur tire aléatoirement un nombre donnée (mais non borné) de valeurs et l'organisateur, ici l'école, tire également un nombre donné (qui peut être différent du nombre de valeurs tirées par le joueur) de valeurs. 

#Les valeurs des deux entités sont ensuite comparées et les gains sont attribués au joueur comme suit: si le joueur n'a aucune valeur commune avec le tirage de l'école, il gagne 0 Euros, si il a une valeur commune, il gagne 1 Euro, et toute valeur supplémentaire en commun multiplie le gain par 2.

#Par exemple, soit les tirages suivants (gauche) et la main du joueur (partie droite):

"""```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```"""

"""Dans le tirage 1 (card 1) le joueur dispose de 4 cartes gagnantes (48, 83, 17, et 86). 
Cela signifie que ce tirage apporte 8 Euros au joueur. Le tirage 2 (Card 2) apporte 2 Euros 
(cartes 32 et 62); le tirage 3 (cartes 1 et 21): 2 Euros, le tirage 4: 1 Euro, les tirages 5 et 6: 0 Euros 
ce qui fait un total de gains de 13 Euros sur la partie.

Ecrivez une fonction ayant la signature suivante ```lototncy(fileName: str) -> 
int```qui calcule les gains des parties fournies dans le fichier passé en paramètre. 
Deux exemples de fichiers sont fournis pour cela. Votre fonction devra se trouver dans un fichier 
nommé ```lototncy.py```et déposé sur votre proejt gitlab.
"""

def transformer_fichier_d_une_game_en_données_lisibles_python(fichier):

    with open (fichier) as f :
        toutes_les_lignes_en_liste = f.readlines()

    cards = []
    for ligne in toutes_les_lignes_en_liste :
        ligne = ligne.rstrip()
        ligne = ligne.split(":")[1]
        tirage_ecole, tirage_eleve = ligne.split("|")
        tirage_ecole = tirage_ecole.split()
        tirage_eleve = tirage_eleve.split()
        for index in range(len(tirage_ecole)) :
            tirage_ecole[index] = int(tirage_ecole[index])
        for index in range(len(tirage_eleve)) :
            tirage_eleve[index] = int(tirage_eleve[index])
        resultats = {"ecole" : tirage_ecole, "eleve" : tirage_eleve}
        cards.append(resultats)
    return cards 


def calculer_gain_de_partie (cards):
    gain_total = 0
    for tirage in cards : 
        compteur = 0
        for elt in tirage["ecole"] : 
            if elt in tirage["eleve"]:
                compteur += 1
        if compteur >= 1 :
            gain_total += 2**(compteur-1)
    return gain_total
        
print("Vous remportez", calculer_gain_de_partie(transformer_fichier_d_une_game_en_données_lisibles_python("cards.txt")), "€ !")