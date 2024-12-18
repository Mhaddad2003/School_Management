import sqlite3

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return value
def case(*args):
    return any((arg == switch.value) for arg in args)



conn = sqlite3.connect("Gestion_Scolarite.db")
curs = conn.cursor()

while True:

    print("Liste des choix".center(10, "#"))
    print("1: Gestion des Enseignants")
    print("2: choix 2")
    print("3: ")
    print("0: Quitter")
    choix = input("Entrer votre choix: ")

    while switch(choix):
        if case("1"):
            while True:
                print("Liste des choix".center(10, "#"))
                print("1: Ajouter un nouveau enseignant")
                print("2: Supprimer un enseignant")
                print("3: Afficher la liste des enseignants")
                print("4: Modifier les information d'un enseignant")
                print("0: Quitter")
                c1 = input("Entrer votre choix: ")
                while switch(c1):
                    conn = sqlite3.connect("Gestion_Scolarite.db")
                    curs = conn.cursor()
                    if case("0"):
                        print("Au revoir")
                        break
                    if case("1"):
                        curs.execute("INSERT INTO Enseignant (nom, prenom, cin, departement) "
                                     "VALUES (?, ?, ?, ?)",
                                     (input("Nom: "),
                                      input("prenom: "),
                                      input("CIN: "),
                                     input("departement: "))
                                     )
                        conn.commit()
                        break
                    if case("2"):
                        curs.execute("DELETE FROM Enseignant "
                                     "WHERE id = ?", input("Enseignant id : "))
                        conn.commit()
                        break
                    if case("3"):
                        curs.execute("SELECT * FROM Enseignant")
                        results = curs.fetchall()
                        print("_"*70)
                        print("|    ID    |    Nom    |    Prenom    |    CIN    |    Departement    |")
                        print("_"*70)
                        for res in results:
                            print(f"|    {res[0]}    |  {res[1]}   |   {res[2]}    |   {res[3]}    |   {res[4]}   |")
                            print("_"*70)
                        conn.commit()
                        break
                    if case(""):
                        curs.execute("DELETE FROM Enseignant "
                                     "WHERE id = ?", input("Enseignant id : "))
                        conn.commit()
                        break
                    else:
                        print("Invalide choix")
                        break


                    conn.close()
                if c1 == "0":
                    break

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



