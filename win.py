"""
Wib - FazbearWare
Description: Create and manage the window that advise about the ransom 
"""
import tkinter as tk

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
