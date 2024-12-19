
import os

FILE_PATH = "../Data/Module.txt"


def ajouter_module():
    module_id = input("ID_Module: ")

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(module_id + ","):
                print("L'ID du module existe déjà. Veuillez entrer un ID unique.")
                return

    print("Entrez les détails du module à ajouter:")
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

def modifier_module():
    module_id = input("Entrez l'ID du module à modifier: ")
    found = False
    new_lines = []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(module_id + ","):
            found = True
            print("Module trouvé. Entrez les nouvelles valeurs:")
            nom_module = input("Nom_Module: ")
            semester = input("Semester: ")
            new_line = f"{module_id},{nom_module},{semester}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Module modifié avec succès!")
    else:
        print("Module non trouvé.")
def supprimer_module():
                module_id = input("Entrez l'ID du module à supprimer: ")
                found = False
                new_lines = []

                with open(FILE_PATH, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                for line in lines:
                    if line.startswith(module_id + ","):
                        found = True
                        print("Module supprimé avec succès!")
                    else:
                        new_lines.append(line)

                if found:
                    with open(FILE_PATH, "w", encoding="utf-8") as f:
                        f.writelines(new_lines)
                else:
                    print("Module non trouvé.")
                    

def gestion_module():
    while True:
        print("Espace Étudiant : Liste des choix".center(50, "#"))
        print("1: Ajouter un module")
        print("2: Lister les modules")
        print("3: Modifier un module")
        print("4: Supprimer un module")
        print("0: Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_module()
        elif choix == "2":
            lister_modules()
        elif choix == "3":
            modifier_module()
        elif choix == "4":
            supprimer_module()
        elif choix == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer!")

gestion_module()
