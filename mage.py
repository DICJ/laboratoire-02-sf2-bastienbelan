from personnage import Personnage
import random

class Mage(Personnage) :
    """sert à gérer les mages

    Args:
        Personnage (): Classe personnages
    """
    def __init__(self, nom: str, vie: int, attaque: int, mana: int, armure: int) :
        super().__init__(nom, vie, attaque, armure)

        #Initialisation
        self._mana = 0 
        
        #Vérification 
        self.mana = mana
        self._mana_max = self.mana

    def __str__(self) -> str :
        return f"Le mage {self.nom} a {self.vie} de vie, une attaque de {self.attaque}, une armure de {self.armure} et une mana de {self.mana}"
    
    #Property et setter
    @property
    def mana(self) -> int :
        return self._mana
    
    @mana.setter
    def mana(self, nouvelle_mana: int) -> None :
        if 0 <= nouvelle_mana <= 100 :
            self._mana = nouvelle_mana
        
        elif nouvelle_mana < 0 :
            self._mana = 0

        elif nouvelle_mana > 100 :
            self._mana = 100

    #Méthodes d'objets
    def diminuer_mana(self) -> None :
        """Diminue la mana d'un chiffre aléatoire entre 15 et 25
        """
        self.mana -= random.randint(15, 25)

    def attaquer(self) -> int :
        """Sert à déterminer les dégâts infligés lors d'une attaque

        Returns:
            int: les dégats infligés à l'adversaire
        """
        #Si il a encore de la mana, l'attaque est boosté de 60
        if self.mana > 0 :
            self.degats = self.attaque + 60
            self.diminuer_mana()
        
        #s'il n'a plus de mana, l'attaque reste celle de base
        else :
            self.degats = self.attaque

        return self.degats
    
    def ajouter_mana_max(self) -> None :
        """Permet de réinitialiser la mana maximale du mage
        """
        self.mana = self._mana_max

    def reset(self) -> None :
        """permet de reset le mage à son point de départ
        """
        self.ajouter_vie_max()
        self.ajouter_mana_max()
