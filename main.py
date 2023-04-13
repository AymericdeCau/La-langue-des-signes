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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False ; pygame.quit()

    while running_practice:
        screen.blit(pygame.image.load("assets/2.jpg"), (0, 0))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exportation(inventaire)
                pygame.quit()
    
    c = Course()

    # cours_santé = font_h2
    # cours_action
    # cours_alimentation
    # cours_base_et_lieu
    # cours_famille
    # cours_santé
    # cours_
    title_course = font_h1.render("Cours", 1, (255,255,255))
    cours_alphabet = font_h2.render("alphabet",1,(255,0,0))
    list_course = ["Action","Alimentation","base et lieux","Famille","Santé","Sentiments","Temps","Vie en Société"]
    list_course_picture = ["La-langue-des-signes-main\assets\picturesforcourse\Action.jpg",
    ".\assets\picturesforcourse\Alimentation et Divers.jpg",
    ".\assets\picturesforcourse\BaseetLieux.jpg",
    ".\assets\picturesforcourse\Famille.jpg",
    ".\assets\picturesforcourse\Santé.jpg",
    ".\assets\picturesforcourse\Sentiments.jpg",
    ".\assets\picturesforcourse\Temps.jpg",
    ".\assets\picturesforcourse\Vie en Société.jpg"]

    background_course = pygame.image.load(r".\assets\picturesforcourse\background.png").convert()
    while running_course:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exportation(inventaire)
                pygame.quit()
        screen.blit(background_course,(0,0))
        
        # affiche et charge les bouttons avec le texte
        for i in range(len(list_course)):
            title_of_the_lesson = font_h3.render(list_course[i],1,(255,0,0))
            cours_affichage = SimpleButton((0,255,0), 750, 300 + i*75, title_of_the_lesson.get_width(), title_of_the_lesson.get_height())
            if cours_affichage.isOver():
                cours_affichage = SimpleButton((0,155,0), 750, 300 + i*75, title_of_the_lesson.get_width(), title_of_the_lesson.get_height())
            cours_affichage.draw(screen)
            screen.blit(title_of_the_lesson,(750, 300 + i*75))
        
        screen.blit(title_course, (750, 120))
        pygame.display.flip()  # on rafraichie la page régulièrement
