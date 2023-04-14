import pygame
from tools import SimpleButton
import time
pygame.init()

clock = pygame.time.Clock()
clock.tick(60)


class Course:
    """
    La partie course fonctionne par l’initialisation des variables.
    Enfin, la 
    """
    def __init__(self,screen):
        self.screen = screen

        #initialise tous les font /!\ MAUVAIS
        self.font_h1 = pygame.font.SysFont('helvetic', 150)
        self.font_h2 = pygame.font.SysFont('helvetic', 120)
        self.font_h3 = pygame.font.SysFont('helvetic', 90)
        self.font_h4 = pygame.font.SysFont("helvetic", 70)
        self.font_p = pygame.font.SysFont('arrial', 30)

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
        self.return_button_text = self.font_p.render("RETOUR",1,(50,)*3)
        self.return_button = SimpleButton((0,100,150), 1550-8, 850-8, self.return_button_text.get_width()+16, self.return_button_text.get_height()+16, border_radius=5)

    def run_sub_lesson(self, index):
        """
        La méthode run() permet de donner le sommaire des leçons et si l’on clique sur l’un des titres on est redirigé vers run_sub_lesson().
        Elle permet aussi de renvoyer vers le menu avec les touches escape, espace ou en cliquant sur le boutton RETOUR
        """
        #affiche les boutons
        next_button_text = self.font_h3.render("page suivante", 1,(50,)*3)
        previous_button_text = self.font_h3.render("ancienne page", 1, (50,)*3)

        next_button = SimpleButton((0,0,150), 50, 600, next_button_text.get_width(), next_button_text.get_height())
        previous_button = SimpleButton((0,0,150), 200, 600, previous_button_text.get_width(), previous_button_text.get_height())
        #affiche le cours
        printing_lesson = pygame.image.load(self.list_course_picture[index]).convert()
        title_of_the_lesson = self.font_h3.render(self.list_course[index],1,(255,0,0))
        running_sub_lesson = True

        while running_sub_lesson == True:
            self.return_button = SimpleButton((0,100,150), 1550-8, 850-8, self.return_button_text.get_width()+16, self.return_button_text.get_height()+16, border_radius=5)
            self.screen.blit(self.background_course,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_sub_lesson == False
                    #exportation(inventaire)
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                        running_sub_lesson = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button==1:
                    if index != len(self.list_course_picture)-1:
                        index += 1
                        printing_lesson = pygame.image.load(self.list_course_picture[index]).convert()
                        title_of_the_lesson = self.font_h3.render(self.list_course[index],1,(255,0,0))
                    else:
                        running_sub_lesson = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button==3:
                    if index != 0:
                        index -=1
                        printing_lesson = pygame.image.load(self.list_course_picture[index]).convert()
                        title_of_the_lesson = self.font_h3.render(self.list_course[index],1,(255,0,0))
                    else:
                        running_sub_lesson = False
            if self.return_button.isOver():
                self.return_button = SimpleButton((0,100,250), 1550-8, 850-8, self.return_button_text.get_width()+16, self.return_button_text.get_height()+16, border_radius=5)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    running_sub_lesson = False

    

            self.return_button.draw(self.screen)
            self.screen.blit(self.return_button_text,(1550,850))
            self.screen.blit(title_of_the_lesson,(150,200))
            self.screen.blit(printing_lesson,(600,0))
            pygame.display.flip()  # on rafraichie la page régulièrement

    def run(self, running_course=False):
        title_part = self.font_h1.render("Cours", 1, (255,255,255))
        while running_course:
            self.return_button = SimpleButton((0,100,150), 1550-8, 850-8, self.return_button_text.get_width()+16, self.return_button_text.get_height()+16, border_radius=5)
            self.screen.blit(self.background_course,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exportation(inventaire)
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                        running_course = False
                        # jsp koii  méètrreeuuu

            
            if self.return_button.isOver():
                self.return_button = SimpleButton((0,100,250), 1550-8, 850-8, self.return_button_text.get_width()+16, self.return_button_text.get_height()+16, border_radius=5)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    running_course = False
            
            # affiche et charge les bouttons avec le texte
            for i in range(len(self.list_course)):
                title_of_the_lesson = self.font_h3.render(self.list_course[i],1,(255,0,0))
                cours_affichage = SimpleButton((0,255,0), 750, 300 + i*75, title_of_the_lesson.get_width(), title_of_the_lesson.get_height())
                if cours_affichage.isOver():
                    cours_affichage = SimpleButton((0,155,0), 750, 300 + i*75, title_of_the_lesson.get_width(), title_of_the_lesson.get_height())
                    if event.type == pygame.MOUSEBUTTONUP and event.button==1:
                        self.run_sub_lesson(i)
                        time.sleep(0.4)
                
                cours_affichage.draw(self.screen)
                self.screen.blit(title_of_the_lesson,(750, 300 + i*75))
            
            self.return_button.draw(self.screen)
            self.screen.blit(self.return_button_text,(1550,850))
            self.screen.blit(title_part, (750, 120))
            pygame.display.flip()  # on rafraichie la page régulièrement
