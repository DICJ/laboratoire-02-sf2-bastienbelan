from personnage import Personnage
from archer import Archer
from guerrier import Guerrier
from mage import Mage
from soldat import Soldat
from berserker import Berserker
from arene import Arene

#fonction permettant d'afficher le menu
def afficher_menu() :
    print("---------------Menu---------------")
    print("1. Ajouter un personnage")
    print("2. Voir les personnages de l'arène")
    print("3. Faire combattre deux personnages de l'arène")
    print("4. Afficher l'historique des combats")
    print("5. Soigner un personnage")
    print("6. Nettoyer l'arène")
    print("7. Voir le nombre de combattants dans l'arène")
    print("8. Lancer le battle royale")
    print("0. quitter")
    print("----------------------------------")

#variables nécessaires
choix = 200
liste_personnage = []
arene = Arene(liste_personnage)

#boucle pour afficher le menu tant que l'utilisateur ne veut pas quitter
while choix != 0 :
    
    #Affichage du menu et demande le choix de l'utilisateur
    afficher_menu()
    choix = int(input("Votre choix : "))
    
    #match case pour le choix de l'utilisateur
    match choix :
        
        #Case pour ajouter un personnage
        case 1 :
            #Demande du type de personnage
            type_personnage = int(input("Quel type de personnages voulez-vous utiliser? (1-Guerrier, 2-Mage, 3-Archer, 4-Soldat, 5-Berserker) : "))
            
            #Si c'est un guerrier
            if type_personnage == 1 :
                
                #Demande des informations à l'utilisateur
                nom = input("Quel est le nom de votre guerrier? : ")
                vie = int(input("Quel est son nombre de points de vie (0 à 500) : "))
                attaque = int(input("Quel est son attaque (0 à 50) : "))
                force = int(input("Quel est sa force? (1 à 50) : "))
                armure = 12

                #Ajout du personnage à l'arène
                arene.ajouter_personnage(Guerrier(nom, vie, attaque, force, armure))
            
            #si c'est un mage
            elif type_personnage == 2 :

                #Demande des informations à l'utilisateur
                nom = input("Quel est le nom de votre mage? : ")
                vie = int(input("Quel est son nombre de points de vie (0 à 500) : "))
                attaque = int(input("Quel est son attaque (0 à 50) : "))
                mana = int(input("Quel est la valeur de sa mana? (0 à 100) : "))
                armure = 5

                #Ajout du personnage à l'arène
                arene.ajouter_personnage(Mage(nom, vie, attaque, mana, armure))
            
            #si c'est un archer
            elif type_personnage == 3 :

                #Demande des informations à l'utilisateur
                nom = input("Quel est le nom de votre archer? : ")
                vie = int(input("Quel est son nombre de points de vie (0 à 500) : "))
                attaque = int(input("Quel est son attaque (0 à 50) : "))
                dexterite = int(input("Quel est sa dextérité? (40 à 70) : "))
                armure = 7

                #Ajout du personnage à l'arène
                arene.ajouter_personnage(Archer(nom, vie, attaque, dexterite, armure))

            #Si c'est un soldat    
            elif type_personnage == 4 :
                
                #Demande des informations à l'utilisateur
                nom = input("Quel est le nom de votre soldat? : ")
                vie = int(input("Quel est son nombre de points de vie? (0 à 500) : "))
                attaque = int(input("Quel est son attaque? (0 à 50) : "))
                armure = 15
                
                #Ajout du personnage à l'arène
                arene.ajouter_personnage(Soldat(nom, vie, attaque, armure))
            
            #Si c'est un berserker
            if type_personnage == 5 :
                
                #Demande des informations à l'utilisateur
                nom = input("Quel est le nom de votre berserker? : ")
                vie = int(input("Quel est son nombre de points de vie (0 à 500) : "))
                attaque = int(input("Quel est son attaque (0 à 50) : "))
                force = int(input("Quel est sa force? (1 à 50) : "))
                armure = 12

                #Ajout du personnage à l'arène
                arene.ajouter_personnage(Berserker(nom, vie, attaque, force, armure))
            
            else :
                print("Type de personnage invalide")

        case 2 :
            #Affichage des détails des personnages
            arene.afficher_details_personnages()

        case 3 : 
            #Affichage des noms des personnages
            print("----------------------------------")
            arene.afficher_personnages()
            print("----------------------------------")

            #L'utilisateur choisi quel personnage veut il faire combattre
            index_1 = int(input("Quel est le premier personnage que vous voulez faire combattre? (entrez le numéro) : "))
            index_2 = int(input("Quel est le deuxième personnage que vous voulez faire combattre? (entrez le numéro) : "))
            print("----------------------------------")
            
            #conversion pour avoir l'index de la liste
            index_1 -= 1
            index_2 -= 1
            
            #faire combattre les personnages dans l'arène
            arene.combattre(index_1, index_2)
        
        case 4 :
            #Affichagr de l'historique des combats
            arene.afficher_historique()

        case 5 : 
            #Affichage des personnages
            arene.afficher_personnages()

            #Demande du personnage à soigner
            index_personnage = int(input("Quel personnage voulez-vous soigner? (entrez le numéro): "))
            
            #Conversion pour avoir l'indez du personnage dans la liste
            index_personnage -= 1
             
            #Fonction reset pour le personnage choisi
            arene.soigner_personnage(index_personnage)
        
        case 6 :
            #nettoyer l'arène
            arene.nettoyer_arene()
        
        case 7 :
            #Impression du nombre de combattants en vie dans l'arène
            nombre_combattants = arene.__len__()
            print(f"Il y a {nombre_combattants} combattants dans l'arène.")
        
        case 8 :
            #Battle royal
            arene.battle_royal()

        case 0 :
            pass

        case _ :
            #Message d'erreur
            print("Veuillez choisir un nombre présent dans le menu")

#Affichage de la fin du programme
print("----------------------------------")
print("Fin du programme")