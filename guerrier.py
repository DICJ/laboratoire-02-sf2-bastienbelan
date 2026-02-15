from personnage import Personnage
import random

class Guerrier(Personnage) :
    """Sert à gérer les guerriers
    """
    
    def __init__(self, nom: str, vie: int, attaque: int, force: int, armure: int) :
        super().__init__(nom, vie, attaque, armure)
        
        #Initialisation
        self._force = 0

        #vérification
        self.force = force
    
    def __str__(self) -> str :
        return f"Le guerrier {self.nom} a {self.vie} de vie, une attaque de {self.attaque}, une armure de {self.armure} et une force de {self.force}"
    
    #property et setter
    @property
    def force(self) -> int :
        return self._force
    
    @force.setter
    def force(self, nouvelle_force: int) -> None :
        if 1 <= nouvelle_force <= 50 :
            self._force = nouvelle_force
        
        elif nouvelle_force > 50 :
            self._force = 50

        elif nouvelle_force < 1 :
            self._force = 1

    #Méthodes d'objets
    def attaquer(self) -> int :
        """Sert à déterminer les dégats effectués lors de l'attaque

        Returns:
            int: retorune les dégats effectués lors de l'attaque
        """
        self.degats = self.attaque + (self.force / 2) + random.randint(-2, 2)
        
        return self.degats