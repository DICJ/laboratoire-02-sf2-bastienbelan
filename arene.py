from personnage import Personnage
from details import Details

class Arene :
    """sert à gérer les personnages
    """
    def __init__(self, liste_personnages: list) :
        
        #initialisation
        self._liste_personnages = []
        self._liste_combats = []

        #vérification
        self.liste_personnages = liste_personnages
    
    def __len__(self) -> int :
        nb_perso = 0

        for x in self.liste_personnages :
            if x.vie > 0 :
                nb_perso += 1
        
        return nb_perso
    
    #property et setter
    @property
    def liste_personnages(self) -> list :
        return self._liste_personnages
    
    @liste_personnages.setter
    def liste_personnages(self, nouvelle_liste: list) -> None :
        self._liste_personnages = nouvelle_liste

    #Méthodes d'objets
    def ajouter_personnage(self, personnage: Personnage ) -> None :
        """Sert à ajouter un personnage à la liste des personnages

        Args:
            personnage (Personnage): Classe personnage (peut être n'importe quel personnage)
        """
        #Ajout du personnage à la liste
        self.liste_personnages.append(personnage)

    def afficher_details_personnages(self) -> None :
        """sert à afficher les détails de chacun des personnages
        """
        print("----------------------------------")
        for x in self.liste_personnages :
            print(f"-{x}")
    
    def afficher_personnages(self) -> None :
        """Sert à afficher le nom de chacun des personnages
        """
        nb = 0
        for x in self.liste_personnages :
            nb += 1 
            print(f"{nb}. {x.nom}")

    def combattre(self, index_1: int, index_2: int) -> None :
        """Sert à faire combattre deux personnages ensemble

        Args:
            index_1 (int): l'index du premier personnage dans la liste
            index_2 (int): l'index du deuxième personnage dans la liste
        """
        infos_combat = Details(self.liste_personnages[index_1].nom, self.liste_personnages[index_2].nom)

        #Tant que l'un ou l'autre personnage a de la vie, le combat continue
        while self.liste_personnages[index_1].vie > 0 and self.liste_personnages[index_2].vie > 0 :
            
            #L'attaquant attaque
            self.degats = self.liste_personnages[index_1].attaquer()
            
            #le défenseur recoit les dégats
            self.liste_personnages[index_2].subir_degat(self.degats)

            #Phrase descriptive
            print(f"-{self.liste_personnages[index_1].nom} inflige {self.degats} dégats à {self.liste_personnages[index_2].nom}, sa vie est maintenant de {self.liste_personnages[index_2].vie}")
            
            #Vérification de mort subite
            if self.liste_personnages[index_2].vie <= 0 :
                break

            #Contre-attaque
            attaquant = self.liste_personnages[index_1]
            defenseur = self.liste_personnages[index_2]
            
            self.liste_personnages[index_1] = defenseur
            self.liste_personnages[index_2] = attaquant

            #Incrémenter le nombre de tours du combat
            infos_combat.incrementer_tour()
        
        #si le premier personnage n'a plus de vie, le deuxième gagne
        if self.liste_personnages[index_1].vie <= 0 :
            print(f"*Le vainqueur est {self.liste_personnages[index_2].nom} !")

            #Définition du nom du vainqueur
            infos_combat.definir_vainqueur(self.liste_personnages[index_2].nom)
        
        #si le deuxieme personnage n'a plus de vie, le premier gagne
        elif self.liste_personnages[index_2].vie <= 0 :
            print(f"*Le vainqueur est {self.liste_personnages[index_1].nom} !")

            #Définition du nom du vainqueur
            infos_combat.definir_vainqueur(self.liste_personnages[index_1].nom)
        
        #Ajout du combat à la liste des combats
        self._liste_combats.append(infos_combat)
    
    def afficher_historique(self) -> None :
        """Sert à afficher la liste des combats
        """
        nb_combats = 0

        for x in self._liste_combats :
            nb_combats += 1

            print(f"{nb_combats}. Le combat entre {x.nom_1} et {x.nom_2} s'est terminé en {x.nombre_tours} rondes et le vainqueur est {x.vainqueur}!")
    
    def soigner_personnage(self, index: int) -> None :
        """sert à soigner un personnage (revenir au point de départ)

        Args:
            index (int): index du personnage à soigner
        """
        #reset du personnage
        self.liste_personnages[index].reset()
        
        print("Le personnage a été soigné!")

    def nettoyer_arene(self) -> None :
        """Permet d'enlever de l'arène les personnages qui sont morts
        """
        for x in self.liste_personnages :

            if x.vie <= 0 :
                self.liste_personnages.remove(x)
    
    def battle_royal(self) -> None :
        """Permet de faire un battle royal entre tout les personnages de l'arène
        """
        #Le nombre de rondes que le battle royale dure
        ronde = 0 
        
        #Boucle pour s'assurer de toujours continuer tant qu'il reste un seul personnage
        while len(self.liste_personnages) > 1 :
            ronde += 1

            #réinitialisation de la vie de chaque personnage
            for x in self.liste_personnages :
                x.reset()
        
            #si le nombre de personnages est pair
            if len(self.liste_personnages) % 2 == 0 :

                #Trouver le nombre de combats
                nb_combats = len(self.liste_personnages) / 2
            
                #Boucle pour chaque combat
                for x in range(int(nb_combats)) :
                    print(f"-------------Combat {x + 1} (ronde {ronde})-------------")

                    #index des personnages
                    index = 2*x
                
                    #combat
                    self.combattre(index, (index+1))
                
                #nettoyage de l'arène
                self.nettoyer_arene()
            
            #Si le nombre de personnage est impair
            else :
                
                #nombre de combats
                nb_combats = len(self.liste_personnages) // 2 
                
                #Boucle pour faire combattre chaque personnage de la liste
                for x in range(int(nb_combats)) :
                    print(f"-------------Combat {x + 1} (ronde {ronde})-------------")
                    
                    #index des personnages
                    index = 2*x
                
                    #combat
                    self.combattre(index, (index+1))
                
                #nettoyage de l'arène
                self.nettoyer_arene()
        
        #Impression du gagnant du battle royale
        print(f"Le gagnant du battle royale est {self.liste_personnages[0].nom}!")