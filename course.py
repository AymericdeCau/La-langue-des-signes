# importation des bibliothèques nécessaires
import pygame
from tools import SimpleButton
import time


class Course:
    def __init__(self,screen):
        self.screen = screen

        #initialise tous les font
        self.font_h1 = pygame.font.SysFont('helvetic', 150)
        #self.font_h2 = pygame.font.SysFont('helvetic', 120)
        self.font_h3 = pygame.font.SysFont('helvetic', 90)
        self.font_h4 = pygame.font.SysFont("helvetic", 70)
        self.font_p = pygame.font.SysFont('arrial', 30)

        # charge le background
        self.background_course = pygame.image.load("./assets/picturesforcourse/background.png").convert()
        self.list_course = ["Action","Alimentation","base et lieux","Famille","Santé","Sentiments","Temps","Vie en Société"]
        self.list_course_picture = [
            "./assets/picturesforcourse/Action.jpg",
            "./assets/picturesforcourse/Alimentation et Divers.jpg",
            "./assets/picturesforcourse/BaseetLieux.jpg",
            "./assets/picturesforcourse/Famille.jpg",
            "./assets/picturesforcourse/Santé.jpg",
            "./assets/picturesforcourse/Sentiments.jpg",
            "./assets/picturesforcourse/Temps.jpg",
            "./assets/picturesforcourse/VieenSociété.jpg"
            ] # (857, 1212) coordonnées pour toutes les images and 471 to have the picture in  the middle
        self.home = SimpleButton((0, 210, 250), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), self.font_p)
        self.return_button = SimpleButton((0,100,150), 1550-8, 850-8,  86, 30, "Retour",(50,)*3, self.font_p,border_radius=5)
        self.next = False 

    def run_sub_lesson(self, index):
        """
        La méthode run() permet de donner le sommaire des leçons et si l’on clique sur l’un des titres on est redirigé vers run_sub_lesson().
        Elle permet aussi de renvoyer vers le menu avec les touches escape, espace ou en cliquant sur le boutton RETOUR
        """

        #charge l’affichage de la leçon
        printing_lesson = pygame.image.load(self.list_course_picture[index]).convert()
        printing_lesson = pygame.transform.scale(printing_lesson, (printing_lesson.get_width()*2/3, printing_lesson.get_height()*2/3))

        title_of_the_lesson = self.font_h3.render(self.list_course[index],1,(255,0,0))
        running_sub_lesson = True
        once_next, once_pre = True, True # variable
        while running_sub_lesson == True:
            #self.screen.blit(self.background_course,(0,0))
            self.screen.fill(((10, 30, 60)))
            #charge les boutons
            previous_page_button = SimpleButton((0,125,255), 650, 350,50, 50," < ", (255,)*3,self.font_p, border_radius=20)
            next_page_button = SimpleButton((0,125,255), 1440, 350, 50, 50, " > ", (255,)*3, self.font_p, border_radius=20)
            self.return_button = SimpleButton((0,100,150), 1600-8, 870-8,  86, 30, "Retour",(50,)*3, self.font_p,border_radius=5)
            self.home = SimpleButton((0, 210, 250), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), self.font_p)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_sub_lesson == False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running_sub_lesson = False
            
            for i in range(len(self.list_course)): # affiche et crée le sommaire 
                title_of_the_lesson_i = self.font_h4.render(self.list_course[i], 1, (10, 30, 60))
                cours_affichage = SimpleButton((255,)*3, 150, 300 + i*65, title_of_the_lesson_i.get_width(), title_of_the_lesson_i.get_height())
                if cours_affichage.isOver():
                    cours_affichage = SimpleButton((250,250,00), 150, 300 + i*65, title_of_the_lesson_i.get_width(), title_of_the_lesson_i.get_height())
                    pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                    if pressed[0]:
                        index = i
                if i==index:
                    cours_affichage = SimpleButton((180,)*3, 150, 300 + i*65, title_of_the_lesson_i.get_width(), title_of_the_lesson_i.get_height())
                cours_affichage.draw(self.screen)
                self.screen.blit(title_of_the_lesson_i,(150, 300 + i*65))

            if previous_page_button.isOver():
                previous_page_button = SimpleButton((0,100,200), 650, 350,50, 50," < ", (255,)*3,self.font_p, border_radius=20)
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]:
                    if index != 0 and once_pre:
                        index -=1
                        once_pre = False
                else:
                    once_pre = True
            
            if next_page_button.isOver():
                next_page_button = SimpleButton((0,100,200), 1440, 350, 50, 50, " > ", (255,)*3, self.font_p, border_radius=20)
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]:
                    if index < len(self.list_course_picture) - 1 and once_next:
                        index += 1
                        once_next = False
                else:
                    once_next = True
            
            if self.return_button.isOver():
                self.return_button = SimpleButton((150,0,100), 1600-8, 870-8,  86, 30, "Retour",(50,)*3, self.font_p, border_radius=5)
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]:
                    running_sub_lesson = False

            if self.home.isOver():
                self.home = SimpleButton((210, 250, 0), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), self.font_p)
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]:
                    running_sub_lesson = False

            printing_lesson = pygame.image.load(self.list_course_picture[index]).convert()
            printing_lesson = pygame.transform.scale(printing_lesson, (printing_lesson.get_width()*8/10, printing_lesson.get_height()*8/10))
            title_of_the_lesson = self.font_h3.render(self.list_course[index],1,(255,0,0))

            self.screen.blit(title_of_the_lesson,(150,200))
            self.screen.blit(printing_lesson,(710,-12))
            previous_page_button.draw(self.screen)
            next_page_button.draw(self.screen)
            self.home.draw(self.screen)
            self.return_button.draw(self.screen)

            pygame.display.flip()  # on rafraichie la page régulièrement

    def run(self, running_course=False):
        title_part = self.font_h1.render("Cours", 1, (255,255,255))
        while running_course:
            self.home = SimpleButton((0, 210, 250), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), self.font_p)
            self.screen.fill(((10, 30, 60)))
            #self.screen.blit(self.background_course,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running_course = False
            

            if self.home.isOver(): # demande si l’on est sur le bouton home 
                self.home = SimpleButton((210, 250, 0), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), self.font_p) # change la couleur du bouton home
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]:
                    running_course = False # fait arrêter la boucle
                
            
            for i in range(len(self.list_course)): # affiche et crée le sommaire 
                title_of_the_lesson = self.font_h3.render(self.list_course[i],1,(10, 30, 60))
                cours_affichage = SimpleButton((255,)*3, 900 - title_of_the_lesson.get_width()//2, 270 + i*75, title_of_the_lesson.get_width(), title_of_the_lesson.get_height())
                if cours_affichage.isOver():
                    cours_affichage = SimpleButton((180,)*3, 900 - title_of_the_lesson.get_width()//2, 270 + i*75, title_of_the_lesson.get_width(), title_of_the_lesson.get_height())
                    pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                    if pressed[0] :
                        self.run_sub_lesson(i)
                    elif not pressed[0]:
                        self.next = True

                
                cours_affichage.draw(self.screen)
                self.screen.blit(title_of_the_lesson,(900 - title_of_the_lesson.get_width()//2, 270 + i*75))
            self.home.draw(self.screen)
            self.screen.blit(title_part, (750, 120))
            pygame.display.flip()  # on rafraichie la page régulièrement

