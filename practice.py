# -*- coding: utf-8 -*-
import pygame
from tools import *
from random import randint, choice

pygame.init()

class Practice:
    def __init__(self, screen, inventory):
        self.screen = screen
        self.score_qcm = inventory[0]
        self.best_score_game = inventory[1]
        self.page = "choose type"
        self.page_list = ["choose type", "qcm page", "game page"]
        self.pictures_location = [
            ("./assets/picturesforcourse/Action.jpg", 97, 235), ("./assets/picturesforcourse/Action.jpg", 365, 236),
            ("./assets/picturesforcourse/Action.jpg", 633, 227), ("./assets/picturesforcourse/Action.jpg", 890, 217), 
            ("./assets/picturesforcourse/AlimentationetDivers.jpg", 94, 225), ("./assets/picturesforcourse/AlimentationetDivers.jpg", 349, 231), 
            ("./assets/picturesforcourse/AlimentationetDivers.jpg", 612, 226), ("./assets/picturesforcourse/AlimentationetDivers.jpg", 902, 215),
            ("./assets/picturesforcourse/BaseetLieux.jpg", 85, 230), ("./assets/picturesforcourse/BaseetLieux.jpg", 345, 226),
            ("./assets/picturesforcourse/BaseetLieux.jpg", 633, 225), ("./assets/picturesforcourse/BaseetLieux.jpg", 887, 225),
            ("./assets/picturesforcourse/Famille.jpg", 63, 227), ("./assets/picturesforcourse/Famille.jpg", 354, 224),
            ("./assets/picturesforcourse/Famille.jpg", 607, 229), ("./assets/picturesforcourse/Famille.jpg", 868, 213),
            ("./assets/picturesforcourse/Santé.jpg", 64, 230), ("./assets/picturesforcourse/Santé.jpg", 323, 230),
            ("./assets/picturesforcourse/Santé.jpg", 617, 240), ("./assets/picturesforcourse/Santé.jpg", 888, 223),
            ("./assets/picturesforcourse/Sentiments.jpg", 65, 226), ("./assets/picturesforcourse/Sentiments.jpg", 322, 232),
            ("./assets/picturesforcourse/Sentiments.jpg", 583, 240), ("./assets/picturesforcourse/Sentiments.jpg", 855, 230),
            ("./assets/picturesforcourse/Temps.jpg", 58, 219), ("./assets/picturesforcourse/Temps.jpg", 340, 232),
            ("./assets/picturesforcourse/Temps.jpg", 602, 221), ("./assets/picturesforcourse/Temps.jpg", 855, 220),
            ("./assets/picturesforcourse/VieenSociété.jpg", 69, 234), ("./assets/picturesforcourse/VieenSociété.jpg", 333, 238),
            ("./assets/picturesforcourse/VieenSociété.jpg", 604, 190)
            ]
        
        self.sign_list = [
            ["Marcher", 0, 0], ["S'asseoir (assis)", 0, 1], ["Se lever", 0, 2], ["S'allonger", 0, 3], ["Se reposer", 1, 0],
            ["Se réveiller", 1, 1], ["Dormir", 1, 2], ["Sortir", 1, 3], ["Vouloir", 2, 0], ["Pouvoir", 2, 1],
            ["Demander", 2, 2], ["Attendre", 2, 3], ["Téléphoner", 3, 0], ["Envoyer", 3, 1], ["Recevoir", 3, 2],
            ["Eau", 4, 0], ["Café", 4, 1], ["Thé / infusion", 4, 2], ["Sucre", 4, 3], ["Lait", 5, 0],
            ["Chocolat", 5, 1], ["Pain", 5, 2], ["Sel", 5, 3], ["Avoir faim", 6, 0], ["Avoir soif", 6, 1],
            ["Alcool", 7, 0], ["Cigarette", 7, 1], ["Téléphone portable", 7, 2], ["SMS", 7, 3], ["Bonjour", 8, 0],
            ["Au revoir", 8, 1], ["Merci", 8, 2], ["S'il vous plaît", 8, 3], ["Oui", 9, 0], ["Non", 9, 1],
            ["Bien", 9, 2], ["Mauvais", 9, 3], ["Hôpital psychiatrique", 10, 0], ["Chambre", 10, 1], ["Bureau", 10, 2],
            ["Dehors", 10, 3], ["Salle d'attente", 11, 0], ["Salle à manger", 11, 1], ["Maison", 11, 2],
            ["E-mail", 12, 0], ["Epoux / Epouse", 13, 0], ["Enfant", 13, 2], ["Parents", 13, 3],
            ["Père", 14, 0], ["Mère", 14, 1], ["Frère", 14, 2], ["Sœur", 14, 3], ["Ami", 15, 0],
            ["Famille", 15, 1], ["Garçon", 15, 2], ["Fille", 15, 3], ["Docteur", 16, 0], ["Infirmier", 16, 1],
            ["Aide-soignant", 16, 2], ["Patient", 16, 3], ["Interprète", 17, 0], ["Intermédiateur", 17, 1], ["Ça va", 18, 0],
            ["En forme", 18, 1], ["Être fatigué", 18, 2], ["Maladie / être malade", 18, 3], ["Content", 19, 0],
            ["Pas content", 19, 1], ["Mal", 19, 2], ["Douleur", 19, 3], ["Anxiété / Soucis", 20, 0], ["Tristesse", 20, 1],
            ["Colère", 20, 2], ["Enervé", 20, 3], ["Calme", 21, 0], ["Problème", 21, 1], ["Comportement", 21, 2],
            ["Rendez-vous", 21, 3], ["Médicament", 22, 0], ["Piqûre", 22, 1], ["Allergie", 22, 2], ["Tension artérielle", 22, 3],
            ["Thermomètre", 23, 0], ["Urgences / Urgent", 24, 0], ["Accueil", 24, 1], ["Quand", 25, 0], ["Journée", 25, 1],
            ["Matin", 25, 2], ["Midi", 25, 3], ["Après-midi", 26, 0], ["soir", 26, 1], ["Jour", 26, 2], ["Nuit", 26, 3],
            ["Hier", 27, 0], ["Aujourd'hui / Maintenant", 27, 1], ["Demain", 27, 2]
            ]   
        self.list_choice = []
        self.level = []
        self.next_qcm = ""
        self.next_game = ""
    
    def run(self):
        self.screen.fill(((10, 30, 60)))
        self.list_choice = []
        if self.page == "choose type":
            self.home = SimpleButton((0, 210, 250), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), font_p)
            self.qcm = SimpleButton((250, 150, 0), self.screen.get_width()/5-20, 200, self.screen.get_width()/5+40, self.screen.get_width()/5, "Questionnaire", (255, 255, 255), font_h4, 50)
            self.jeux = SimpleButton((200, 0, 100), 3*self.screen.get_width()/5-20, 200, self.screen.get_width()/5+40, self.screen.get_width()/5, "Jeux", (255, 255, 255), font_h4, 50, select_color=(255, 210, 50))
            text = font_p.render("Nombre de bonne réponse au QCM : " + str(self.score_qcm), 1, (255,255,255))
            self.screen.blit(text, ((50, 800)))
            text = font_p.render("Meilleur score au jeu : " + str(self.best_score_game), 1, (255,255,255))
            self.screen.blit(text, ((1700 - text.get_width(), 800)))
            
            self.list_bouton = [self.home, self.qcm, self.jeux]
            self.list_bouton_nav = [self.home]
        if self.page == "qcm page":
            self.back = SimpleButton((0, 210, 250), 20, 20, 100, 50, "Retour", (255, 255, 255), font_p)
            
            temp_sign_list = self.sign_list       
            
            index_solution = randint(0, len(temp_sign_list)-1)
            text = font_h3.render("Quel est le signe pour : " + temp_sign_list[index_solution][0], 1, (255,255,255))
            self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, self.screen.get_height()/2 - text.get_height()/2 -250)))
            solution = temp_sign_list[index_solution]
            
            self.list_option = []
            temp_sign_list.pop(index_solution)
            for i in range(3):
                index_option = randint(0, len(temp_sign_list)-1)
                self.list_option.append(temp_sign_list[index_option])
                temp_sign_list.pop(index_option)

            self.solution_place = randint(0, 3)
            self.list_option.insert(self.solution_place, solution)

            self.sol_1 = SimpleButton((0, 0, 255), (self.screen.get_width()-820)/5 - 10, self.screen.get_height()/2 -10, 225, 259, border_radius=10)
            self.sol_2 = SimpleButton((255, 0, 0), (self.screen.get_width()-820)/5*2 + 205 - 10, self.screen.get_height()/2 -10, 225, 259, border_radius=10)
            self.sol_3 = SimpleButton((0, 255, 0), (self.screen.get_width()-820)/5*3 + 205*2 - 10, self.screen.get_height()/2 -10, 225, 259, border_radius=10)
            self.sol_4 = SimpleButton((255, 255, 20), (self.screen.get_width()-820)/5*4 + 205*3 - 10, self.screen.get_height()/2 -10, 225, 259, border_radius=10)

            self.list_bouton = [self.back, self.sol_1, self.sol_2, self.sol_3, self.sol_4]
            self.list_choice = [self.sol_1, self.sol_2, self.sol_3, self.sol_4]
            self.list_bouton_nav = []

        if self.page == "good answer":
            self.score_qcm += 1
            export((self.score_qcm, self.best_score_game))
            self.back = SimpleButton((0, 210, 250), 20, 20, 100, 50, "Retour", (255, 255, 255), font_p)
            self.next_qcm = SimpleButton((0, 210, 250), self.screen.get_width()/2 - 50, 400, 100, 50, "Suivant", (255, 255, 255), font_p)
            text = font_h3.render("Bravo vous avez trouvé la bonne réponse !", 1, (255,255,255))
            self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, self.screen.get_height()/2 - text.get_height()/2 -250)))
            self.list_bouton = [self.back, self.next_qcm]
            self.list_bouton_nav = []

        if self.page == "bad answer":
            self.back = SimpleButton((0, 210, 250), 20, 20, 100, 50, "Retour", (255, 255, 255), font_p)
            self.next_qcm = SimpleButton((0, 210, 250), self.screen.get_width()/2 - 50, 400, 100, 50, "Suivant", (255, 255, 255), font_p)
            self.course = SimpleButton((0, 210, 250),  self.screen.get_width()/2 - 125, 500, 250, 50, "Aller à la partie cours", (255, 255, 255), font_p)
            text = font_h4.render(f"Dommage, vous n'avez pas trouvé la bonne réponse (signe n°{self.solution_place+1})", 1, (255,255,255))
            self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, self.screen.get_height()/2 - text.get_height()/2 -250)))
            self.list_bouton = [self.back, self.next_qcm, self.course]
            self.list_bouton_nav = [0, 0, self.course]
        
        if self.page == "game page":
            self.back = SimpleButton((0, 210, 250), 20, 20, 100, 50, "Retour", (255, 255, 255), font_p)
            self.level_1 = SimpleButton((240, 220, 0),  self.screen.get_width()/7, 560, self.screen.get_width()/5, 100, "Facile", (255, 255, 255), font_h4)
            self.level_2 = SimpleButton((220, 100, 0),  self.screen.get_width()/7 * 3, 560, self.screen.get_width()/5, 100, "Moyen", (255, 255, 255), font_h4)
            self.level_3 = SimpleButton((170, 0, 0),  self.screen.get_width()/7 * 5, 560, self.screen.get_width()/5, 100, "Difficile", (255, 255, 255), font_h4)
            text = font_h4.render("Choisisez le niveau de difficulté : ", 1, (255,255,255))
            self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, 400)))
            self.screen.blit(pygame.image.load("./assets/picturesforgame/touche_A.png"), (90, 383))
            text = font_h4.render("Le but du jeu est d'éviter les blocs et les images.", 1, (255,255,255))
            self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, 100)))
            text = font_h4.render("Cliquez sur la signification des signes qui apparaissent pour les détruire.", 1, (255,255,255))
            self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, 180)))
            self.list_bouton = [self.back, self.level_1, self.level_2, self.level_3]
            self.level = [self.level_1, self.level_2, self.level_3]
            self.list_bouton_nav = []

        if self.page == "game":
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
            pygame.draw.rect(self.screen, (100, 200, 255), ((0, 0), (1800,900)))
            pygame.draw.rect(self.screen, (255, 255, 255), ((0,200), (1800, 10)))
            pygame.draw.rect(self.screen, (255, 255, 255), ((0,700), (1800,10)))
            text = font_h4.render("Utilisez la touche A pour monter ou descendre.", 1, (255,255,255))
            self.screen.blit(text, ((20, 750)))
            text = font_h4.render("Cliquez sur la signification d'un signe pour détruire le bloc du signe.", 1, (255,255,255))
            self.screen.blit(text, ((20, 830)))

            figure = [pygame.image.load("./assets/picturesforgame/fig_1.png"), pygame.image.load("./assets/picturesforgame/fig_2.png"), pygame.image.load("./assets/picturesforgame/fig_3.png"), pygame.image.load("./assets/picturesforgame/fig_4.png"), pygame.image.load("./assets/picturesforgame/fig_5.png")]
            mvt = 0

            clicked_a = False
            clicked_mousse = False
            temp_sign_list = []
            temp_sign_list = [x for x in self.sign_list]
            visible_sign_list = []
            for i in range(35):
                random_sign = randint(0, len(temp_sign_list) - 1)
                visible_sign_list.append(temp_sign_list[random_sign])
                temp_sign_list.pop(random_sign)
            
            difficulty = 550 if self.level[0] == 0 else 500 if self.level[0] == 1 else 450
            self.score = 0

            block_color = (50, 50, 100)

            block = 10
            block_list = []
            block_speed = 1

            nb_boss = 0
            boss_advance = 0
            boss_list = []

            level_dificulty = -2500 if self.level[0] == 0 else -1500 if self.level[0] == 1 else 0
            boss_speed = 5 if self.level[0] == 0 else 3 if self.level[0] == 1 else 1

            figure_x, figure_y, figure_drct = 0, 380, -1
            game = True
            

                        
            while game == True:
                user_test = False
                self.score += 1

                if self.score//100 > self.best_score_game: self.best_score_game = self.score//100

                text = font_h4.render("Score : " + str(self.score//100), 1, (255,255,255))
                pygame.draw.rect(self.screen, (100, 200, 255), ((1400, 740), (text.get_width() + 10, text.get_height())))
                self.screen.blit(text, ((1400, 740)))

                pygame.display.flip()
                if figure_drct == 1 and figure_y > 0: figure_y -= 1
                if figure_drct == -1 and figure_y < 380: figure_y += 1

                pygame.draw.rect(self.screen, (100, 200, 255), ((0, 210), (1800, 490)))
                if figure_drct == 1: self.screen.blit(pygame.transform.rotate( figure[mvt], 180), ((figure_x + 100, figure_y + 210), (50, 50)))
                if figure_drct == -1: self.screen.blit(figure[mvt], ((figure_x + 100, figure_y + 210), (50, 50)))

                if mvt < 4: mvt += 1
                else: mvt = 0


                for i in range(5):
                    for j in range(7):
                        pygame.draw.rect(self.screen, (60, 80, 110), ((j * 1800/7 + 2, i * 35 + 2), (1800/7 - 4, 31)))
                        text = font_p.render(visible_sign_list[7 * i + j][0], 1, (255, 255, 255))
                        self.screen.blit(text, ((j * 1800/7 + 2 + 1772/14 - text.get_width()/2, i * 35 + 8), (1800/7 - 4, 31)))
                
                pos = pygame.mouse.get_pos()
                if 2 < pos[0] < 1798 and 2 < pos[1] < 173:
                    i = ((pos[1]) -2 )// 35
                    j = ((pos[0]) -2 )// int(1800/7)
                    pygame.draw.rect(self.screen, (110, 80, 60), ((j * 1800/7 + 2, i * 35 + 2), (1800/7 - 4, 31)))
                    text = font_p.render(visible_sign_list[7 * i + j][0], 1, (255, 255, 255))
                    self.screen.blit(text, ((j * 1800/7 + 2 + 1772/14 - text.get_width()/2, i * 35 + 8), (1800/7 - 4, 31)))
                    user_test = visible_sign_list[7 * i + j]

                block += 1
                if block > difficulty:
                    unit_x = randint(30, 200)
                    unit_y = randint(30, 300)
                    if choice([-1, 1]) == -1:
                        unit_d = 210
                    else: unit_d = 700 - unit_y
                    block_list.append([unit_x, unit_y, unit_d, 1796])
                    block = 0
                
                if self.score//5000 >= nb_boss:
                    block = level_dificulty
                    name = choice(visible_sign_list)
                    boss_y = 210 + randint(0, 221)
                    boss_list.append([name, 1796, boss_y, pygame.image.load(self.pictures_location[name[1]][0])])
                    boss_advance = boss_speed
                    nb_boss += 1


                for unit in block_list:
                    unit[3] -= block_speed
                    pygame.draw.rect(self.screen, block_color, ((unit[3], unit[2]), (unit[0], unit[1])))
                    if unit[3] < figure_x + 80 + figure[mvt].get_width() and figure_x + 150 <= unit[3] + unit[0] and figure_y + 215 <= unit[2] + unit[1] and figure_y + 200  + figure[mvt].get_height() >= unit[2]:
                        game = False
                        self.page = "game over"
                    if unit[3] + unit[0] < 0:
                        block_list.remove(unit)

                boss_advance += 1
                for boss in boss_list:
                    if boss_advance >= boss_speed: boss[1] -= 1
                    pygame.draw.rect(self.screen, block_color, ((boss[1], boss[2]), (213, self.pictures_location[boss[0][1]][2] + 10)))
                    self.screen.blit(boss[3], (boss[1] + 5, boss[2] + 5), (21 + boss[0][2] * 205, self.pictures_location[boss[0][1]][1], 203, self.pictures_location[boss[0][1]][2]))
                    if boss[1] < figure_x + 80 + figure[mvt].get_width() and figure_x + 150 <= boss[1] + 203 and figure_y + 215 <= boss[2] + self.pictures_location[boss[0][1]][2] and figure_y + 200  + figure[mvt].get_height() >= boss[2]:
                        game = False
                        self.page = "game over"
                    if boss[1] + 213 < 0: boss_list.remove(boss)
                if boss_advance >= boss_speed: boss_advance = 0
                    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a and clicked_a == False:
                            clicked_a = True
                            if figure_drct == 1: figure_drct = -1  # and figure_y < 30  Pour ne pas pouvoir changé de sens que lorsque l'on est très proche des lignes
                            elif figure_drct == -1 : figure_drct = 1  # and figure_y > 350
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a and clicked_a == True:
                            clicked_a = False
                    if event.type == pygame.MOUSEBUTTONDOWN and clicked_mousse == False and user_test != False:
                        clicked_mousse = True
                        for boss in boss_list:
                            if user_test == boss[0]:
                                boss_list.remove(boss)
                    if event.type == pygame.MOUSEBUTTONUP and clicked_mousse == True: clicked_mousse = False
                    if event.type == pygame.QUIT:
                        export((self.score_qcm, self.best_score_game))
                        pygame.quit()


            self.list_bouton = []
            self.list_bouton_nav = []
            self.list_choice = []




        if self.page == "game over":
            self.screen.fill(((10, 30, 60)))
            self.back = SimpleButton((0, 210, 250), 20, 20, 100, 50, "Retour", (255, 255, 255), font_p)
            self.next_game = SimpleButton((0, 210, 250), self.screen.get_width()/2 - 100, 400, 200, 50, "Recommencer", (255, 255, 255), font_p)
            self.course = SimpleButton((0, 210, 250),  self.screen.get_width()/2 - 125, 500, 250, 50, "Aller à la partie cours", (255, 255, 255), font_p)
            text = font_h1.render("Game Over", 1, (255,255,255))
            self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, self.screen.get_height()/2 - text.get_height()/2 -250)))
            self.list_bouton = [self.back, self.next_game, self.course]
            text = font_h4.render("Score : " + str(self.score//100), 1, (255,255,255))
            self.screen.blit(text, ((1300, 800)))
            self.list_bouton_nav = [0, 0, self.course]
                



        self.next = False
        self.refresh()
        return 0
    
    def refresh(self):
        for button in self.list_bouton:
            button.draw(self.screen)
        for choice in range (len(self.list_choice)):
            self.screen.blit(pygame.image.load(self.pictures_location[self.list_option[choice][1]][0]), (self.list_choice[choice].x + 10, self.list_choice[choice].y + 10), (21 + (self.list_option[choice][2]%4) * 205, self.pictures_location[self.list_option[choice][1]][1], 204, self.pictures_location[self.list_option[choice][1]][2]))

    def checked(self):
        for b in self.list_bouton:
            if b.isOver(): # si le bouton est survolé
                if b.selection != True : # si le bouton n'est pas encore sélectionner
                    b.select(self.screen) # on change alors la couleur de l'arrière plan
                    if b in self.list_choice:
                        choice = self.list_choice.index(b)
                        self.screen.blit(pygame.image.load(self.pictures_location[self.list_option[choice][1]][0]), (b.x + 10, b.y + 10), (21 + (self.list_option[choice][2]%4) * 205, self.pictures_location[self.list_option[choice][1]][1], 204, self.pictures_location[self.list_option[choice][1]][2]))
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0] and self.next == True:
                    self.next = False
                    if b == self.next_game:
                        self.page = "game page"
                        b.selection = "init"
                        self.run()
                    elif b == self.next_qcm:
                        self.page = "qcm page"
                        b.selection = "init"
                        self.run()
                    elif b in self.level:
                        self.level = [self.level.index(b)]
                        self.page = "game"
                        self.run()
                    elif b in self.list_bouton_nav:
                        b.unselect(self.screen)
                        return self.list_bouton.index(b), (self.score_qcm, self.best_score_game)
                    elif b in self.list_choice:
                        if self.list_choice.index(b) == self.solution_place:
                            self.page = "good answer"
                            self.run()
                        else:
                            self.page = "bad answer"
                            self.run()
                    elif b not in (self.list_bouton_nav and self.list_choice):
                        self.page = self.page_list[self.list_bouton.index(b)]
                        b.selection = "init"
                        export((self.score_qcm, self.best_score_game))
                        self.run()
                if not pressed[0]: self.next = True
                break
            else:
                if b.selection != False: # si le bouton n'est pas survolé mais que la couleur de l'arrière plan est encore en mode sélection alors
                    b.unselect(self.screen) # on le remet en mode non sélection, c'est à dire que l'on remet l'arrière plan initiale
                    if b in self.list_choice:
                        choice = self.list_choice.index(b)
                        self.screen.blit(pygame.image.load(self.pictures_location[self.list_option[choice][1]][0]), (b.x + 10, b.y + 10), (21 + (self.list_option[choice][2]%4) * 205, self.pictures_location[self.list_option[choice][1]][1], 204, self.pictures_location[self.list_option[choice][1]][2]))
        return "none", (self.score_qcm, self.best_score_game)
