import sqlite3

# Connexion à la base de données

def connect_db():
    return sqlite3.connect("Gestion_Scolarite.db")
    
# Fonctions pour l'étudiant 

def ajouter_etudiant():
    conn = connect_db()
    curs = conn.cursor()
    
    num_apogee = int(input("Entrez le numéro d'apogée de l'étudiant : "))
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

def lister_etudiant():
    conn = connect_db()
    curs = conn.cursor()
    
    print("La liste des étudiants :")
    
    curs.execute("SELECT * FROM Etudiant")
    etudiants = curs.fetchall()
    
    if etudiants:
        print("La liste des étudiants :")
        print(f"{'Numéro d\'apogée':<19} {'Nom':<20} {'Prénom':<20} {'CIN':<20} {'Date de naissance':<15}")
        print("-" * 100)  
        
        for etudiant in etudiants:
            print(f"{etudiant[0]:<19} {etudiant[1]:<20} {etudiant[2]:<20} {etudiant[3]:<20} {etudiant[4]:<15}")
    else:
        print("Aucun étudiant trouvé dans la base de données!")

# Pour la table inscrit

def inscrire_etudiant():
    conn = connect_db()
    curs = conn.cursor()

    module_id = input("Entrez l'id du module : ")
    etu_apo = input("Entrez l'apogee d'étudiant : ")
    if module_existe(module_id) and etudiant_existe(etu_apo):
        note = input("Entrez la note du etudiant : ")
        valide = input("Validation (V:validé / NV : non valide / AS:componsé) : ")
        curs.execute("INSERT INTO Inscrire VALUES (?, ?, ?, ?)", (module_id, etu_apo, note, valide))
        conn.commit()
        print("Success!")
    else:
        print("le numero d'apogee ou l'id de module est incorrect!")
    conn.close()

def modifier_note():
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
        print("Success!")
    else:
        print("Le numero d'apogee ou l'id de module est incorrect!")
    conn.close()
    
def supprimer_inscription():
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
        print("La suppression est faite avec succès!")
    else:
        print("Le numero d'apogee ou l'id de module est incorrect!")
    conn.close()
    
def lister_inscription():
    conn = connect_db()
    curs = conn.cursor()
    print("La liste des Incriptions : ")

    curs.execute("SELECT m.matiere, i.etudiant_apogee, i.note, i.valide FROM Inscrire i JOIN Module m ON i.module_id = m.id")
    data = curs.fetchall()

    if data:
        print(f'{"Module":<15} {"Numero d\'apogee":<20} {"Note":<10} {"Validation":<10}')
        print("-" * 61)

        for line in data:
            print(f"{line[0]:<15} {line[1]:<20} {line[2]:<10} {line[3]:<10}")
    else:
        print("Aucun inscription au module trouvé dans la base de données!")

# Fonctions pour l'enseignant

def ajouter_enseignant():
    conn = connect_db()
    curs = conn.cursor()
    
    nom = input("Entrez le nom de l'enseignant : ")
    prenom = input("Entrez le prénom de l'enseignant : ")
    cin = input("Entrez le cin de l'enseignant : ")
    dept = input("Entrez le departement de l'enseignant : ")

    curs.execute("INSERT INTO Enseignant (nom, prenom, cin, departement) "
                 "VALUES (?, ?, ?, ?)", (nom, prenom, cin, dept))
    
    conn.commit()
    conn.close()
    
    print("Enseignant ajouté avec succès!")
    
def enseignant_existe(id):
    conn = connect_db()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM Enseignant WHERE id = ?", (id,))
    res = curs.fetchone()
    
    conn.close()
    
    return res is not None

def modifier_enseignant():
    conn = connect_db()
    curs = conn.cursor()
    
    ens_id = input("Entrez l'id de l'enseignant : ")
    if enseignant_existe(ens_id):
        curs.execute("UPDATE Enseignant SET departement = ?"
                     "WHERE id = ?",
                     (input("Entrez le nouveau departement de l'enseignant : "), ens_id)
                     )
        
        conn.commit()
        
        print(f"Enseignant avec le id {ens_id} modifié!")
    else:
        print("Aucun enseignant trouvé avec ce id!")
        
    conn.close()

def supprimer_enseignant():
    conn = connect_db()
    curs = conn.cursor()
    
    ens_id = input("Entrez l'id de l'enseignant : ")
    if enseignant_existe(ens_id):
        curs.execute("DELETE FROM Enseignant WHERE id = ?", ens_id)
        print(f"Enseignant avec le id {ens_id} supprimé!")
    else:
        print("Aucun enseignant trouvé avec ce id!")
        
    conn.commit()
    conn.close()

def lister_enseignant():
    conn = connect_db()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM Enseignant")
    results = curs.fetchall()
    
    if results:
        print("La liste des enseignants :")
        print(f"{'ID':<6} {'Nom':<15} {'Prénom':<15} {'CIN':<10} {'Département':<20}")
        print("-" * 61)
        for res in results:
            print(f"{res[0]:<6} {res[1]:<15} {res[2]:<15} {res[3]:<10} {res[4]:<20}")
    else:
        print("Aucun enseignant trouvé dans la base de données!")
        
    conn.commit()
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
            semester = input("Entrez le numéro de la semestre (s1/s2/s3/s4) : ").strip()
            

            if not matiere or not semester:
                print("Les champs 'matière' et 'semestre' ne peuvent pas être vides!")
                return
            
            donnees_Module = (id_ens, matiere, semester)
            curs.execute("INSERT INTO Module(Enseignant_id, matiere, semestre) VALUES (?, ?, ?)", donnees_Module)
            
            conn.commit()
            print("Module ajouté avec succès!")
        else:
            print("Le module avec cet ID n'existe pas!")
    except ValueError:
        print("Veuillez entrer un ID valide pour le module!")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'ajout du module : {e}")
    finally:
        conn.close()  

def supprimer_module():
    conn = connect_db()
    curs = conn.cursor()
    
    id = int(input("Entrez l'ID du Module à supprimer : "))
    
    if module_existe(id):
        try:

            curs.execute("DELETE FROM Module WHERE id = ?", (id,))
            conn.commit()
            
            if curs.rowcount > 0:
                print(f"Le module avec l'ID {id} a été supprimé avec succès!")
            else:
                print(f"Aucun module trouvé avec l'ID {id}!")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression du module : {e}")
        finally:
            conn.close()
    else:
        print("Le module n'existe pas!")

def modifier_module():
    conn = connect_db()
    curs = conn.cursor()
    
    id = int(input("Entrez l'ID du Module à mettre à jour : "))
    
    if module_existe(id):
        try:
            nouveau_semestre = input("Entrez le nouveau numéro de la semestre (s1/s2/s3/s4) : ")
            
            curs.execute("UPDATE Module SET semestre = ? WHERE id = ?", (nouveau_semestre, id))
            conn.commit()
            
            if curs.rowcount > 0:
                print(f"Le semestre du module avec l'ID {id} a été mis à jour avec succès à {nouveau_semestre}!")
            else:
                print(f"Aucun module trouvé avec l'ID {id}!")
        except sqlite3.Error as e:
            print(f"Erreur lors de la mise à jour du semestre : {e}")
        finally:
            conn.close()
    else:
        print("Le module n'existe pas!")   
        
def lister_module():
    conn = connect_db()
    curs = conn.cursor()
    
    try:
        print("La liste des modules :")
        
    
        curs.execute("SELECT * FROM Module")
        modules = curs.fetchall()
        
      
        if modules:
    
            print(f"{'ID':<10} {'Enseignant ID':<20} {'Matière':<20} {'Semestre':<10}")
            print("-" * 61)
    
     
            for module in modules:
                print(f"{module[0]:<10} {module[1]:<20} {module[2]:<20} {module[3]:<10}")
        else:
            print("Aucun module trouvé dans la base de données!")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'affichage des modules : {e}")
    finally:
        conn.close()
        
class Switch:
    value = None
    def __new__(class_, value):
        class_.value = value
        return value
def case(*args):
    return any((arg == Switch.value) for arg in args)

# Menu pour l'étudiant 

def menu_etudiant():
    while True:

        print("Espace Etudiant : Liste des choix".center(61, "-"))
        print("1: Ajouter un étudiant")
        print("2: Modifier un étudiant")
        print("3: Supprimer un étudiant")
        print("4: Lister l'ensemble des étudiants")
        print("5: Inscrire un étudiant à un module")
        print("6: Modifier la note d'un étudiant")
        print("7: Supprimer une inscription")
        print("8: Lister les inscriptions")
        print("0: Quitter")
        choix = input("Entrer votre choix : ")

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
            print("Choix 5: Inscrire un étudiant à un module")
            inscrire_etudiant()
        elif case("6"):
            print("Choix 6: Modifier la note d'un étudiant")
            modifier_note()
        elif case("7"):
            print("Choix 7: Supprimer une inscription")
            supprimer_inscription()
        elif case("8"):
            print("Choix 8: Lister les inscriptions")
            lister_inscription()
        elif case("0"):
            print("Au revoir!")
            break 
        else:
            print("Choix invalide, veuillez réessayer!")
            
# Menu pour l'enseignant

def menu_enseignant():
    while True:
        
        print("Espace Enseignant : Liste des choix".center(61, "-"))
        print("1: Ajouter un enseignant")
        print("2: Modifier un enseignant")
        print("3: Supprimer un enseignant")
        print("4: Lister l'ensemble des enseignants")
        print("0: Quitter")
        choix = input("Entrer votre choix : ")

        switch = Switch(choix)

        if case("1"):
            print("Choix 1: Ajouter un enseignant")
            ajouter_enseignant() 
        elif case("2"):
            print("Choix 2: Modifier un enseignant")
            modifier_enseignant()
        elif case("3"):
            print("Choix 3: Supprimer un enseignant")
            supprimer_enseignant()
        elif case("4"):
            print("Choix 4: Lister les enseignants")
            lister_enseignant()
        elif case("0"):
            print("Au revoir!")
            break 
        else:
            print("Choix invalide, veuillez réessayer!")

# Menu pour le module

def menu_module():
    while True:
        print("Espace Module : Liste des choix".center(61, "-"))
        print("1: Ajouter un module")
        print("2: Modifier un module")
        print("3: Supprimer un module")
        print("4: Lister les modules")
        print("0: Quitter")
        choix = input("Entrer votre choix : ")

        switch = Switch(choix)

        if case("1"):
            print("Choix 1: Ajouter un module")
            ajouter_module() 
        elif case("2"):
            print("Choix 2: Modifier un module")
            modifier_module()
        elif case("3"):
            print("Choix 3: Supprimer un module")
            supprimer_module()
        elif case("4"):
            print("Choix 4: Lister les modules")
            lister_module()
        elif case("0"):
            print("Au revoir!")
            break 
        else:
            print("Choix invalide, veuillez réessayer!")
            
# Menu principal

def menuPrincipal():
    while True:

        print("Espace Scolarité : Liste des choix".center(61, "-"))
        print("1: Espace étudiant")
        print("2: Espace enseignant")
        print("3: Espace module")
        print("0: Quitter")
        choix = input("Entrer votre choix : ")

        switch = Switch(choix)

        if case("1"):
            print("Choix 1: Espace étudiant")
            menu_etudiant() 
        elif case("2"):
            print("Choix 2: Espace enseignant")
            menu_enseignant()
        elif case("3"):
            print("3: Espace module")
            menu_module()
        elif case("0"):
            print("Au revoir!")
            break 
        else:
            print("Choix invalide, veuillez réessayer!")
            
menuPrincipal()
