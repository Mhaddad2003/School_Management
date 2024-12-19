import os

FILE_PATH1 = "C:/Users/HP/Downloads/Master 2I/s1/Interaction Humain Technologies/IHM projets/projet1/data/Etudiant.txt"
FILE_PATH2 = "C:/Users/HP/Downloads/Master 2I/s1/Interaction Humain Technologies/IHM projets/projet1/data/Enseignant.txt"
FILE_PATH3 = "C:/Users/HP/Downloads/Master 2I/s1/Interaction Humain Technologies/IHM projets/projet1/data/Module.txt"


# Fonctions pour l'étudiant 

def ajouter_etudiant():
    print("Entrez les détails de l'étudiant à ajouter :")

    student_id = input("ID_Étudiant: ")

    # Vérifier si l'étudiant déjà existe
    with open(FILE_PATH1, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(student_id + ","):
                print("Un étudiant avec cet ID existe déjà!")
                return

    nom = input("Nom : ")
    prenom = input("Prénom : ")
    cin = input("CIN : ")
    date_naissance = input("Date de Naissance (YYYY-MM-DD) : ")

    new_student_data = f"{student_id},{nom},{prenom},{cin},{date_naissance}\n"

    with open(FILE_PATH1, "a", encoding="utf-8") as f:
        f.write(new_student_data)

    print("\nÉtudiant ajouté avec succès!")

def modifier_etudiant():
    student_id = input("Entrez l'ID de l'étudiant à modifier : ")
    found = False
    new_lines = []

    with open(FILE_PATH1, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(student_id + ","):
            found = True
            print("Étudiant trouvé! Entrez les nouvelles valeurs :")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            cin = input("CIN : ")
            date_naissance = input("Date de Naissance (YYYY-MM-DD) : ")
            new_line = f"{student_id},{nom},{prenom},{cin},{date_naissance}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH1, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Étudiant modifié avec succès!")
    else:
        print("Étudiant non trouvé!")

def supprimer_etudiant():
    student_id = input("Entrez l'ID de l'étudiant à supprimer : ")
    found = False
    new_lines = []

    with open(FILE_PATH1, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(student_id + ","):
            found = True
            print("Étudiant supprimé avec succès!")
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH1, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    else:
        print("Étudiant non trouvé!")
        
def lister_etudiant():
    with open(FILE_PATH1, "r", encoding="utf-8") as f:
        data = f.readline()
        line_number = 1

        print("=" * 100)
        print(f"{'ID_Étudiant':<12} {'Nom':<20} {'Prénom':<20} {'CIN':<10} {'Date de Naissance':<15}")
        print("=" * 100)

        while data:
            data = data.strip()
            student_data = data.split(',')

            print(f"{student_data[0]:<12} {student_data[1]:<20} {student_data[2]:<20} {student_data[3]:<10} {student_data[4]:<15}")

            line_number += 1
            data = f.readline()

        print("=" * 100)

# Fonctions pour l'enseignant

def ajouter_enseignant():
    print("Entrez les détails de l'enseignant à ajouter :")

    enseignant_id = input("ID_Enseignant: ")

    # Vérifier si l'enseignant déjà existe
    with open(FILE_PATH2, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(enseignant_id + ","):
                print("Erreur: Un enseignant avec cet ID existe déjà!")
                return

    nom = input("Nom : ")
    prenom = input("Prénom : ")
    cin = input("CIN : ")
    dept = input("Departement : ")

    new_enseignant_data = f"{enseignant_id},{nom},{prenom},{cin},{dept}\n"

    with open(FILE_PATH2, "a", encoding="utf-8") as f:
        f.write(new_enseignant_data)

    print("\nEnseignant ajouté avec succès!")

def modifier_enseignant():
    enseignant_id = input("Entrez l'ID de l'enseignant à modifier : ")
    found = False
    new_lines = []

    with open(FILE_PATH2, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(enseignant_id + ","):
            found = True
            print("Enseignant trouvé. Entrez les nouvelles valeurs :")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            cin = input("CIN : ")
            dept = input("Departement : ")
            new_line = f"{enseignant_id},{nom},{prenom},{cin},{dept}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH2, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Enseignant modifié avec succès!")
    else:
        print("Enseignant non trouvé!")

def supprimer_enseignant():
    enseignant_id = input("Entrez l'ID de l'enseignant à supprimer : ")
    found = False
    new_lines = []

    with open(FILE_PATH2, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(enseignant_id + ","):
            found = True
            print("Enseignant supprimé avec succès!")
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH2, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    else:
        print("Enseignant non trouvé!")
        
def lister_enseignant():
    with open(FILE_PATH2, "r", encoding="utf-8") as f:
        data = f.readline()
        line_number = 1

        print("=" * 100)
        print(f"{'ID_Enseignant':<20} {'Nom':<20} {'Prénom':<20} {'CIN':<10} {'Departement':<15}")
        print("=" * 100)

        while data:
            data = data.strip()
            enseignant_data = data.split(',')

            print(f"{enseignant_data[0]:<20} {enseignant_data[1]:<20} {enseignant_data[2]:<20} {enseignant_data[3]:<10} {enseignant_data[4]:<15}")

            line_number += 1
            data = f.readline()

        print("=" * 100)
        
# Fonctions pour le module

def ajouter_module():
    module_id = input("ID_Module : ")

    with open(FILE_PATH3, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(module_id + ","):
                print("L'ID du module existe déjà! Veuillez entrer un ID unique!")
                return

    print("Entrez les détails du module à ajouter : ")
    nom_module = input("Nom_Module : ")
    semester = input("Semester : ")

    new_module_data = f"{module_id},{nom_module},{semester}\n"

    with open(FILE_PATH3, "a", encoding="utf-8") as f:
        f.write(new_module_data)

    print("\nModule ajouté avec succès!")

def modifier_module():
    module_id = input("Entrez l'ID du module à modifier : ")
    found = False
    new_lines = []

    with open(FILE_PATH3, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(module_id + ","):
            found = True
            print("Module trouvé. Entrez les nouvelles valeurs : ")
            nom_module = input("Nom_Module : ")
            semester = input("Semester : ")
            new_line = f"{module_id},{nom_module},{semester}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH3, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Module modifié avec succès!")
    else:
        print("Module non trouvé!")
        
def supprimer_module():
    module_id = input("Entrez l'ID du module à supprimer : ")
    found = False
    new_lines = []

    with open(FILE_PATH3, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(module_id + ","):
            found = True
            print("Module supprimé avec succès!")
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH3, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    else:
        print("Module non trouvé!")
                    
def lister_modules():
    with open(FILE_PATH3, "r", encoding="utf-8") as f:
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

# Menu pour l'étudiant

def menu_etudiant():
    while True:
        print("Espace Étudiant : Liste des choix".center(50, "-"))
        print("1: Ajouter un étudiant")
        print("2: Modifier un étudiant")
        print("3: Supprimer un étudiant")
        print("4: Lister les étudiants")
        print("0: Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            print("Choix 1: Ajouter un étudiant")
            ajouter_etudiant()
        elif choix == "2":
            print("Choix 2: Modifier un étudiant")
            modifier_etudiant()
        elif choix == "3":
            print("Choix 3: Supprimer un étudiant")
            supprimer_etudiant()
        elif choix == "4":
            print("Choix 4: Lister les étudiants")
            lister_etudiant()
        elif choix == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer!")
    
# Menu pour l'enseignant        
    
def menu_enseignant():
    while True:
        print("Espace Enseignant : Liste des choix".center(50, "-"))
        print("1: Ajouter un enseignant")
        print("2: Modifier un enseignant")
        print("3: Supprimer un enseignant")
        print("4: Lister les enseignants")
        print("0: Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            print("Choix 1: Ajouter un étudiant")
            ajouter_enseignant()
        elif choix == "2":
            print("Choix 2: Modifier un enseignant")
            modifier_enseignant()
        elif choix == "3":
            print("Choix 3: Supprimer un enseignant")
            supprimer_enseignant()
        elif choix == "4":
            print("Choix 4: Lister les enseignants")
            lister_enseignant()
        elif choix == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer!")
            
#  Menu pour le module

def menu_module():
    while True:
        print("Espace Étudiant : Liste des choix".center(50, "-"))
        print("1: Ajouter un module")
        print("2: Modifier un module")
        print("3: Supprimer un module")
        print("4: Lister les modules")
        print("0: Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            print("Choix 1: Ajouter un module")
            ajouter_module()
        elif choix == "2":
            print("Choix 2: Modifier un module")
            modifier_module()
        elif choix == "3":
            print("Choix 3: Supprimer un module")
            supprimer_module()
        elif choix == "4":
            print("Choix 4: Lister les modules")
            lister_modules()
        elif choix == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer!")
            
# Menu principal

def menuPrincipal():
    while True:

        print("Espace Scolarité : Liste des choix".center(50, "-"))
        print("1: Espace étudiant")
        print("2: Espace enseignant")
        print("3: Espace module")
        print("0: Quitter")
        choix = input("Entrer votre choix : ")

        if choix == "1":
            print("Choix 1: Espace étudiant")
            menu_etudiant() 
        elif choix == "2":
            print("Choix 2: Espace enseignant")
            menu_enseignant()
        elif choix == "3":
            print("Choix 3: Espace module")
            menu_module()
        elif choix == "0":
            print("Au revoir!")
            break 
        else:
            print("Choix invalide, veuillez réessayer!")
            
menuPrincipal()