#This Code was maded only for edicational and learning purposes, i wanted to learn how ransomware works 
import pygame
import os
import sys

def path_search():
    for dir,subdir,files in os.walk("C:/Users/USUARIO/Desktop/obs"):
        print(f"Dir : {dir}")
        print(f"subdir : {subdir}")
        print(f"files : {files}")

path_search()




 



def fazwin():
    pygame.init() #init pygame
    pygame.mixer.init() #init pygame audio module
 # create window
    wind = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("")
 #load img and music
    fazbear_img = pygame.image.load("./assets/img.jpg")
    pygame.mixer.music.load("./assets/aud.mp3")
    pygame.mixer.music.play(-1)
    execute_win = True
    # window loop
    while execute_win:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                execute_win = False
     #load window
        wind.fill((0, 0, 0)) 
        wind.blit(fazbear_img, (0, 0))
        pygame.display.flip()

    pygame.quit()