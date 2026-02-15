from guerrier import Guerrier
import random

class Berserker(Guerrier) :
    
    def __init__(self, nom: str, vie: int, attaque: int, force: int, armure: int) :
        super().__init__(nom, vie, attaque, force, armure)

    def attaquer(self) -> int :
        """Permet de calculer le nombre de points de vie que fait notre attaque

        Returns:
            int: retourne les dégats que produit notre attaque
        """
        #Total de vie qu'il a perdu
        vie_perdu = self._vie_max - self.vie
        
        #le nombre de tranches de 10 vie qu'il a perdu
        dizaine_vie_perdu = vie_perdu // 10
        
        #le nombre de dégats supplémentaires
        degats_supplementaire = dizaine_vie_perdu * 5
        
        #calcul total dégats
        self.degats = (self.attaque + (self.force / 2) + random.randint(-2, 2)) + degats_supplementaire
        
        return self.degats
    
    def subir_degat(self, degat: int) -> int :
        """fonction qui enleve des points de vie au berserker

        Args:
            degat (int): Le nombre de points de vie que le berserker va perdre

        Returns:
            int : retourne la vie finale du berserker
        """
        #Calcul de 50% de la vie du berserker
        moitie_vie = self.vie / 2
        
        #Impression du message lorsque le berserker entre en fureur
        if self.vie <= moitie_vie :
            print(f" Le Berserker {self.nom} entre en FUREUR!!!!")
        
        #Calcul des dégats
        degat_final = (degat - self.armure)
        
        #Si les dégats sont plus petit que 0, ils deviennent = à 0
        if degat_final < 0 :
            degat_final = 0
        
        #Calcul de la vie
        self.vie -= degat_final
        
        return self.vie