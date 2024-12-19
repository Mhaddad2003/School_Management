import os

FILE_PATH = "./Module.txt"


def ajouter_module():

    print("Entrez les détails du module à ajouter:")

    module_id = input("ID_Module: ")
    nom_module = input("Nom_Module: ")
    semester = input("Semester: ")


    new_module_data = f"{module_id},{nom_module},{semester}\n"

    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(new_module_data)  

    print("\nModule ajouté avec succès!")



def lister_modules():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = f.readline()  
        line_number = 1  
        
        print("=" * 80)
        print(f"{'ID_Module':<12} {'Nom_Module':<45} {'Semester':<10}")
        print("=" * 80)
        
        while data:
            data = data.strip()
            
            module_data = data.split(',')

            print(f"{module_data[0]:<12} {module_data[1]:<45} {module_data[2]:<10}")
            

            line_number += 1
            data = f.readline()

        print("=" * 80)


def gestion_module():
    while True:
        print("Espace Étudiant : Liste des choix".center(50, "#"))
        print("1: Ajouter un module")
        print("2: Lister les modules")
        print("0: Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_module()
        elif choix == "2":
            lister_modules()
        elif choix == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer!")

gestion_module()
