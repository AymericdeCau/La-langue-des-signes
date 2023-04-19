# -*- coding: utf-8 -*-
import pygame
from tools import *
from random import randint

pygame.init()

class Practice:
    def __init__(self, screen):
        self.screen = screen
        self.page = "choose type"
        self.page_list = ["choose type", "qcm page", "jeux page"]
        self.pictures_location = ["./assets/picturesforcourse/Action.jpg"]
        self.list_choice = []
        self.next_qcm = ""
    
    def run(self):
        self.screen.fill(((10, 30, 60)))
        self.list_choice = []
        if self.page == "choose type":
            self.home = SimpleButton((0, 210, 250), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), font_p)
            self.qcm = SimpleButton((250, 150, 0), self.screen.get_width()/5-20, 200, self.screen.get_width()/5+40, self.screen.get_width()/5, "Questionnaire", (255, 255, 255), font_h4, 50)
            self.jeux = SimpleButton((200, 0, 100), 3*self.screen.get_width()/5-20, 200, self.screen.get_width()/5+40, self.screen.get_width()/5, "Jeux", (255, 255, 255), font_h4, 50, select_color=(255, 210, 50))
            self.list_bouton = [self.home, self.qcm, self.jeux]
            self.list_bouton_nav = [self.home]
        if self.page == "qcm page":
            self.back = SimpleButton((0, 210, 250), 20, 20, 100, 50, "Retour", (255, 255, 255), font_p)
            
            sign_list = [["Marcher", 0, 0], ["S'asseoir (assis)", 0, 1], ["Se lever", 0, 2], ["S'allonger", 0, 3], ["Se reposer", 0, 4], ["Se réveiller", 0, 5]]         
            
            index_solution = randint(0, len(sign_list)-1)
            text = font_h3.render("Quel est le signe pour : " + sign_list[index_solution][0], 1, (255,255,255))
            self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, self.screen.get_height()/2 - text.get_height()/2 -250)))
            solution = sign_list[index_solution]
            
            self.list_option = []
            sign_list.pop(index_solution)
            for i in range(3):
                index_option = randint(0, len(sign_list)-1)
                self.list_option.append(sign_list[index_option])
                sign_list.pop(index_option)
            self.solution_place = randint(0, 3)
            self.list_option.insert(self.solution_place, solution)
            self.sol_1 = SimpleButton((0, 0, 255), (self.screen.get_width()-820)/5 - 10, self.screen.get_height()/2 -10, 225, 259, border_radius=10)
            self.sol_2 = SimpleButton((255, 0, 0), (self.screen.get_width()-820)/5*2 + 205 - 10, self.screen.get_height()/2 -10, 225, 259, border_radius=10)
            self.sol_3 = SimpleButton((0, 255, 0), (self.screen.get_width()-820)/5*3 + 205*2 - 10, self.screen.get_height()/2 -10, 225, 259, border_radius=10)
            self.sol_4 = SimpleButton((255, 255, 20), (self.screen.get_width()-820)/5*4 + 205*3 - 10, self.screen.get_height()/2 -10, 225, 259, border_radius=10)
            print(solution, self.solution_place, self.list_option)
            self.list_bouton = [self.back, self.sol_1, self.sol_2, self.sol_3, self.sol_4]
            self.list_choice = [self.sol_1, self.sol_2, self.sol_3, self.sol_4]
            self.list_bouton_nav = []
        if self.page == "good answer":
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
        self.next = False
        self.refresh()
        return 0
    
    def refresh(self):
        for button in self.list_bouton:
            button.draw(self.screen)
        for choice in range (len(self.list_choice)):
            self.screen.blit(pygame.image.load(self.pictures_location[self.list_option[choice][1]]), (self.list_choice[choice].x + 10, self.list_choice[choice].y + 10), (21 + (self.list_option[choice][2]%4) * 205, 96 + (self.list_option[choice][2]//4) * 290, 204, 239))

    def checked(self):
        for b in self.list_bouton:
            if b.isOver(): # si le bouton est survolé
                if b.selection != True : # si le bouton n'est pas encore sélectionner
                    b.select(self.screen) # on change alors la couleur de l'arrière plan
                    if b in self.list_choice:
                        choice = self.list_choice[self.list_choice.index(b)]
                        self.screen.blit(pygame.image.load(self.pictures_location[self.list_option[self.list_choice.index(choice)][1]]), (choice.x + 10, choice.y + 10), (21 + (self.list_option[self.list_choice.index(choice)][2]%4) * 205, 96 + (self.list_option[self.list_choice.index(choice)][2]//4) * 270, 204, 239))
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0] and self.next == True:
                    self.next = False
                    if b == self.next_qcm:
                        self.page = "qcm page"
                        b.selection = "init"
                        self.run()
                    elif b in self.list_bouton_nav:
                        b.unselect(self.screen)
                        return self.list_bouton.index(b)
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
                        self.run()
                if not pressed[0]: self.next = True
                break
            else:
                if b.selection != False: # si le bouton n'est pas survolé mais que la couleur de l'arrière plan est encore en mode sélection alors
                    b.unselect(self.screen) # on le remet en mode non sélection, c'est à dire que l'on remet l'arrière plan initiale
                    if b in self.list_choice:
                        choice = self.list_choice[self.list_choice.index(b)]
                        self.screen.blit(pygame.image.load(self.pictures_location[self.list_option[self.list_choice.index(choice)][1]]), (choice.x + 10, choice.y + 10), (21 + (self.list_option[self.list_choice.index(choice)][2]%4) * 205, 96 + (self.list_option[self.list_choice.index(choice)][2]//4) * 270, 204, 239))
        return "none"
