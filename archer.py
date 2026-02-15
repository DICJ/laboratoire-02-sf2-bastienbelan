from personnage import Personnage
import random 

class Archer(Personnage) :
    """Sert à gérer les archers

    Args:
        Personnage (class): classe personnage
    """
    def __init__(self, nom: str, vie: int, attaque: int, dexterite: int, armure: int) :
        super().__init__(nom, vie, attaque, armure)

        #Initialisation
        self._dexterite = 0

        #verification
        self.dexterite = dexterite
    
    def __str__(self) :
        return f"L'archer {self.nom} a {self.vie} de vie, une attaque de {self.attaque}, une armure de {self.armure} et une dextérité de {self.dexterite}"
    
    #Property et setter
    @property
    def dexterite(self) -> int :
        return self._dexterite
    
    @dexterite.setter
    def dexterite(self, nouvelle_dexterite: int) -> None :
        if 40 <= nouvelle_dexterite <= 70 :
            self._dexterite = nouvelle_dexterite
        
        elif nouvelle_dexterite < 40 :
            self._dexterite = 40

        elif nouvelle_dexterite > 70 :
            self._dexterite = 70
    
    #Méthodes d'objets
    def attaquer(self) -> int :
        """sert à déterminer les dégats de l'attaque

        Returns:
            int: retourne les dégats que fait l'attaque
        """
        nombre = random.randint(1,100)

        self.degats = self.attaque + 15

        if nombre < self.dexterite :
            self.degats = self.degats * 2
        
        return self.degats