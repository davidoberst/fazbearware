import os  
home_path =  os.path.expanduser('~')
current_user = os.getlogin()
print(home_path)
print(current_user)