def importation():
    fichier = open("user_data.txt", "a")
    fichier.close()
    with open("user_data.txt", "r") as fichier:
        inventaire = [ligne.split(" : ") for ligne in fichier]
    if len(inventaire) == 0:
        running1 = "yes"
        inventaire.append(["bienvenue",running1])
    else: 
        if inventaire[0][0] == "bienvenue": running1 = inventaire[0][1]
        else: running1 = "yes"
    return running1, inventaire

def exportation(inventaire):
    with open("user_data.txt", "w") as fichier:
        for variable in inventaire:
            fichier.write(" : ".join(variable))

