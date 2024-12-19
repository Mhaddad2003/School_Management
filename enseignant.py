import os

FILE_PATH = "../Data/Enseignant.txt"

def ajouter_enseignant():
    print("Entrez les détails de l'enseignant à ajouter:")

    enseignant_id = input("ID_Enseignant: ")

    # Check if the ID already exists
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(enseignant_id + ","):
                print("Erreur: Un enseignant avec cet ID existe déjà.")
                return

    nom = input("Nom: ")
    prenom = input("Prénom: ")
    cin = input("CIN: ")
    dept = input("Departement: ")

    new_enseignant_data = f"{enseignant_id},{nom},{prenom},{cin},{dept}\n"

    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(new_enseignant_data)

    print("\nEnseignant ajouté avec succès!")

def lister_enseignants():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = f.readline()
        line_number = 1

        print("=" * 80)
        print(f"{'ID_Enseignant':<12} {'Nom':<20} {'Prénom':<20} {'CIN':<10} {'Departement':<15}")
        print("=" * 80)

        while data:
            data = data.strip()
            enseignant_data = data.split(',')

            print(f"{enseignant_data[0]:<12} {enseignant_data[1]:<20} {enseignant_data[2]:<20} {enseignant_data[3]:<10} {enseignant_data[4]:<15}")

            line_number += 1
            data = f.readline()

        print("=" * 80)

def modifier_enseignant():
    enseignant_id = input("Entrez l'ID de l'enseignant à modifier: ")
    found = False
    new_lines = []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(enseignant_id + ","):
            found = True
            print("Enseignant trouvé. Entrez les nouvelles valeurs:")
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            cin = input("CIN: ")
            dept = input("Departement: ")
            new_line = f"{enseignant_id},{nom},{prenom},{cin},{dept}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Enseignant modifié avec succès!")
    else:
        print("Enseignant non trouvé.")

def supprimer_enseignant():
    enseignant_id = input("Entrez l'ID de l'enseignant à supprimer: ")
    found = False
    new_lines = []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(enseignant_id + ","):
            found = True
            print("Enseignant supprimé avec succès!")
        else:
            new_lines.append(line)

    if found:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    else:
        print("Enseignant non trouvé.")

def gestion_enseignant():
    while True:
        print("Espace Enseignant : Liste des choix".center(50, "#"))
        print("1: Ajouter un enseignant")
        print("2: Lister les enseignants")
        print("3: Modifier un enseignant")
        print("4: Supprimer un enseignant")
        print("0: Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_enseignant()
        elif choix == "2":
            lister_enseignants()
        elif choix == "3":
            modifier_enseignant()
        elif choix == "4":
            supprimer_enseignant()
        elif choix == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer!")

gestion_enseignant()