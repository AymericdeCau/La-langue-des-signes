import pygame

pygame.font.init()
font_h1 = pygame.font.SysFont('helvetic', 150)
font_h2 = pygame.font.SysFont('helvetic', 120)
font_h3 = pygame.font.SysFont('helvetic', 90)
font_h4 = pygame.font.SysFont('helvetic', 70)
font_p = pygame.font.SysFont('arrial', 30)

class SimpleButton:

    "La classe SimpleButton permet de créer des boutons rectangulaire de couleur, position, dimension et nom choisis par l'utilisateur lors de sa création" # les doc de la class, print(self.__doc__) pourles lire dans le programme

    # __init__ est une fonction appelé "constructeur" dont le nom est imposé par python, elle se lance lors de la création d'une nouvelle instance de la classe SimpleButton
    def __init__(self, color, x, y, width, height, text='', text_color="black", font=font_h4, border_radius=0, border_width=0, select_color="none"):
        """
        color         : couleur de l'arrière plan du bouton
        x             : abscisse du bouton
        y             : ordonné du bouton
        width         : largeur du bouton
        height        : hauteur du bouton
        text          : texte à afficher sur le bouton (optionnel)
        text_color    : couleur du texte (optionnel)
        font          : police du texte (optionnel)
        border_radius : arrondis les angles de border_radius pixels (optionnel)
        border_width  : permet de ne faire qu'une bande de largeur border_width autour du texte sans arrière plan (valeur=0 -> bouton plein  et valeur>0 -> ligne autour du texte) (optionnel)
        select_color  : permet de choisir la couleur de l'arrière plan quand le bouton est survolé par la sourie (optionnel)
        """
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.font = font
        self.border_radius = border_radius
        self.border_width = border_width
        self.selection = "init"
        # La couleur selct_color par défaut est couleur complémentaire à celle de l'arrière plan
        if select_color == "none": self.select_color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        else: self.select_color = select_color 
        

    def draw(self, screen, color=10, outline=False):  # il faut appeler draw() pour afficher le bouton dans le script
        if color == 10: color = self.color
        if outline:
            pygame.draw.rect(screen, outline, 
                             (self.x-2, self.y-2, self.width+4, self.height+4), width=0, border_radius=self.border_radius)
        pygame.draw.rect(screen, color, 
                         (self.x, self.y, self.width, self.height), self.border_width, border_radius=self.border_radius)
        if self.text != '':
            text = self.font.render(self.text, 1, self.text_color)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self): # méthode permettant de vérifier si le bouton est survolé
        pos = pygame.mouse.get_pos()
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    
    def select(self, screen): # méthode permettant de changer la couleur du bouton et de modifier l'aparence du curseur
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
        self.selection = True
        # Si on ne spécifie pas de couleur, la couleur opossée à celle du bouton est affichée par défaut.
        self.draw(screen, self.select_color)

    def unselect(self, screen):
        self.selection = False
        self.draw(screen)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

# Un exemple sur une fenêtre nommé screen
# a = SimpleButton("red",  screen.get_width() / 2 - 125, screen.get_height() /2 - 50, 250, 100, "NomDuBouton", (50, 100, 255), 20,5)
# a.draw(screen)
# if a.isOver():
#     if a.selection == False:
#         a.select(screen)
# else:
#     if a.selection == True:
#         a.unselect(screen)



class ComplexButton:

    "La classe ComplexButton permet de créer des boutons en forme de polygone de couleur, position, dimension et nom choisis par l'utilisateur lors de sa création"
    # Cette classe est utilisée explicitement dans le menu

    def __init__(self, color, coordinate, border_width=0, select_color="none"): # on initialise un bouton
        """
        color         : couleur de l'arrière plan du bouton
        coordinate    : coordonné des points qui forment le polygone
        border_width  : permet de ne faire qu'une bande de largeur border_width autour du texte sans arrière plan (valeur=0 -> bouton plein  et valeur>0 -> ligne autour du texte) (optionnel)
        select_color  : permet de définir la couleur de l'arrière plan quand le bouton est survolé par la sourie (optionnel)

        """
        self.color = color
        self.coor = coordinate
        self.border_width = border_width
        self.selection = False
        if select_color == "none": self.select_color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        else: self.select_color = select_color
        # print(self.__doc__) # permet d'afficher la documentation écrit juste au-dessus "La classe ComplexButton ..."

    def draw(self, screen, color="rien"):  # il faut appeler draw() pour afficher le bouton dans le script
        if color == "rien": color = self.color
        pygame.draw.polygon(screen, color, self.coor, self.border_width)

    def isOver(self): # méthode permettant de vérifier si le bouton est survolé
        pos = pygame.mouse.get_pos()
        if self.coor[0][1] <= pos[1] <=  self.coor[3][1]:
            if self.coor[0][0] - (pos[1]-self.coor[0][1])*(self.coor[0][0]-self.coor[3][0])/(self.coor[3][1]-self.coor[0][1]) <= pos[0] <= self.coor[1][0] - (pos[1]-self.coor[1][1])*(self.coor[1][0]-self.coor[2][0])/(self.coor[2][1]-self.coor[1][1]):
                return True
        return False
    
    def select(self, screen): # méthode permettant de changer la couleur du bouton et de modifier l'aparence du curseur
        # Si on ne spécifie pas de couleur, la couleur opossée à celle du bouton est affichée par défaut.
        self.draw(screen, self.select_color)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
        self.selection = True

    def unselect(self, screen):
        self.draw(screen)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
        self.selection = False


# importation() permet de récupérer les données d'utilisation de l'utilisateur,
# celle-ci sont stokée dans user_data.txt
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

# exportation() est la fonction associé à importation() qui souvegarde
# les données de l'utilisateur dans le fichier user_data.txt
def exportation(inventaire):
    with open("user_data.txt", "w") as fichier:
        for variable in inventaire:
            fichier.write(" : ".join(variable))
