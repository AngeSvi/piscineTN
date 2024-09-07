### La totale

#il vous est demandé de réécrire l'algorithme afin qu'il s'exécute tourjours  en ```O(n)```, 
# ```n``` étant le nombre d'éléments dans la liste mais 
# vous n'avez pas le droit d'utiliser l'opération de division :-)

#Cette nouvelle fonction aura la signature suivante:

#```python
#produitSansSoiLineaireTotale(valeurs :list(int)) -> list(int) :
#```
#et sera à définir dans le fichier ```pss3.py```.

def produitSansSoiLineaire (liste):
    liste_de_produits = []
    produit = 1
    for elt in liste :
        produit *= elt #24

    for elt in liste : 
        produit_divise = produit / elt
        liste_de_produits.append (int(produit_divise))
    return liste_de_produits

liste_de_chiffres = [1, 2, 3, 4]

print(produitSansSoiLineaire(liste_de_chiffres))