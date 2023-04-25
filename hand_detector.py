# -*- coding: utf-8 -*-
# importation des librairies utiles au bon fonctionnement de ce fichier
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import pygame
from tools import *




labels = ["A", "B", "C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","rien","S","T","U","V","W","X"] # classifie les différentes positions des mains que cela représente
class SignDetector:
    def __init__ (self,screen):
        #self.pyscreen = screen
        #self.launch()
        self.cap = cv2.VideoCapture(0)
        self.detector = HandDetector(maxHands=1)
        self.success, self.img = self.cap.read()
        self.imgOutput = self.img.copy()
        self.hands, self.img = self.detector.findHands(self.img)
    def run(self,running_video):
        imgSize = 300 # donne la taille demandé pour l’image
        offset = 20 # donne la marge de l’image
        classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
        try:
            while running_video:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running_video = False
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running_video = False
                self.success, self.img = self.cap.read()
                self.imgOutput = self.img.copy()
                self.hands, self.img = self.detector.findHands(self.img)

                if self.hands:
                    hand = self.hands[0]
                    x, y, w, h = hand['bbox'] # permet d’obtenir les caractéristiques de la l’image centré sur la main

                    imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255 # crée une image carré blanche pour pouvoir peut importe la taille de la main obtenu par la webcam d’avoir une image de 300px par 300px
                    imgCrop = self.img[y - offset:y + h + offset, x - offset:x + w + offset] # permet que l’image est une marge pour mieux observer les extrémités des doigts

                    imgCropShape = imgCrop.shape

                    aspectRatio = h / w # cée une variable pour le ratio de la main et de l’image centré sur cette main

                    if aspectRatio > 1: # permet de définir si la partie non visible du carré crée doit avoir en haut et bas du blanc ou à droite et à gauche
                        k = imgSize / h
                        wCal = math.ceil(k * w)
                        imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                        imgResizeShape = imgResize.shape
                        wGap = math.ceil((imgSize - wCal) / 2)
                        imgWhite[:, wGap:wCal + wGap] = imgResize
                        prediction, index = classifier.getPrediction(imgWhite, draw=False)

                    else:
                        k = imgSize / w
                        hCal = math.ceil(k * h)
                        imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                        imgResizeShape = imgResize.shape
                        hGap = math.ceil((imgSize - hCal) / 2)
                        imgWhite[hGap:hCal + hGap, :] = imgResize
                        prediction, index = classifier.getPrediction(imgWhite, draw=False)

                    cv2.rectangle(self.imgOutput, (x - offset, y - offset-50),
                                  (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
                    cv2.putText(self.imgOutput, labels[index], (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2) # affiche le signe que l’on fait grâce au dossier Model ou une IA à pu s’entrainer
                    cv2.putText(self.imgOutput, "Echap pour quitter",(0,20),cv2.FONT_HERSHEY_COMPLEX, 1, (255,)*3, 2) # explique comment sortir de cette parti
                    cv2.rectangle(self.imgOutput, (x-offset, y-offset),
                                  (x + w+offset, y + h+offset), (255, 0, 255), 4) 

                if cv2.waitKey(1) == 27: # vérifie si la touche escape n’est pas appuyée
                    break
                cv2.imshow("Detecteur de Signe", self.imgOutput) # affiche le rendu visuel de l’image
                cv2.waitKey(1)
        
            # Ferme les fenêtres
            self.cap.release()
            cv2.destroyWindow("Detecteur de Signe")
            return True
        except:
            return False