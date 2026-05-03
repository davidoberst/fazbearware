"""
Wib - FazbearWare
Description: Create and manage the window that advise about the ransom 
"""
import tkinter as tk

window = tk.Tk()
window.title("FOUR FILES ARE ENCRYPTED BY FAZBEARWARE")
window.geometry("800x600")
window.configure(bg="black")
title = tk.Label(
    window,
    text="Oops! All your files are encrypted",  
    fg="red",
    bg="black",
    font=("Georgia",22),
    padx=20,pady=20
)

title.pack(side="top", fill="x", anchor="n")





title.pack(expand=True)
window.mainloop()
