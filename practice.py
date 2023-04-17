# -*- coding: utf-8 -*-
import pygame
from tools import *

pygame.init()

class Practice:
    def __init__(self, screen):
        self.screen = screen
        self.page = "choose type"
    
    def run(self):
        self.screen.fill(((10, 30, 60)))
        if self.page == "choose type":
            self.home = SimpleButton((0, 210, 250), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), font_p)
            self.qcm = SimpleButton((250, 150, 0), self.screen.get_width()/5-20, 200, self.screen.get_width()/5+40, self.screen.get_width()/5, "Questionnaire", (255, 255, 255), font_h4, 50)
            self.jeux = SimpleButton((200, 0, 100), 3*self.screen.get_width()/5-20, 200, self.screen.get_width()/5+40, self.screen.get_width()/5, "Jeux", (255, 255, 255), font_h4, 50, select_color=(255, 210, 50))
            self.liste_bouton = [self.home, self.qcm, self.jeux]
            self.liste_bouton_nav = [self.home]
            self.refresh()
        return 0
    
    def refresh(self):
        self.home.draw(self.screen)
        self.qcm.draw(self.screen)
        self.jeux.draw(self.screen)

    def checked(self):
        for b in self.liste_bouton:
            if b.isOver(): # si le bouton est survolé
                if not b.selection : # si le bouton n'est pas encore sélectionner
                    b.select(self.screen) # on change alors la couleur de l'arrière plan
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]: # si la souris est préssé alors que le bouton est survolé comme vu au dessus
                    # 0=gauche, 1=milieu, 2=droite
                    if b in self.liste_bouton_nav: return self.liste_bouton.index(b)
            else:
                if b.selection: # si le bouton n'est pas survolé mais que la couleur de l'arrière plan est encore en mode sélection alors
                    b.unselect(self.screen) # on le remet en mode non sélection, c'est à dire que l'on remet l'arrière plan initiale
        return "none"
