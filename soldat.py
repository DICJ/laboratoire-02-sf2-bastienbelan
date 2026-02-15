from personnage import Personnage

class Soldat(Personnage) :
    
    def __init__(self, nom: str, vie: int, attaque: int, armure: int) :
        super().__init__(nom, vie, attaque, armure)
    
    def __str__(self) :
        return f"Le soldat {self.nom} a {self.vie} de vie, une attaque de {self.attaque} et une armure de {self.armure}"
    
    #Méthodes d'obets
    def subir_degat(self, degat):
        """sert à subir des dégats et diminuer la vie du défenseur

        Args:
            degat (int): dégats subi par le personnage

        Returns:
            int: la nouvelle vie du personnage 
        """
        degat_final = int(((degat - self.armure) * 0.90))

        if degat_final < 0 :
            degat_final = 0

        self.vie -= degat_final
        
        return self.vie