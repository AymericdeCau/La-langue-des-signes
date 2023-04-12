# -*- coding: utf-8 -*-
import pygame
from tools import bouton, button
from function import *
from course import Course
pygame.init()

pygame.font.init()

clock = pygame.time.Clock()
clock.tick(10)

font_h1 = pygame.font.SysFont('helvetic', 150)
font_h2 = pygame.font.SysFont('helvetic', 120)
font_h3 = pygame.font.SysFont('helvetic', 90)
font_p = pygame.font.SysFont('arrial', 30)

pygame.display.set_caption("Le language des signes")
screen = pygame.display.set_mode((1800, 900))

screen_width = screen.get_width()
screen_height = screen.get_height()
reload = 2 # 0=nul, 1=rafraichissement, 2=initialisation

running = True
running_home = bool(importation()[0])
inventaire = importation()[1]
running_practice = False
running_course = False
running_video = False
running_settings = False

nut = pygame.image.load("La-langue-des-signes-main/assets/picturesforhome/nut.png").convert_alpha()
nut = pygame.transform.scale(nut, (150, 150)) # l'écrou pour settings


while running: # boucle while principle qui permet à la fenêtre de rester ouverte comme sur toute fenêtre pygame
    # chacune des boucles while situé ici représente une page de l'application
    # ainsi cette première boucle représente la page d'accueil home sur laquelle est le menu
    while running_home == True:

        if reload == 2 or screen_width != screen.get_width() or screen_height != screen.get_height():
            # initialisation de la page quand l'utilisateur ouvre l'application ou quand il modifie la taille de la fenêtre

            screen.fill(((10, 30, 60)))
            # toutes les valeurs du menu sont calculés en fonction de ces variables pour facilité le changement de valeurs
            m_h = screen.get_height() / 6 * 5 # hauteur du menu
            m_L = screen.get_width() / 6 * 5 # longeur du menu
            m_x = screen.get_width() / 2 - m_L / 2 # abscisse du menu
            m_y = screen.get_height() / 2 - m_h / 2 # ordonné du menu
            m_i = 30 # espace entre les éléments du menu
            
            # Les cinq boutons du menu sont définis ici, bouton est une class (voir tools.py) facilitant la création et manipulation de ces boutons
            home = bouton((0, 210, 250), [(m_x, m_y), (m_x + m_L, m_y), (m_x + m_L, m_y + m_h/20*8), (m_x, m_y + m_h/20*8)])
            practice = bouton((140, 255, 0), [(m_x , m_y + m_h/20*8 + m_i), (m_x + m_L/5*2, m_y + m_h/20*8 + m_i), (m_x + m_L/5, m_y + m_h), (m_x, m_y + m_h)])
            course = bouton((250, 150, 0), [(m_x + m_L/5*2 + m_i, m_y + m_h/20*8 + m_i), (m_x + m_L, m_y + m_h/20*8 + m_i), (m_x + m_L, m_y + m_h/20*8 + m_i + m_h/20*6  - m_i/2), (m_x + m_L/10*3 + m_i, m_y + m_h/20*8 + m_i + m_h/20*6 - m_i/2)])
            video = bouton((200, 0, 100), [(m_x + m_L/10*3 + m_i - m_i*(m_L/5)/(m_h/20*12-m_i), m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L/10*3 + m_i - m_i*m_L/5/m_h/20*8 + m_L/10*5, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L/10 + m_i + m_L/5*3, m_y + m_h), (m_x + m_L/5 + m_i, m_y + m_h)])
            settings = bouton((100, 100, 100), [(m_x + m_L/10*3 + 2*m_i - m_i*m_L/5/m_h/20*8 + m_L/10*5 + m_i / 2, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L, m_y + m_h), (m_x + m_L/10 + 2*m_i + m_L/5*3 + m_i / 2, m_y + m_h)])
            
            liste_bouton = ["home", "practice", "course", "video", "settings"]

            for b in liste_bouton:
                # globals() permet de transformer les éléments de la liste liste_bouton de type str en variable
                globals()[b].draw(screen) # draw est un attribut définie dans la class bouton et permet d'afficher les boutons sur la page
            reload = 1

        if reload == 1: # rafraichissement "mineur" de la page home : de tous les textes susceptible d'être survolé puis recouvert par le changement de couleur de fond du bouton
            text = font_h1.render("La Langue Muette", 1, (255,255,255))
            screen.blit(text, ((home.coor[0][0] + home.coor[1][0])/2 - text.get_width()/2, (home.coor[1][1] + home.coor[2][1])/2 - text.get_height()/2))
            text = font_h2.render("Exercice", 1, (255,255,255))
            screen.blit(text, ((practice.coor[0][0] + (practice.coor[1][0] + practice.coor[2][0])/2)/2 - text.get_width()/2, (practice.coor[1][1] + practice.coor[2][1])/2 - text.get_height()))
            text = font_h2.render("Cours", 1, (255,255,255))
            screen.blit(text, (((course.coor[0][0] + course.coor[3][0])/2 + (course.coor[1][0] + course.coor[2][0])/2)/2 - text.get_width()/2, (course.coor[1][1] + course.coor[2][1])/2 - text.get_height()/2))
            text = font_h2.render("Vidéo", 1, (255,255,255))
            screen.blit(text, (((video.coor[0][0] + video.coor[3][0])/2 + (video.coor[1][0] + video.coor[2][0])/2)/2 - text.get_width()/2, (video.coor[1][1] + video.coor[2][1])/2 - text.get_height()/2))
            screen.blit(nut, ((settings.coor[0][0] + settings.coor[1][0])/2 - nut.get_width()/2, (settings.coor[1][1] + settings.coor[2][1])/2 - nut.get_height()/2))
            reload = 0


        for b in liste_bouton: # on vérifie pour chaque bouton du menu
            if globals()[b].isAu(): # si le bouton est survolé
                if globals()[b].selection == False : # si le bouton n'est pas encore sélectionner
                    globals()[b].select(screen) # on change alors la couleur de l'arrière plan
                    if b == "settings": nut = pygame.transform.rotate(nut, 90) # et si le bouton en question est settings on fait tourner l'écrou
                    reload = 1 # enfin on rafraichit les textes parceque le changement de couleur se fait par dessus
                    
                pressed = pygame.mouse.get_pressed() # on récupère les cliques de la souris
                if pressed[0]: # si la souris est préssé alors que le bouton est survolé comme vu au dessus
                    # 0=gauche, 1=milieu, 2=droite
                    running_home = False # on arrête la boucle actuel
                    globals()["running_" + b] = True # et on lance la boucle while souhaité
                    reload = 2 # on met le reload en mode initialisation
            else:
                if globals()[b].selection == True : # si le bouton n'est pas survolé mais que la couleur de l'arrière plan est encore en mode sélection alors
                    globals()[b].unselect(screen) # on le remet en mode non sélection, c'est à dire que l'on remet l'arrière plan initiale
                    if b == "settings": nut = pygame.transform.rotate(nut, 90) # si le bouton en question est le bouton settings on le fait tourner
                    reload = 1 # enfin on rafraichit les textes parceque le changement de couleur se fait par dessus


        pygame.display.flip()  # on rafraichit la page à chaque tour de boucle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    while running_practice:
        screen.blit(pygame.image.load("assets/2.jpg"), (0, 0))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exportation(inventaire)
                pygame.quit()
    
    running_course = True
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
    "La-langue-des-signes-main\assets\picturesforcourse\Alimentation et Divers.jpg",
    "La-langue-des-signes-main\assets\picturesforcourse\BaseetLieux.jpg",
    "La-langue-des-signes-main\assets\picturesforcourse\Famille.jpg",
    "La-langue-des-signes-main\assets\picturesforcourse\Santé.jpg",
    "La-langue-des-signes-main\assets\picturesforcourse\Sentiments.jpg",
    "La-langue-des-signes-main\assets\picturesforcourse\Temps.jpg",
    "La-langue-des-signes-main\assets\picturesforcourse\Vie en Société.jpg"]

    background_course = pygame.image.load(r"C:\La-langue-des-signes-main\La-langue-des-signes-main\assets\picturesforcourse\background.png").convert()
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
            cours_affichage = button((0,255,0), 750, 300 + i*75, title_of_the_lesson.get_width(), title_of_the_lesson.get_height())
            if cours_affichage.isOver():
                cours_affichage = button((0,155,0), 750, 300 + i*75, title_of_the_lesson.get_width(), title_of_the_lesson.get_height())
            cours_affichage.draw(screen)
            screen.blit(title_of_the_lesson,(750, 300 + i*75))
        
        screen.blit(title_course, (750, 120))
        pygame.display.flip()  # on rafraichie la page régulièrement

