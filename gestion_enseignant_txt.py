
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return value
def case(*args):
    return any((arg == switch.value) for arg in args)

def ajouter_enseignant():
    id = input("Entrez l'id de l'enseignant: ")
    nom = input("Entrez le nom de l'enseignant: ")
    prenom = input("Entrez le prénom de l'enseignant: ")
    cin = input("Entrez le cin de l'enseignant: ")
    dept = input("Entrez le departement de l'enseignant: ")

    data = f"{id},{nom},{prenom},{cin},{dept}\n"

    with open("data/Enseignant.txt", "a", encoding="utf-8") as f:
        f.write(data)

    print("Enseignant ajouté avec succès!")



def lister_enseignant():
    with open("data/Enseignant.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        print("_" * 70)
        print("|    ID    |    Nom    |    Prenom    |    CIN    |    Departement    |")
        print("_" * 70)
        for line in lines:
            line = line.strip()
            line = line.split(',')
            print(f"|    {line[0]}    |  {line[1]}   |   {line[2]}    |   {line[3]}    |   {line[4]}   |")
            print("_" * 70)





def menu_enseignant():
    while True:
        print("Liste des choix".center(10, "#"))
        print("1: Ajouter un nouveau enseignant")
        print("2: Afficher la liste des enseignants")
        print("0: Quitter")
        c1 = input("Entrer votre choix: ")
        while switch(c1):
            if case("0"):
                print("Au revoir")
                break
            elif case("2"):
                lister_enseignant()
                break
            elif case("1"):
                ajouter_enseignant()
                break
            else:
                print("Invalide choix")
                break
        if c1 == "0":
            break

menu_enseignant()