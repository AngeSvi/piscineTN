### Version 0
#Vous disposez d'une liste Python contenant des entiers. Ecrivez une fonction :

#```python
#produitSansSoi(valeurs :list(int)) -> list(int) :
#```

#qui renvoie, pour chaque élément de la liste, le produit de toutes les autres valeurs de la la liste (toutes les valeurs sauf celle se trouvant à l'indice courant).

#Par exemple, le résultat de l'appel de la fonction avec la liste ```(1,2,3,4)```, renverra ```(24,12,8,6)```.

#Simple, non ? 

#Votre fonction devra se trouver seule dans un fichier nommé ```pss1.py'''


def produitSansSoi (liste):
    liste_de_produits = []
    for index in range(len(liste)) :       
        a_ajouter = multiplication_exception(liste, index)
        liste_de_produits.append(a_ajouter)
    return liste_de_produits

def multiplication_exception (liste, index_exclu):
    produit = 1
    for index in range(len(liste)) :
        if index != index_exclu :
            produit *= liste[index]
    return produit 

liste_de_chiffres = [1, 2, 3, 4]

print(produitSansSoi(liste_de_chiffres))