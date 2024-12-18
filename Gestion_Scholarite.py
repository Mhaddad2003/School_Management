import sqlite3
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return value
def case(*args):
    return any((arg == switch.value) for arg in args)

def connect_db():
    return sqlite3.connect("Gestion_Scolarite.db")

def exist_enseignant(id):
    conn = connect_db()
    curs = conn.cursor()
    curs.execute("SELECT * FROM Enseignant WHERE id=?", (id))
    res = curs.fetchone()
    conn.close()
    return res is not None

def ajouter_enseignant():
    conn = connect_db()
    curs = conn.cursor()
    nom = input("Entrez le nom de l'enseignant: ")
    prenom = input("Entrez le prénom de l'enseignant: ")
    cin = input("Entrez le cin de l'enseignant: ")
    dept = input("Entrez le departement de l'enseignant: ")

    curs.execute("INSERT INTO Enseignant (nom, prenom, cin, departement) "
                 "VALUES (?, ?, ?, ?)", (nom, prenom, cin, dept))
    conn.commit()
    conn.close()

def delete_enseignant():
    conn = connect_db()
    curs = conn.cursor()
    ens_id = input("Entrez l'id de l'enseignant: ")
    if exist_enseignant(ens_id):
        curs.execute("DELETE FROM Enseignant WHERE id = ?", ens_id)
    else:
        print("Enseignant n'existe pas")
    conn.commit()
    conn.close()

def lister_enseignant():
    conn = connect_db()
    curs = conn.cursor()
    curs.execute("SELECT * FROM Enseignant")
    results = curs.fetchall()
    print("_" * 70)
    print("|    ID    |    Nom    |    Prenom    |    CIN    |    Departement    |")
    print("_" * 70)
    for res in results:
        print(f"|    {res[0]}    |  {res[1]}   |   {res[2]}    |   {res[3]}    |   {res[4]}   |")
        print("_" * 70)
    conn.commit()
    conn.close()

def update_enseignant():
    conn = connect_db()
    curs = conn.cursor()
    ens_id = input("Entrez l'id de l'enseignant: ")
    if exist_enseignant(ens_id):
        curs.execute("UPDATE Enseignant SET departement = ?"
                     "WHERE id = ?",
                     (input("Entrez le nouveau departement de l'enseignant: "), ens_id)
                     )
        conn.commit()
    else:
        print("Enseignant n'existe pas")
    conn.close()


def menu_enseignant():
    while True:
        print("Liste des choix".center(10, "#"))
        print("1: Ajouter un nouveau enseignant")
        print("2: Supprimer un enseignant")
        print("3: Afficher la liste des enseignants")
        print("4: Modifier les information d'un enseignant")
        print("0: Quitter")
        c1 = input("Entrer votre choix: ")
        while switch(c1):
            if case("0"):
                print("Au revoir")
                break
            elif case("1"):
                ajouter_enseignant()
                break
            elif case("2"):
                delete_enseignant()
                break
            elif case("3"):
                lister_enseignant()
                break
            elif case("4"):
                update_enseignant()
                break
            else:
                print("Invalide choix")
                break
        if c1 == "0":
            break

while True:
    print("Liste des choix".center(10, "#"))
    print("1: Gestion des Enseignants")
    print("2: choix 2")
    print("3: ")
    print("0: Quitter")
    choix = input("Entrer votre choix: ")

    while switch(choix):
        if case("1"):
            menu_enseignant()
            break
        if case("2"):
            print("choix 2")
            break
        if case("3"):
            print("choix 3")
            break
        else:
           print("invalid choix")
           break

    if choix == "0":
        break



