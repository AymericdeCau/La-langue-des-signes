import pygame
pygame.font.init()
font = pygame.font.SysFont('helvetic', 70)

class button():
    def __init__(self, color, x, y, width, height, text='', text_color="black", border_radius=0):  # on initialise un bouton
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.border_radius = border_radius
        self.text_color = text_color

    def draw(self, screen, outline=True):  # il faut appeler draw() pour afficher le bouton dans le script
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4,
                             self.height+4), width=0, border_radius=self.border_radius)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width,
                         self.height), width=0, border_radius=self.border_radius)

        if self.text != '':
            text = font.render(self.text, 1, self.text_color)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                        self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self):  # on vérifie si le bouton est survolé
        pos = pygame.mouse.get_pos()
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False




class bouton():
    def __init__(self, color, coordonné, largeur=0):  # on initialise un bouton
        self.color = color
        self.coor = coordonné
        self.largeur = largeur
        self.selection = False

    def draw(self, screen, color="rien"):  # il faut appeler draw() pour afficher le bouton dans le script
        if color == "rien": color = self.color
        pygame.draw.polygon(screen, color, self.coor, self.largeur)

    def isAu(self):  # on vérifie si le bouton est survolé
        pos = pygame.mouse.get_pos()
        if self.coor[0][1] <= pos[1] <=  self.coor[3][1]:
            if self.coor[0][0] - (pos[1]-self.coor[0][1])*(self.coor[0][0]-self.coor[3][0])/(self.coor[3][1]-self.coor[0][1]) <= pos[0] <= self.coor[1][0] - (pos[1]-self.coor[1][1])*(self.coor[1][0]-self.coor[2][0])/(self.coor[2][1]-self.coor[1][1]):
                return True
        return False
    
    def select(self, screen, color="rien"): # Si on ne spécifie pas de couleur, la couleur opossée à celle du bouton est affichée par défaut.
        if color == "rien": color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        self.draw(screen, color)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
        self.selection = True
    def unselect(self, screen):
        self.draw(screen)
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
        self.selection = False