#This Code was maded only for edicational and learning purposes, i wanted to learn how ransomware works 
import pygame
import os
import random
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
   
  



