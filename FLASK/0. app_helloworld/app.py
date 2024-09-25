# Se importa el módulo Flask desde el paquete flask
from flask import Flask

# Crea una instancia de la clase Flask
#El argumento __name__ le dice a Flask
#que utilice el nombre del archivo actual main.py
app = Flask(__name__)


# Este es un decorador que define una ruta que
# corresponde a la página principal del app
@app.route('/')
# Cuando alguien visite app(por ejemplo,  http://localhost:5000/),
# la función hello( será ejecutada)
def hello():
    return "<h1>Hello, Word Flask !</h1>"

# Solo se ejecuta si el archivo es ejecutado directamente 
# arranca la aplicación Flask en modo de depuración (debug=True)
if __name__=='__main__':
    app.run(debug=True, port=5000)

