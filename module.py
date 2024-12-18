import sqlite3

class Switch:
    value = None
    def __new__(class_, value):
        class_.value = value
        return value

def case(*args):
    return any((arg == Switch.value) for arg in args)

def connect_db():
    return sqlite3.connect("C:/Users/hp/Desktop/Data/Gestion_Scolarite (1).db")


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
        id_ens = int(input("Entrez l'id' d'enseignant : "))
        matiere = input("Entrez le nom de la matiere : ")
        semester = input("Entrez le numero de semestre : ")
        
        donnees_Module = (id_ens, matiere, semester)
        
        curs.execute("INSERT INTO Module(Enseignant_id, matiere, semestre) VALUES (?, ?, ?)", donnees_Module)

        conn.commit()
        print("Module ajouté avec succès!")
    except Exception as e:
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

gestion_module()
