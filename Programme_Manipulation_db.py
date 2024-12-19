import sqlite3

# Connexion à la base de données

def connect_db():
    return sqlite3.connect("Gestion_Scolarite.db")
    
# Fonctions pour l'étudiant 

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
    
def etudiant_existe(num_apogee):
    conn = connect_db()
    curs = conn.cursor()
    
    curs.execute("SELECT 1 FROM Etudiant WHERE num_apogee = ?", (num_apogee,))
    result = curs.fetchone()
    
    conn.close()
    
    return result is not None
  
def supprimer_etudiant():
    conn = connect_db()
    curs = conn.cursor()
    num_apogee = int(input("Entrez le numéro d'apogée de l'étudiant à supprimer : "))
    
    if etudiant_existe(num_apogee):
        curs.execute("DELETE FROM Etudiant WHERE num_apogee = ?", (num_apogee,))
        
        conn.commit()
        conn.close()
        
        print(f"Étudiant avec le numéro d'apogée {num_apogee} supprimé!")
    else:
        print("Aucun étudiant trouvé avec ce numéro d'apogée!")
        
def modifier_etudiant():
    conn = connect_db()
    curs = conn.cursor()
    num_apogee = input("Entrez le numéro d'apogée de l'étudiant à modifier : ")
    
    if etudiant_existe(num_apogee):
        nom = input("Entrez le nouveau nom de l'étudiant en cas de saisie incorrecte  : ")
        
        curs.execute("Update Etudiant set nom = ? WHERE num_apogee = ?", (nom, num_apogee,))
        
        conn.commit()
        conn.close()
        
        print(f"Étudiant avec le numéro d'apogée {num_apogee} modifié!")
    else:
        print("Aucun étudiant trouvé avec ce numéro d'apogée!")

def lister_etudiant():
    conn = connect_db()
    curs = conn.cursor()
    print("La liste des étudiants :")
    
    curs.execute("SELECT * FROM Etudiant")
    etudiants = curs.fetchall()
    
    if etudiants:
        print("La liste des étudiants :")
        print(f"{'Numéro dapogée':<19} {'Nom':<20} {'Prénom':<20} {'CIN':<20} {'Date de naissance':<15}")
        print("-" * 100)  
        
        for etudiant in etudiants:
            print(f"{etudiant[0]:<19} {etudiant[1]:<20} {etudiant[2]:<20} {etudiant[3]:<20} {etudiant[4]:<15}")
    else:
        print("Aucun étudiant trouvé dans la base de données!")

def inscrit_etudiant():
    conn = connect_db()
    curs = conn.cursor()

    module_id = input("Entrez l'id du module : ")
    etu_apo = input("Entrez l'apogee d'etudiant : ")
    if module_existe(module_id) and etudiant_existe(etu_apo):
        note = input("Entrez la note du etudiant : ")
        valide = input("validation (V: valide/NV:non valide/AS:compose): ")
        curs.execute("INSERT INTO Inscrire VALUES (?, ?, ?, ?)", (module_id, etu_apo, note, valide))
        conn.commit()
    else:
        print("le numero d'apogee ou l'id de module est incorrect")
    conn.close()

def update_note():
    conn = connect_db()
    curs = conn.cursor()
    module_id = input("Entrez l'id du module : ")
    etu_apo = input("Entrez l'apogee d'etudiant : ")
    curs.execute("SELECT * FROM Inscrire WHERE module_id = ? and etudiant_apogee = ?", (module_id, etu_apo))
    result = curs.fetchone()

    if result:
        note = input("Entrez la note d'etudiant : ")
        curs.execute("UPDATE Inscrire SET note = ?"
                     "WHERE module_id = ? and etudiant_apogee = ?", (note, module_id, etu_apo)
                     )
        conn.commit()
        if (int(note) < 10):
            curs.execute("UPDATE Inscrire SET valide = 'NV'"
                         "WHERE module_id = ? and etudiant_apogee = ?", (module_id, etu_apo)
                         )
            conn.commit()
        else:
            curs.execute("UPDATE Inscrire SET valide = 'V'"
                         "WHERE module_id = ? and etudiant_apogee = ?", (module_id, etu_apo)
                         )
            conn.commit()

    else:
        print("le numero d'apogee ou l'id de module est incorrect")
    conn.close()

def sup_inscrit():
    conn = connect_db()
    curs = conn.cursor()
    module_id = input("Entrez l'id du module : ")
    etu_apo = input("Entrez l'apogee d'etudiant : ")
    curs.execute("SELECT * FROM Inscrire WHERE module_id = ? and etudiant_apogee = ?", (module_id, etu_apo))
    result = curs.fetchone()
    if result:
        curs.execute(
            "DELETE FROM Inscrire WHERE module_id = ? AND etudiant_apogee = ?",
            (module_id, etu_apo)
        )
        conn.commit()
        print("la suppression se fait avec succes")
    else:
        print("le numero d'apogee ou l'id de module est incorrect")
    conn.close()

class Switch:
    value = None
    def __new__(class_, value):
        class_.value = value
        return value
def case(*args):
    return any((arg == Switch.value) for arg in args)

# Fonctions pour l'enseignant

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

# Fonctions pour le module 

def module_existe(id):
    conn = connect_db()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM Module WHERE id = ?", (id,))
    result = curs.fetchone()
    
    conn.close()
    
    return result is not None


def ajouter_module():
    conn = connect_db()
    curs = conn.cursor()
    
    try:
        id_ens = int(input("Entrez l'ID de l'enseignant : "))


        curs.execute("SELECT COUNT(*) FROM Enseignant WHERE id = ?", (id_ens,))
        exists = curs.fetchone()[0]
        
        if exists:
            matiere = input("Entrez le nom de la matière : ").strip()
            semester = input("Entrez le numéro du semestre : ").strip()
            

            if not matiere or not semester:
                print("Les champs 'matière' et 'semestre' ne peuvent pas être vides.")
                return
            
            donnees_Module = (id_ens, matiere, semester)
            curs.execute("INSERT INTO Module(Enseignant_id, matiere, semestre) VALUES (?, ?, ?)", donnees_Module)
            
            conn.commit()
            print("Module ajouté avec succès!")
        else:
            print("L'enseignant avec cet ID n'existe pas.")
    except ValueError:
        print("Veuillez entrer un ID valide pour l'enseignant.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'ajout du module : {e}")
    finally:
        conn.close()  # Ensure connection is always closed


def supp_module():
    conn = connect_db()
    curs = conn.cursor()
    
    id = int(input("Entrez l'ID du Module à supprimer : "))
    
    if module_existe(id):
        try:

            curs.execute("DELETE FROM Module WHERE id = ?", (id,))
            conn.commit()
            
            if curs.rowcount > 0:
                print(f"Le module avec l'ID {id} a été supprimé avec succès.")
            else:
                print(f"Aucun module trouvé avec l'ID {id}.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression du module : {e}")
        finally:
            conn.close()
    else:
        print("Le module n'exist pas")

def modifier_module():
    conn = connect_db()
    curs = conn.cursor()
    
    id = int(input("Entrez l'ID du Module à mettre à jour : "))
    
    if module_existe(id):
        try:
            nouveau_semestre = input("Entrez le nouveau numéro de semestre : ")
            
            curs.execute("UPDATE Module SET semestre = ? WHERE id = ?", (nouveau_semestre, id))
            conn.commit()
            
            if curs.rowcount > 0:
                print(f"Le semestre du module avec l'ID {id} a été mis à jour avec succès à {nouveau_semestre}.")
            else:
                print(f"Aucun module trouvé avec l'ID {id}.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la mise à jour du semestre : {e}")
        finally:
            conn.close()
    else:
        print("Le module n'existe pas.")

        
        
def lister_modules():
    conn = connect_db()
    curs = conn.cursor()
    
    try:
        print("La liste des modules :")
        
    
        curs.execute("SELECT * FROM Module")
        modules = curs.fetchall()
        
      
        if modules:
    
            print(f"{'ID':<10} {'Enseignant ID':<20} {'Matière':<20} {'Semestre':<10}")
            print("-" * 70)
            
     
            for module in modules:
                print(f"{module[0]:<10} {module[1]:<20} {module[2]:<20} {module[3]:<10}")
        else:
            print("Aucun module trouvé dans la base de données.")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'affichage des modules : {e}")
    finally:
        conn.close()

# Menu pour l'étudiant 

def menuEtd():
    while True:

        print("Espace Etudiant : Liste des choix".center(60, "-"))
        print("1: Ajouter un étudiant")
        print("2: Modifier un étudiant")
        print("3: Supprimer un étudiant")
        print("4: Lister l'ensemble des étudiants")
        print("5: inscrit l'etudiant dans un model")
        print("6: Modifier la note de l'etudiant")
        print("7: Delete une inscription")
        print("0: Quitter")
        choix = input("Entrer votre choix: ")

        switch = Switch(choix)

        if case("1"):
            print("Choix 1: Ajouter un étudiant")
            ajouter_etudiant() 
        elif case("2"):
            print("Choix 2: Modifier un étudiant")
            modifier_etudiant()
        elif case("3"):
            print("Choix 3: Supprimer un étudiant")
            supprimer_etudiant()
        elif case("4"):
            print("Choix 4: Lister les étudiants")
            lister_etudiant()
        elif case("5"):
            print("Choix 5: inscrit l'etudiant dans un model")
            inscrit_etudiant()
        elif case("6"):
            print("Choix 6: Modifier la note de l'etudiant")
            update_note()
        elif case("7"):
            print("Choix 7: Delete un inscription")
            sup_inscrit()
        elif case("0"):
            print("Au revoir!")
            break 
        else:
            print("Choix invalide, veuillez réessayer!")
            
# Menu pour l'enseignant

def menu_enseignant():
    while True:
        print("Liste des choix".center(60, "-"))
        print("1: Ajouter un nouveau enseignant")
        print("2: Supprimer un enseignant")
        print("3: Afficher la liste des enseignants")
        print("4: Modifier les information d'un enseignant")
        print("0: Quitter")
        c1 = input("Entrer votre choix: ")
        while Switch(c1):
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

# Menu pour le module

def gestion_module():
    while True:
        print("Espace Etudiant : Liste des choix".center(10, "#"))
        print("1: Ajouter un module")
        print("2: Modifier un module")
        print("3: Supprimer un module")
        print("4: Lister les modules")
        print("0: Quitter")
        choix = input("Entrer votre choix: ")

        switch = Switch(choix)

        if case("1"):
            print("Choix 1: Ajouter un Module")
            ajouter_module() 
        elif case("2"):
            print("Choix 2: Modifier un Module")
            modifier_module()
        elif case("3"):
            print("Choix 3: Supprimer un Module")
            supp_module()
        elif case("4"):
            print("Choix 4: Lister les Modules")
            lister_modules()
        elif case("0"):
            print("Au revoir!")
            break 
        else:
            print("Choix invalide, veuillez réessayer!")
            
# Menu principal

def menuPrincipal():
    while True:

        print("Espace Scolarité : Liste des choix".center(60, "-"))
        print("1: Espace étudiant")
        print("2: Espace enseignant")
        print("3: Espace module")
        print("0: Quitter")
        choix = input("Entrer votre choix : ")

        switch = Switch(choix)

        if case("1"):
            print("Choix 1: Espace étudiant")
            menuEtd() 
        elif case("2"):
            print("Choix 2: Espace enseignant")
            menu_enseignant()
        elif case("3"):
            print("Choix 3: Espace module")
            gestion_module()
        elif case("0"):
            print("Au revoir!")
            break 
        else:
            print("Choix invalide, veuillez réessayer!")
            
menuPrincipal()