import os

FILE_PATH = "../Data/Etudiant.txt"

def ajouter_etudiant():
    print("Entrez les détails de l'étudiant à ajouter:")

    student_id = input("ID_Étudiant: ")

    # Check if the student ID already exists
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(student_id + ","):
                print("Un étudiant avec cet ID existe déjà.")
                return

    nom = input("Nom: ")
    prenom = input("Prénom: ")
    cin = input("CIN: ")
    date_naissance = input("Date de Naissance (YYYY-MM-DD): ")

    new_student_data = f"{student_id},{nom},{prenom},{cin},{date_naissance}\n"

    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(new_student_data)

    print("\nÉtudiant ajouté avec succès!")

def lister_etudiants():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = f.readline()
        line_number = 1

        print("=" * 80)
        print(f"{'ID_Étudiant':<12} {'Nom':<20} {'Prénom':<20} {'CIN':<10} {'Date de Naissance':<15}")
        print("=" * 80)

        while data:
            data = data.strip()
            student_data = data.split(',')

            print(f"{student_data[0]:<12} {student_data[1]:<20} {student_data[2]:<20} {student_data[3]:<10} {student_data[4]:<15}")

            line_number += 1
            data = f.readline()

        print("=" * 80)

def modifier_etudiant():
    student_id = input("Entrez l'ID de l'étudiant à modifier: ")
    found = False
    new_lines = []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(student_id + ","):
            found = True
            print("Étudiant trouvé. Entrez les nouvelles valeurs:")
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            cin = input("CIN: ")
            date_naissance = input("Date de Naissance (YYYY-MM-DD): ")
            new_line = f"{student_id},{nom},{prenom},{cin},{date_naissance}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Étudiant modifié avec succès!")
    else:
        print("Étudiant non trouvé.")

def supprimer_etudiant():
    student_id = input("Entrez l'ID de l'étudiant à supprimer: ")
    found = False
    new_lines = []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(student_id + ","):
            found = True
            print("Étudiant supprimé avec succès!")
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    else:
        print("Étudiant non trouvé.")

def gestion_etudiant():
    while True:
        print("Espace Étudiant : Liste des choix".center(50, "#"))
        print("1: Ajouter un étudiant")
        print("2: Lister les étudiants")
        print("3: Modifier un étudiant")
        print("4: Supprimer un étudiant")
        print("0: Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_etudiant()
        elif choix == "2":
            lister_etudiants()
        elif choix == "3":
            modifier_etudiant()
        elif choix == "4":
            supprimer_etudiant()
        elif choix == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer!")

gestion_etudiant()