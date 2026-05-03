"""
UI Module - FazbearWare
Description: This module functions to alter the Windows visual interface, 
including wallpaper changes and ambient audio triggers.
"""

import ctypes
import pygame
import os

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