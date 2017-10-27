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

    def retourne(self, ressources_rendues):
        """
        remet les plages de ressources donnees dans le systeme.
        """
        print(ressources_rendues.intervalles)
        intervalles_finaux = []
        #  min = (intervalle for intervalle in self.intervalles if min > min(intervalle))
        if len(self.intervalles) > 0:
            min = self.intervalles[0][0]

            for intervalle in ressources_rendues.intervalles:
                if intervalle[1] < min:
                    intervalles_finaux.append(intervalle)
                elif intervalle[1] == min:
                    intervalles_finaux.append(
                        intervalle.extend(self.intervalles[0])
                    )
                else:
                    self.intervalles.extend(self.intervalles[1:])
        else:
            self.intervalles = ressources_rendues.intervalles



    def __str__(self):
        """
        renvoie une chaine 'visuelle' des ressources contenues dans self.
        par exemple, '|x  xxxxx  |' indique qu'il y a 10 ressources,
        les ressources 0, 3-7 sont disponibles.
        """
        string = ""
        indice_actuel = 0
        if len(self.intervalles) == 0:
            for _ in range(0, self.nombre_ressources):
                string += "."
        for intervalle in self.intervalles:
            while intervalle[0] > indice_actuel:
                string += "."
                indice_actuel += 1
            while intervalle[1] > indice_actuel:
                string += "x"
                indice_actuel += 1

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
