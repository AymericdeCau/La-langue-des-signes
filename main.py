# -*- coding: utf-8 -*-
import pygame
from tools import *
from function import *
from home import Home
from course import Course
from practice import Practice
from settings import Settings
from hand_detector import SignDetector

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

    while running_settings:
        import requests

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
    onclick = True
    while running_video:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running, running_video = False, False ; pygame.quit()
        if reload == 2:
            screen.fill(((10, 30, 60)))
            title = font_h1.render("Détecteur de signe",1,(255, 0, 0))
            explanations1 = font_p.render("Ce programme est conçu pour détecter l'alphabet FSL à partir de la vidéo de votre webcam. Nous souhaitons",1,(255,)*3)
            explanations2 = font_p.render("vous informer que ce programme ne collecte ni n'envoie aucune donnée de votre webcam.Nous vous recommandons de ",1,(255,)*3)
            explanations3 = font_p.render("mettre votre main devant la caméra avant de lancer le programme afin de garantir le bon lancement du programme.",1,(255,)*3)
            explanations4 = font_p.render("Nous espérons que cela vous permettra de profiter pleinement de notre programme en toute sécurité. Merci",1,(255,)*3)
            accepter = SimpleButton((255,155,0), 800, 700, 250, 130,"Accepter",(255,)*3,font_h4)
            if accepter.isOver() :
                accepter = SimpleButton((255,0,255), 800, 700, 250, 130,"Accepter",(255,)*3,font_h4)
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0] and not onclick:
                    retour = font_p.render("Cliquez sur Échap sur cette page pour sortir",1, (255, 255, 255))
                    printing_alphabet_lesson = pygame.image.load("./assets/picturesforcourse/alphabetFSL.png").convert()
                    screen.blit(retour, (900 - retour.get_width()//2, 15))
                    screen.blit(printing_alphabet_lesson,(900 - printing_alphabet_lesson.get_width()//2, 450 - printing_alphabet_lesson.get_height()//2 + 30)) # affiche au centre l’image
                    pygame.display.flip()  # on rafraichie la page 

                    SDetector = SignDetector(screen)
                    reload = SDetector.run(True)
                    while reload == False:
                        running_video = False
            pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
            if not pressed[0]:
                onclick = False
            screen.blit(title,(900 - title.get_width()//2, 60))
            screen.blit(explanations1,(900 - explanations1.get_width()//2,220))
            screen.blit(explanations2,(900 - explanations2.get_width()//2,300))
            screen.blit(explanations3,(900 - explanations3.get_width()//2,380))
            screen.blit(explanations4,(900 - explanations4.get_width()//2,460))
            accepter.draw(screen)

            
            
            pygame.display.flip()  # on rafraichie la page 

        
        reload = 2
        running_home = True

