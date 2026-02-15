class Personnage :
    """Personnages de jeux vidéos
    """

    def __init__(self, nom: str, vie: int, attaque: int, armure: int) :
        #Initialisation
        self.nom = nom
        self._attaque = 0
        self._armure = 0
        self._vie = 0

        #Validation
        self.vie = vie
        self.attaque = attaque
        self.armure = armure
        self._vie_max = self.vie

    def __str__(self) -> str :
        return f"Le personnage {self.nom} a {self.vie} de vie, une armure de {self.armure} et une attaque de {self.attaque}"
    
    def __eq__(self, autre_perso: "Personnage") -> bool :

        if self.nom == autre_perso.nom and self.vie == autre_perso.vie :
            return True
        
        else : 
            return False

    #property et setter
    @property
    def vie(self) -> int :
        return self._vie
    
    @vie.setter
    def vie(self, nouvelle_vie: int) -> None :
        if 0 <= nouvelle_vie <= 500 :
            self._vie = nouvelle_vie

        elif nouvelle_vie < 0 :
            self._vie = 0

        elif nouvelle_vie > 500 :
            self._vie = 500

    @property
    def attaque(self) -> int :
        return self._attaque
    
    @attaque.setter
    def attaque(self, nouvelle_attaque) -> None :

        if 0 <= nouvelle_attaque <= 50 :
            self._attaque = nouvelle_attaque

        elif nouvelle_attaque < 0 :
            self._attaque = 0

        elif nouvelle_attaque > 50 :
            self._attaque = 50
    
    @property
    def armure(self) -> int :
        return self._armure
    
    @armure.setter
    def armure(self, nouvelle_armure: int) -> None :

        if 0 <= nouvelle_armure <= 15 :
            self._armure = nouvelle_armure

        elif nouvelle_armure < 0 :
            self._armure = 0
        
        elif nouvelle_armure > 15 :
            self._armure = 15

    #Méthodes d'objets
    def subir_degat(self, degat: int) -> int :
        """sert à subir des dégats et diminuer la vie du défenseur

        Args:
            degat (int): dégats subi par le personnage

        Returns:
            int: la nouvelle vie du personnage 
        """
        degat_final = (degat - self.armure)

        if degat_final < 0 :
            degat_final = 0

        self.vie -= degat_final
        
        return self.vie
    
    def attaquer(self) -> int :
        """Sert à attaquer un personnage

        Returns:
            int: retourne le nombre de points de vie que génère notre attaque
        """
        return self.attaque
    
    def ajouter_vie_max(self) -> None :
        """Permet de réinitialiser la vie maximale du personnage
        """
        self.vie = self._vie_max

    def reset(self) -> None :
        """Permet de réinitialiser le personnage au complet (le faire revenir à son point de départ)
        """
        self.ajouter_vie_max()

        