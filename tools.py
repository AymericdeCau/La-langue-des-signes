import pygame

pygame.font.init()
font_h1 = pygame.font.SysFont('helvetic', 150)
font_h2 = pygame.font.SysFont('helvetic', 120)
font_h3 = pygame.font.SysFont('helvetic', 90)
font_h4 = pygame.font.SysFont('helvetic', 70)
font_p = pygame.font.SysFont('arrial', 30)

class SimpleButton:

    "La classe SimpleButton permet de créer des >>> boutons rectangulaire <<< de couleur, position, dimension et nom choisis par l'utilisateur lors de sa création"

    def __init__(self, color, x, y, width, height, text='', text_color="black", border_radius=0, color_width=0):
        # __init__ est une fonction appelé "constructeur" dont le nom est imposé par python, elle se lance lors de la création d'une nouvelle instance de la classe SimpleButton
        # border_radius permet d'arrondir les bords de notre "rectangle"
        # color_width permet de ne faire qu'un trait de largeur color_width autour du texte sans arrière plan (valeur=0 -> bouton plein  et valeur>0 -> ligne autour du texte)
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.border_radius = border_radius
        self.color_width = color_width
        self.selection = False
        # print(self.__doc__) # permet d'afficher la documentation écrit juste au-dessus "La classe SimpleButton ..."

    def draw(self, screen, outline=False):  # il faut appeler draw() pour afficher le bouton dans le script
        if outline:
            pygame.draw.rect(screen, outline, 
                             (self.x-2, self.y-2, self.width+4, self.height+4), width=0, border_radius=self.border_radius)
        pygame.draw.rect(screen, self.color, 
                         (self.x, self.y, self.width, self.height), self.color_width, border_radius=self.border_radius)
        if self.text != '':
            text = font_h4.render(self.text, 1, self.text_color)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self): # méthode permettant de vérifier si le bouton est survolé
        pos = pygame.mouse.get_pos()
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    
    def select(self, screen, color="none"): # méthode permettant de changer la couleur du bouton et de modifier l'aparence du curseur
        # Si on ne spécifie pas de couleur, la couleur opossée à celle du bouton est affichée par défaut.
        if color == "none":
            color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        self.draw(screen, color)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
        self.selection = True

    def unselect(self, screen):
        self.draw(screen)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
        self.selection = False

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

    "La classe ComplexButton permet de créer des >>> boutons en forme de polygone <<< de couleur, position, dimension et nom choisis par l'utilisateur lors de sa création"

    def __init__(self, color, coordonné, largeur=0): # on initialise un bouton
        self.color = color
        self.coor = coordonné
        self.largeur = largeur
        self.selection = False
        # print(self.__doc__) # permet d'afficher la documentation écrit juste au-dessus "La classe ComplexButton ..."

    def draw(self, screen, color="rien"):  # il faut appeler draw() pour afficher le bouton dans le script
        if color == "rien": color = self.color
        pygame.draw.polygon(screen, color, self.coor, self.largeur)

    def isOver(self): # méthode permettant de vérifier si le bouton est survolé
        pos = pygame.mouse.get_pos()
        if self.coor[0][1] <= pos[1] <=  self.coor[3][1]:
            if self.coor[0][0] - (pos[1]-self.coor[0][1])*(self.coor[0][0]-self.coor[3][0])/(self.coor[3][1]-self.coor[0][1]) <= pos[0] <= self.coor[1][0] - (pos[1]-self.coor[1][1])*(self.coor[1][0]-self.coor[2][0])/(self.coor[2][1]-self.coor[1][1]):
                return True
        return False
    
    def select(self, screen, color="none"): # méthode permettant de changer la couleur du bouton et de modifier l'aparence du curseur
        # Si on ne spécifie pas de couleur, la couleur opossée à celle du bouton est affichée par défaut.
        if color == "none":
            color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        self.draw(screen, color)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
        self.selection = True

    def unselect(self, screen):
        self.draw(screen)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
        self.selection = False
