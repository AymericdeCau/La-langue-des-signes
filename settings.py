# -*- coding: utf-8 -*-
import pygame
from tools import *

pygame.init()

class Settings:
    def __init__(self, screen, fps):
        self.screen = screen
        self.fps=fps
    
    def run(self):
        self.screen.fill(((10, 30, 60)))
        self.home = SimpleButton((0, 210, 250), 20, 20, 200, 50, "Retour au menu", (255, 255, 255), font_p)
        self.home.draw(self.screen)
        text = font_h1.render("Settings", 1, (255,255,255))
        self.screen.blit(text, ((self.screen.get_width()/2 - text.get_width()/2, 150)))
        fps_text = font_h4.render("FPS :      30      60", 1, (0,100,255))
        self.screen.blit(fps_text, ((self.screen.get_width()/2 - fps_text.get_width()/2, 500)))

        self.minfps = SimpleButton((250,250,250), 860, 515, 20, 20, border_radius=100, select_color=(255,255,255))
        self.maxfps = SimpleButton((255,255,255), 990, 515, 20, 20, border_radius=100, select_color=(255,255,255))
        self.tick_button_min = SimpleButton((0,0,0), 863, 518, 14, 14, border_radius=100, select_color=(0,0,0))
        self.tick_button_max = SimpleButton((0,0,0), 993, 518, 14, 14, border_radius=100, select_color=(0,0,0))
        self.liste_bouton = [self.home, self.maxfps, self.minfps]
        self.liste_name_bouton = ["home"]
        return 0

    def refresh(self):
        self.home.draw(self.screen)

    def checked(self):
        if self.tick_button_min in self.liste_bouton:
            self.tick_button_min.draw(self.screen)
        if self.tick_button_max in self.liste_bouton:
            self.tick_button_max.draw(self.screen)
        for b in self.liste_bouton:
            if b.isOver(): # si le bouton est survolé
                if not b.selection : # si le bouton n'est pas encore sélectionner
                    b.select(self.screen) # on change alors la couleur de l'arrière plan
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]: # si la souris est préssé alors que le bouton est survolé comme vu au dessus
                    if b == self.minfps and self.tick_button_min not in self.liste_bouton:
                        
                        self.liste_bouton.append(self.tick_button_min)
                        self.fps = 30
                        if self.tick_button_max in self.liste_bouton:
                            self.liste_bouton.remove(self.tick_button_max)
                            self.maxfps.draw(self.screen)
                    elif b == self.maxfps and self.tick_button_max not in self.liste_bouton:
                        self.liste_bouton.append(self.tick_button_max)
                        self.fps = 60
                        if self.tick_button_min in self.liste_bouton:
                            self.liste_bouton.remove(self.tick_button_min)
                            self.minfps.draw(self.screen)
                    # 0=gauche, 1=milieu, 2=droite
                    elif b == self.home:
                        return self.liste_bouton.index(b), self.fps
            else:
                if b.selection: # si le bouton n'est pas survolé mais que la couleur de l'arrière plan est encore en mode sélection alors
                    b.unselect(self.screen) # on le remet en mode non sélection, c'est à dire que l'on remet l'arrière plan initiale
        return "none", self.fps
