import random
import string
def generate_victimID():
 result = []
 for x in range(20):
  result.append((random.choice(string.ascii_letters + string.digits)))
 return "".join(result)
VICTIM_ID = generate_victimID()

