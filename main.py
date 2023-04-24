# -*- coding: utf-8 -*-
import pygame
from tools import *
from function import *
from home import Home
from course import Course
from practice import Practice
from settings import Settings
from hand_detector import HandDetector

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


    for event in pygame.event.get(): # pour pouvoir sortir quand on est dans aucune des pages
        if event.type == pygame.QUIT:
            running = False ; pygame.quit()


    # chacune des boucles while situé ici représente une page de l'application
    # ainsi cette première boucle représente la page d'accueil home sur laquelle est le menu
    while running_home:
        if reload == 2: # initialisation de la page quand l'utilisateur l'ouvre
            menu = Home(screen) # on crée notre menu
            reload = menu.run() # on le lance
        
        index_of_next_page = menu.checked() # on vérifie si l'utilisateur clique sur un des boutons
        if index_of_next_page != False: # si un des boutons est cliqué
            running_home = False # on ferme la page du menu
            reload = 2 # on met reload en mode initialisation pour l'initiatlisation de la prochaine page
            globals()["running_" + liste_name_page[index_of_next_page]] = True # on lance la page qui a été cliqué

        pygame.display.flip()  # on rafraichit la page à chaque tour de boucle
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running, running_home = False, False ; pygame.quit() # l'utilisateur peut fermer la page quand il le souhaite


    while running_practice:
        if reload == 2: # initialisation de la page quand l'utilisateur l'ouvre
            practice = Practice(screen) # on crée notre menu
            reload = practice.run() # on le lance

        index_of_next_page = practice.checked() # on vérifie si l'utilisateur clique sur un des boutons menant à une autre page
        if index_of_next_page != "none": # si un des boutons est cliqués
            running_practice = False # on ferme la page du menu
            reload = 2 # on met reload en mode initialisation pour l'initiatlisation de la prochaine page
            globals()["running_" + liste_name_page[index_of_next_page]] = True # on lance la page qui a été cliquée

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running, running_practice = False, False ; pygame.quit()


    #while running_video:
    #    if reload == 2: # initialisation de la page quand l'utilisateur l'ouvre
    #        video = Settings(screen) # on crée notre menu
    #        reload = video.run() # on le lance
    #
    #    index_of_next_page = video.checked() # on vérifie si l'utilisateur clique sur un des boutons
    #    if index_of_next_page != "none": # si un des boutons est cliqués
    #        running_video = False # on ferme la page du menu
    #        reload = 2 # on met reload en mode initialisation pour l'initiatlisation de la prochaine page
    #        globals()["running_" + liste_name_page[index_of_next_page]] = True # on lance la page qui a été cliquée
    #
    #    pygame.display.flip()
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT: running, running_video = False, False ; pygame.quit()


    while running_settings:
        if reload == 2: # initialisation de la page quand l'utilisateur l'ouvre
            settings = Settings(screen) # on crée notre menu
            reload = settings.run() # on le lance

        index_of_next_page = settings.checked() # on vérifie si l'utilisateur clique sur un des boutons
        if index_of_next_page != "none": # si un des boutons est cliqués
            running_settings = False # on ferme la page du menu
            reload = 2 # on met reload en mode initialisation pour l'initiatlisation de la prochaine page
            globals()["running_" + liste_name_page[index_of_next_page]] = True # on lance la page qui a été cliquée

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running, running_settings = False, False ; pygame.quit()

    while running_course: # initialisation de la page quand l'utilisateur l'ouvre
        if reload == 2:
            course = Course(screen)
            reload = course.run(True,False)
        running_course = False
        reload = 2
        running_home = True
    while running_video:
        if reload == 2:
            HDetector = HandDetector()
            reload = HDetector.run(True)
        running_video = False
        reload = 2
        running_home = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running, running_video = False, False ; pygame.quit()

