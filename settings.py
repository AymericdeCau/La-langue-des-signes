# -*- coding: utf-8 -*-
import pygame
from tools import *

pygame.init()

class Settings:
    def __init__(self, screen, fps):
        self.screen = screen
        self.fps = fps
        self.tick_button = SimpleButton((255,)*3, 403, 405, 10, 10, border_radius=100)

    
    def run(self):
        self.text = font_h1.render("Settings", 1, (255,255,255))
        self.fps_text = font_p.render("FPS :   30      60", 1, (0,0,0))
        self.screen.fill(((10, 30, 60)))
        self.home = SimpleButton((0, 210, 250), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), font_p)
        self.maxfps = SimpleButton((250,250,250), 400, 400, 20, 20, border_radius=100)
        self.minfps = SimpleButton((255,255,255), 458, 400, 20, 20, border_radius=100)
        
        self.refresh()
        self.liste_bouton = [self.home]
        self.liste_name_bouton = ["home"]
        return 0

    def refresh(self):
        self.screen.blit(self.fps_text, (303, 400))
        self.home.draw(self.screen)
        self.maxfps.draw(self.screen)
        self.minfps.draw(self.screen)
        self.home.draw(self.screen)
        self.screen.blit(self.text, ((self.screen.get_width()//2 - self.text.get_width()//2, 150)))
        self.tick_button.draw(self.screen)
    def checked(self):
        for b in self.liste_bouton:
            if b.isOver(): # si le bouton est survolé
                if not b.selection : # si le bouton n'est pas encore sélectionner
                    b.select(self.screen) # on change alors la couleur de l'arrière plan
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]: # si la souris est préssé alors que le bouton est survolé comme vu au dessus
                    # 0=gauche, 1=milieu, 2=droite
                    if b == self.maxfps:
                        self.tick_button = SimpleButton((0,)*3, 405, 405, 10, 10, border_radius=100)
                        self.fps = 30
                    if b == self.minfps:
                        self.tick_button = SimpleButton((0,)*3, 463, 405, 10, 10, border_radius=100)
                        self.fps = 60
                    return self.liste_bouton.index(b)
            else:
                if b.selection: # si le bouton n'est pas survolé mais que la couleur de l'arrière plan est encore en mode sélection alors
                    b.unselect(self.screen) # on le remet en mode non sélection, c'est à dire que l'on remet l'arrière plan initiale
        self.refresh()
        return "none", self.fps

# Ce document est sous licence Creative Commons CC BY-SA
