class Armure :
    """Permet d'ajouter une armure à un personnage
    """
    
    def __init__(self, nom : str, points_armure : int) :
        self.nom = nom
        self._points_armure = 0

        #Validation
        self.points_armure = points_armure
    
    #Property et setter
    @property
    def points_armure(self) -> int :
        return self._points_armure
    
    @points_armure.setter
    def points_armure(self, nouveau_points: int) -> None :
        
        if 0 < nouveau_points < 15 :
            self._points_armure = nouveau_points
        
        elif nouveau_points < 0 :
            self._points_armure = 0
        
        elif nouveau_points > 15 :
            self._points_armure = 15