#!/usr/bin/env python3
"""
manipulations complexes de tableaux : listes d'intervalles.
"""


class Ressources:
    """
    On stocke une liste de ressources, compressee par plages contigues.
    """
    def __init__(self, nombre_ressources, intervalles=None):
        # invariant : les intervalles sont tries par indices croissants
        self.nombre_ressources = nombre_ressources
        if intervalles is not None:
            self.intervalles = intervalles
        else:
            self.intervalles = [[0, nombre_ressources]]

    def disponible(self, indice):
        """
        renvoie si l'indice donne est disponible dans la ressource.
        """
        for intervalle in self.intervalles:
            if intervalle[0] <= indice < intervalle[1]:
                return True
        return False

    def reserve(self, ressources_demandees):
        """
        enleve le nombre de ressources demandees (premieres disponibles).
        renvoie les ressources correspondant aux plages reservees.
        """
        ressources_a_enlever = ressources_demandees
        ressources_enlevees = []
        ressources_gardees = []
        for intervalle in self.intervalles:
            if intervalle[1]-intervalle[0] <= ressources_a_enlever:
                ressources_enlevees.append(intervalle)
                ressources_a_enlever -= intervalle[1]-intervalle[0]

            elif ressources_a_enlever > 0:
                ressources_enlevees.append([intervalle[0],
                    intervalle[0]+ressources_a_enlever])
                ressources_gardees.append([intervalle[0]+ressources_a_enlever,
                    intervalle[1]])
                ressources_a_enlever = 0
            else:
                ressources_gardees.append(intervalle)

        self.intervalles = ressources_gardees
        return Ressources(ressources_demandees, ressources_enlevees)
    

    def simplifier(self):
        """ 
        permet de simplifier [2,7], [7,9] en [2,9]
        """
        print("avant simplification:")
        print(self.intervalles)

        est_simplifie=False
        if len(self.intervalles) >1:
            while not est_simplifie:
                for indice in range(len(self.intervalles)-1):
                    if self.intervalles[indice][1]==self.intervalles[indice+1][0]:
                        #dans ce cas on ajoute les extremités des deux intervalles.
                        self.intervalles[indice]=[self.intervalles[indice][0],self.intervalles[indice+1][1]]
                        del self.intervalles[indice+1]
                        break
                    elif indice == len(self.intervalles)-2:
                        est_simplifie = True

        print("après simplification:")
        print(self.intervalles)

    def retourne(self, ressources_rendues):
        """
        remet les plages de ressources donnees dans le systeme.
        """
        if len(self.intervalles) > 0:
            for intervalle_rendu in ressources_rendues.intervalles:
                for index, intervalle_actuel in enumerate(self.intervalles):
                    if intervalle_rendu[1] <= intervalle_actuel[0]:
                        self.intervalles.insert(index, intervalle_rendu)
                        break
                    elif index == len(self.intervalles)-1:#si on arrive à la fin des intervalles
                        self.intervalles.append(intervalle_rendu)
                        break

        else:
            self.intervalles = ressources_rendues.intervalles
        self.simplifier()


    def __str__(self):
        """
        renvoie une chaine 'visuelle' des ressources contenues dans self.
        par exemple, '|x  xxxxx  |' indique qu'il y a 10 ressources,
        les ressources 0, 3-7 sont disponibles.
        """
        string = ""
        indice_actuel = 0
        for intervalle in self.intervalles:
            while intervalle[0] > indice_actuel:
                string += "."
                indice_actuel += 1
            while intervalle[1] > indice_actuel:
                string += "x"
                indice_actuel += 1

        for _ in range(indice_actuel, self.nombre_ressources):
            string += "."

        return string

def test():
    """
    on teste en gruyerisant une ressource.
    """
    ressource = Ressources(10)
    print(ressource)
    reservees = [ressource.reserve(c) for c in (2, 2, 3, 2, 1)]
    print(ressource)
    ressource.retourne(reservees[1])
    print(ressource)
    ressource.retourne(reservees[3])
    print(ressource)
    ressource.reserve(3)
    print(ressource)
    print(ressource.intervalles)

if __name__ == "__main__":
    test()
