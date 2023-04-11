# -*- coding: utf-8 -*-
import pygame
from tools import bouton
from fonction import *

pygame.init()

pygame.font.init()

clock = pygame.time.Clock()
clock.tick(10)

font_h1 = pygame.font.SysFont('helvetic', 150)
font_h2 = pygame.font.SysFont('helvetic', 100)
font_h3 = pygame.font.SysFont('helvetic', 80)

pygame.display.set_caption("Le language des signes")
pygame.display.set_icon(pygame.image.load("./asserts/logo.jpg"))
screen = pygame.display.set_mode((1800, 900)) #, pygame.RESIZABLE)

screen_width = screen.get_width()
screen_height = screen.get_height()
reload = 2

running = True
running_accueil, inventaire = importation()
running_accueil = True
running_exercice = False
running_cours = False
running_video = False
running_settings = False


petite_fille = pygame.image.load("asserts/1.jpg")
écrou = pygame.image.load("asserts/écrou.png")
écrou = pygame.transform.scale(écrou, (150, 150))



while running:

    while running_accueil == True:
        if reload == 2 or screen_width != screen.get_width() or screen_height != screen.get_height():
            # initialisation de la page quand l'utilisateur ouvre l'application ou quand il modifie la taille de la fenêtre

            screen.fill(((10, 30, 60)))

            m_h = screen.get_height() / 6 * 5 # hauteur du menu
            m_L = screen.get_width() / 6 * 5 # longeur du menu
            m_x = screen.get_width() / 2 - m_L / 2 # abscisse du menu
            m_y = screen.get_height() / 2 - m_h / 2 # ordonné du menu
            m_i = 30 # espace entre les éléments du menu
            rotation = 0 # rotation de l'écrou du menu settings

            accueil = bouton((0, 210, 250), [(m_x, m_y), (m_x + m_L, m_y), (m_x + m_L, m_y + m_h/20*8), (m_x, m_y + m_h/20*8)])
            exerice = bouton((140, 255, 0), [(m_x , m_y + m_h/20*8 + m_i), (m_x + m_L/5*2, m_y + m_h/20*8 + m_i), (m_x + m_L/5, m_y + m_h), (m_x, m_y + m_h)])
            cours = bouton((250, 150, 0), [(m_x + m_L/5*2 + m_i, m_y + m_h/20*8 + m_i), (m_x + m_L, m_y + m_h/20*8 + m_i), (m_x + m_L, m_y + m_h/20*8 + m_i + m_h/20*6  - m_i/2), (m_x + m_L/10*3 + m_i, m_y + m_h/20*8 + m_i + m_h/20*6 - m_i/2)])
            video = bouton((200, 0, 100), [(m_x + m_L/10*3 + m_i - m_i*(m_L/5)/(m_h/20*12-m_i), m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L/10*3 + m_i - m_i*m_L/5/m_h/20*8 + m_L/10*5, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L/10 + m_i + m_L/5*3, m_y + m_h), (m_x + m_L/5 + m_i, m_y + m_h)])
            settings = bouton((120, 120, 120), [(m_x + m_L/10*3 + 2*m_i - m_i*m_L/5/m_h/20*8 + m_L/10*5 + m_i / 2, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L, m_y + m_h/20*8 + m_i + m_h/20*6 + m_i/2), (m_x + m_L, m_y + m_h), (m_x + m_L/10 + 2*m_i + m_L/5*3 + m_i / 2, m_y + m_h)])
            
            liste_bouton = [[accueil, running_accueil], [exerice, running_exercice], [cours, running_cours], [video, running_video], [settings, running_settings]]
            for b in liste_bouton:
                b[0].draw(screen)

            text = font_h1.render("La Langue Muette", 1, (255,255,255))
            screen.blit(text, (accueil.coor[0][0], (accueil.coor[1][1] + accueil.coor[2][1]) / 2))
            text2 = font_h3.render("Exercice", 1, (250,150,0))
            screen.blit(text2, (exerice.coor[0][0], (exerice.coor[1][1] + exerice.coor[2][1]) / 2))
            screen.blit(écrou, (settings.coor[0][0]+10, settings.coor[1][1]+10))

            reload = 0
        for b in liste_bouton:
            if b[0].isAu():
                if b[0].selection == False : b[0].select(screen)
                pressed = pygame.mouse.get_pressed()
                if pressed[0]: # 0=gauche, 1=milieu, 2=droite
                    running_accueil = False
                    b[1] = True
                    running_exercice = True
                    reload = 2
            else:
                if b[0].selection == True : b[0].unselect(screen)

        # if accueil.isAu():
        #     if accueil.selection == False : accueil.select(screen)
        #     pressed = pygame.mouse.get_pressed()
        #     if pressed[0]: # 0=gauche, 1=milieu, 2=droite
        #         running_accueil = "False"

        #         reload = 2
        # else: 
        #     if accueil.selection == True: accueil.unselect(screen)
        # screen.blit(text, ((accueil.coor[0][0] + accueil.coor[1][0]) / 2 - text.get_width()/2, (accueil.coor[1][1] + accueil.coor[2][1]) / 2 - text.get_height()/2))
        # if exerice.isAu():exerice.select(screen)
        # else: exerice.unselect(screen)
        # if cours.isAu():cours.select(screen)
        # else: cours.unselect(screen)
        # if video.isAu():video.select(screen, (240, 240, 0))
        # else: video.unselect(screen)
        # if settings.isAu():
        #     settings.select(screen)
        #     if rotation == 0:
        #         écrou = pygame.transform.rotate(écrou, 90)
        #         rotation = 1
        # else:
        #     settings.unselect(screen)
        #     if rotation == 1:
        #         écrou = pygame.transform.rotate(écrou, -90)
        #         rotation = 0
        # screen.blit(écrou, (settings.coor[0][0]+10, settings.coor[1][1]+18))
        # screen.blit(text2, ((exerice.coor[0][0] + exerice.coor[1][0] + exerice.coor[2][0] + exerice.coor[3][0]) / 4 - text2.get_width()/2, (exerice.coor[1][1] + exerice.coor[2][1]) / 2 - text2.get_height()))
        


        pygame.display.flip()  # on rafraichie la page régulièrement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


    running_exercice = False
    while running_exercice:
        screen.blit(pygame.image.load("asserts/2.jpg"), (0, 0))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exportation(inventaire)
                pygame.quit()
    
    running_cours = True
    c = Cours()
    while running_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exportation(inventaire)
                pygame.quit()

        
        Titre_cours = font_h1.render("Cours", 1, (255,255,255))
        cours_alphabet = font_h2.render("alphabet",1,(255,0,0))
        cours_santé = font_h2
        cours_action
        cours_alimentation
        cours_base_et_lieu
        cours_famille
        cours_santé
        cours_
        
        #screen.blit(pygame.image.load("asserts/2.jpg"), (0, 0))
        screen.blit(text, (400, 100))
        pygame.display.flip()  # on rafraichie la page régulièrement

    


