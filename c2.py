"""
C2 SERVER 
Description: 
"""
from flask import Flask

# Creas la instancia de la aplicación
app = Flask(__name__)

# Defines una "ruta": la dirección donde el servidor escuchará
@app.route('/')
def home():
    return "FazbearWare C2 Server"

# Ejecutas el servidor en localhost (127.0.0.1) y un puerto (ej. 5000)
if __name__ == '__main__':
    app.run(port=5000, debug=True)