class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return value
def case(*args):
    return any((arg == switch.value) for arg in args)


while True:

    print("Liste des choix".center(10, "#"))
    print("1: choix 1")
    print("2: choix 2")
    print("3: ")
    print("4: ")
    print("5: ")
    print("0: Quitter")
    choix = input("Entrer votre choix: ")

    while switch(choix):
        if case("1"):
            print("choix 1")
            break
        if case("2"):
            print("choix 2")
            break
        if case("3"):
            print("choix 3")
            break
        elif switch.case("0"):
            print("Au revoir!")
            break
    else:
        print("Choix invalide, veuillez réessayer!")



