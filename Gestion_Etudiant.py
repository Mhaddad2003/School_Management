import sqlite3

def connect_db():
    return sqlite3.connect("C:/Users/hp/Downloads/Gestion_Scolarite.db")
    
def ajouter_etudiant():
    conn = connect_db()
    curs = conn.cursor()
    
    num_apogee = input("Entrez le numéro d'apogée de l'étudiant : ")
    nom = input("Entrez le nom de l'étudiant : ")
    prenom = input("Entrez le prénom de l'étudiant : ")
    cin = input("Entrez le CIN de l'étudiant : ")
    date_naiss = input("Entrez la date de naissance de l'étudiant (format AAAA-MM-JJ) : ")
    
    donnees_Etd = (num_apogee, nom, prenom, cin, date_naiss)
    
    curs.execute("INSERT INTO Etudiant(num_apogee, nom, prenom, cin, date_naiss) VALUES (?, ?, ?, ?, ?)", donnees_Etd)

    conn.commit()
    conn.close()

    print("Étudiant ajouté avec succès!")
    
class Switch:
    value = None
    def __new__(class_, value):
        class_.value = value
        return value

def case(*args):
    return any((arg == Switch.value) for arg in args)

while True:

    print("Espace Etudiant : Liste des choix".center(10, "#"))
    print("1: Ajouter un étudiant")
    print("2: Modifier un étudiant")
    print("3: Supprimer un étudiant")
    print("4: Lister l'ensemble des étudiants")
    print("0: Quitter")
    choix = input("Entrer votre choix: ")

    switch = Switch(choix)

    if case("1"):
        print("Choix 1: Ajouter un étudiant")
        ajouter_etudiant() 
    elif case("2"):
        print("Choix 2: Modifier un étudiant")
    elif case("3"):
        print("Choix 3: Supprimer un étudiant")
    elif case("4"):
        print("Choix 4: Lister les étudiants")
    elif case("0"):
        print("Au revoir!")
        break 
    else:
        print("Choix invalide, veuillez réessayer!")
