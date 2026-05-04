import random
import string
def generate_victimID():
 result = []
 for x in range(55):
  result.append((random.choice(string.ascii_letters + string.digits)))
 victim_ID = "".join(result)
 print(victim_ID)
generate_victimID()

