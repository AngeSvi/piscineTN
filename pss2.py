#Pour corser un peu les choses, il vous est demandé de réécrire l'oalgorithme afin qu'il s'exécute en ```O(n)```, ```n``` étant le nombre d'éléments dans la liste. 

#Cette nouvelle fonction aura la signature suivante:

#```python
#produitSansSoiLineaire(valeurs :list(int)) -> list(int) :
#```
#et sera à définir dans le fichier ```pss2.py```.

def produitSansSoiLineaire (liste):
    liste_de_produits = []
    produit = 1
    for elt in liste :
        produit *= elt
    for elt in liste : 
        produit_divise = produit / elt
        liste_de_produits.append (int(produit_divise))
    return liste_de_produits

liste_de_chiffres = [1, 2, 3, 4]

print(produitSansSoiLineaire(liste_de_chiffres))