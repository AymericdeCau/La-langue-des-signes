Le dossier Model permet de détecter les signes fait à travers la webcam. Cette IA a été entrainé grâce au site web https://teachablemachine.withgoogle.com/train/image qui m’a permit de pouvoir détecter chaque signe par les images que je lui ai envoyé de ma main en train de faire le signe. Ces enregistrements ont été faite dans un programme ressemblant presque exactement à celui de hand_detector.py avec en plus dans la boucle while :
"key = cv2.waitKey(1)
if key == ord("s"): # si la touche "s" est appuyé cela enregistreles images
    counter += 1
    cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgwhite)
    print(counter)"

