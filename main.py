# -*- coding: utf-8 -*-
import pygame
from tools import SimpleButton, ComplexButton
from function import *
from home import Home
from course import Course

pygame.init()

clock = pygame.time.Clock()
clock.tick(60)

pygame.display.set_caption("Le language des signes")
pygame.display.set_icon(pygame.image.load("./assets/picturesforhome/logo.png"))
screen = pygame.display.set_mode((1800, 900))

screen_width = screen.get_width()
screen_height = screen.get_height()
reload = 2 # 0=nul, 1=rafraichissement, 2=initialisation

running = True
running_home = bool(importation()[0]) # importation est une fonction définie dans function.py permettant de 
inventaire = importation()[1]
running_practice = False
running_course = False
running_video = False
running_settings = False
liste_name_page = ["home", "practice", "course", "video", "settings"]


while running: # boucle while principle qui permet à la fenêtre de rester ouverte comme sur toute fenêtre pygame
    # chacune des boucles while situé ici représente une page de l'application

    # ainsi cette première boucle représente la page d'accueil home sur laquelle est le menu
    while running_home:
        if reload == 2: # initialisation de la page quand l'utilisateur l'ouvre
            menu = Home(screen) # on crée notre menu
            menu.run() # on le lance
        
        index_of_next_page = menu.checked() # on vérifie si l'utilisateur clique sur un des boutons
        if index_of_next_page != False: # si un des boutons est cliqué
            running_home = False # on ferme la page du menu
            reload = 2 # on met reload en mode initialisation pour l'initiatlisation de la prochaine page
            globals()["running_" + liste_name_page[index_of_next_page]] = True # on lance la page qui a été cliqué

        pygame.display.flip()  # on rafraichit la page à chaque tour de boucle
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running, running_home = False, False ; pygame.quit() # l'utilisateur peut fermer la page quand il le souhaite
    
        while running_course:
            course = Course(screen)
            course.run(True)