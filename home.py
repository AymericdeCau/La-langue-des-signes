# -*- coding: utf-8 -*-
import pygame
from tools import *

pygame.init()

class Home:

    def __init__(self, screen):
        self.screen = screen
        nut = pygame.image.load("./assets/picturesforhome/nut.png")
        self.nut = pygame.transform.scale(nut, (150, 150)) # l'écrou pour settings

    def run(self):
        self.screen.fill(((10, 30, 60)))
        # toutes les valeurs du menu sont calculés en fonction de ces variables pour facilité le changement de valeurs
        m_h = self.screen.get_height() / 6 * 5 # hauteur du menu
        m_L = self.screen.get_width() / 6 * 5 # longeur du menu
        m_x = self.screen.get_width() / 2 - m_L / 2 # abscisse du menu
        m_y = self.screen.get_height() / 2 - m_h / 2 # ordonné du menu
        m_i = 30 # espace entre les éléments du menu
        
        # Les cinq boutons du menu sont définis ici, ComplexButton est une class (voir tools.py) facilitant la création et manipulation de ces boutons
        # home est donc une instance de la class ComplexButton
        self.home = ComplexButton((0, 210, 250), [(m_x, m_y), (m_x + m_L, m_y), (m_x + m_L, m_y + m_h/20*8), (m_x, m_y + m_h/20*8)])
        # print(home.__doc__) # <<< pour lire les informations relatives à la classe ComplexButton vous pouvez décommenté l'instruction à gauche de ce texte <<<
        self.practice = ComplexButton((140, 255, 0), [(m_x , m_y + m_h/20*8 + m_i), (m_x + m_L/5*2, m_y + m_h/20*8 + m_i), (m_x + m_L/5, m_y + m_h), (m_x, m_y + m_h)])
        self.course = ComplexButton((250, 150, 0), [(m_x + m_L/5*2 + m_i, m_y + m_h/20*8 + m_i), (m_x + m_L, m_y + m_h/20*8 + m_i), (m_x + m_L, m_y + m_h/20*8 + m_i + m_h/20*6  - m_i/2), (m_x + m_L/10*3 + m_i, m_y + m_h/20*8 + m_i + m_h/20*6 - m_i/2)])
        self.video = ComplexButton((200, 0, 100), [(m_x + m_L/10*3 + m_i - m_i*(m_L/5)/(m_h/20*12-m_i), m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L/10*3 + m_i - m_i*m_L/5/m_h/20*8 + m_L/10*5, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L/10 + m_i + m_L/5*3, m_y + m_h), (m_x + m_L/5 + m_i, m_y + m_h)])
        self.settings = ComplexButton((100, 100, 100), [(m_x + m_L/10*3 + 2*m_i - m_i*m_L/5/m_h/20*8 + m_L/10*5 + m_i / 2, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L, m_y + m_h), (m_x + m_L/10 + 2*m_i + m_L/5*3 + m_i / 2, m_y + m_h)])
        
        self.liste_bouton = [self.home, self.practice, self.course, self.video, self.settings]
        self.liste_name_bouton = ["home", "practice", "course", "video", "settings"]

        for b in self.liste_bouton:
            # globals() permet de transformer les éléments de la liste liste_bouton de type str en variable
            b.draw(self.screen) # draw est une méthode définie dans la class bouton qui permet d'afficher les boutons sur la page
            
        self.refresh()
        return 0

    def refresh(self):
            text = font_h1.render("La Langue Muette", 1, (255,255,255))
            self.screen.blit(text, ((self.home.coor[0][0] + self.home.coor[1][0])/2 - text.get_width()/2, (self.home.coor[1][1] + self.home.coor[2][1])/2 - text.get_height()/2))
            text = font_h2.render("Exercice", 1, (255,255,255))
            self.screen.blit(text, ((self.practice.coor[0][0] + (self.practice.coor[1][0] + self.practice.coor[2][0])/2)/2 - text.get_width()/2, (self.practice.coor[1][1] + self.practice.coor[2][1])/2 - text.get_height()))
            text = font_h2.render("Cours", 1, (255,255,255))
            self.screen.blit(text, (((self.course.coor[0][0] + self.course.coor[3][0])/2 + (self.course.coor[1][0] + self.course.coor[2][0])/2)/2 - text.get_width()/2, (self.course.coor[1][1] + self.course.coor[2][1])/2 - text.get_height()/2))
            text = font_h2.render("Vidéo", 1, (255,255,255))
            self.screen.blit(text, (((self.video.coor[0][0] + self.video.coor[3][0])/2 + (self.video.coor[1][0] + self.video.coor[2][0])/2)/2 - text.get_width()/2, (self.video.coor[1][1] + self.video.coor[2][1])/2 - text.get_height()/2))
            self.screen.blit(self.nut, ((self.settings.coor[0][0] + self.settings.coor[1][0])/2 - self.nut.get_width()/2, (self.settings.coor[1][1] + self.settings.coor[2][1])/2 - self.nut.get_height()/2))
    
    def checked(self):
        for b in self.liste_bouton: # on vérifie pour chaque bouton du menu
            if b.isOver(): # si le bouton est survolé
                if b.selection == False : # si le bouton n'est pas encore sélectionner
                    b.select(self.screen) # on change alors la couleur de l'arrière plan
                    if b == self.settings: self.nut = pygame.transform.rotate(self.nut, 90) # et si le bouton en question est settings on fait tourner l'écrou
                    self.refresh()
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]: # si la souris est préssé alors que le bouton est survolé comme vu au dessus
                    # 0=gauche, 1=milieu, 2=droite
                    return self.liste_bouton.index(b)
            else:
                if b.selection == True : # si le bouton n'est pas survolé mais que la couleur de l'arrière plan est encore en mode sélection alors
                    b.unselect(self.screen) # on le remet en mode non sélection, c'est à dire que l'on remet l'arrière plan initiale
                    self.refresh()
                    if b == "settings": self.nut = pygame.transform.rotate(self.nut, 90) # si le bouton en question est le bouton settings on le fait tourner
        return False
