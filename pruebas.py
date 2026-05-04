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
    text="1. Payment is accepted in Bitcoin (BTC) only. You must send the equivalent of $3000 USD to the wallet address provided below.\n\n"
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
    text=f"Your personal id : YUEHYWUEY38",
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