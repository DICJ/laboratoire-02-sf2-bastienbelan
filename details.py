class Details() :
    """sert à gérer les combats dans l'arène
    """
    #Attributs d'objets
    def __init__(self, nom_1: str, nom_2 : str) :
        
        #Initialisation des variables
        self.nom_1 = nom_1
        self.nom_2 = nom_2
        self.vainqueur = ""
        self.nombre_tours = 0
    
    #Méthodes d'objets
    def incrementer_tour(self) -> None :
        """sert à incrémenter le nombre de tours de 1 à chacun des tours du combat
        """
        self.nombre_tours += 1

    def definir_vainqueur(self, nom_vainqueur : str) -> str :
        """sert à définir le nom du vainqueur

        Args:
            nom_vainqueur (str): Le nom du vainqueur

        Returns:
            str: le nom du vainqueur
        """
        self.vainqueur = nom_vainqueur
        
        return self.vainqueur