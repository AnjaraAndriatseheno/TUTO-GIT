todo_list =["Arroser les plantes", "Sortir le singe", "Aller à la pharmacie", "Finir le projet GIT"]

def print_list(todo_list) : 
    print("Voici ce qu'il reste à faire dans votre liste")
    i = 0
    while i < len(todo_list) : 
        print(todo_list[i])
        print("")
        i += 1


def new_todo(todo_list):
    print("Souhaitez vous ajouter un nouvelle tâche à votre liste?")
    choice = input()
    if choice == "oui" :
        print("Veuillez entrer votre nouvelle tâche")
        new_todo = input()
        todo_list.append(new_todo)
    else : 
        print("Okay bonne journée")


    




# Fonction pour modifier le statut d'un todo - à réaliser
def modifier_statut_todo():
    print('Fonctionnalité "modifier le statut d\'un todo" à venir')

# Fonction pour supprimer un todo - à réaliser
def supprimer_todo():
    print('Fonctionnalité "supprimer un todo" à venir')

# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Changer le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: quitter')
    print('========================')

    # Actions suivant le choix
    choix = input('=> Choix : ')
    match choix:
        case '1':
            lister_todos()
        case '2':
            creer_todo()
        case '3':
            modifier_statut_todo()
        case '4':
            supprimer_todo()
        case 'q':
            print('Au revoir')
        case _:
            print('Choix invalide')