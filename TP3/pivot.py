#!/usr/bin/env python

"""
Trie les valeurs en fonction d'un pivot
"""


def pivote_tableau(tableau, indice_pivot):
    """
    sépare le tableau en deux tableaux selon un pivot
    """
    tab_inf = []
    tab_sup = []
    pivot = tableau[indice_pivot]
    tableau.remove(pivot)

    for ele in tableau:
        if ele <= pivot:
            tab_inf.append(ele)
        elif ele > pivot:
            tab_sup.append(ele)
    return tab_inf, tab_sup


def decaler_tableau(tableau, indice_depart, indice_final):
    """
    tableau[indice_depart] correspond à la valeur à déplacer à l'indice_final
    """
    assert 0 <= indice_depart > indice_final < len(tableau)

    indice_actuel = indice_final+1
    val_tmp = tableau[indice_final]

    tableau[indice_final] = tableau[indice_depart]
    tableau[indice_depart] = val_tmp

    while indice_actuel <= indice_depart:
        tableau[indice_actuel], val_tmp = val_tmp, tableau[indice_actuel]
        indice_actuel += 1


def pivote_tableau_en_place(tableau, indice_pivot):
    """
    trie le tableau selon un pivot
    """
    pivot = tableau[indice_pivot]

    for i in range(len(tableau)):
        if i > indice_pivot:
            if tableau[i] <= pivot:
                decaler_tableau(tableau, i, indice_pivot)
                indice_pivot += 1
            elif i < indice_pivot:
                if tableau[i] >= pivot:
                    tableau[indice_pivot], tableau[i], indice_pivot \
                        = tableau[i], pivot, i


def main():
    """
    main
    """
    tab = [6, 2, 5, 3, 4, 2]
    #indice = 1
    #tab_inf, tab_sup = pivote_tableau(tab, indice)

    #print(tab_inf)
    #print(tab_sup)

    #print(tab)
    for i in range(5):
        tab = [1, 2, 5, 3, 4]
        pivote_tableau_en_place(tab, i)
        print(tab)

main()
