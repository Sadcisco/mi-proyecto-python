from flask import Flask
app = Flask(__name__)

@app.route('/nueva-ruta')
def nueva_ruta():
    return '¡Esta es una nueva ruta!'

@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'


if __name__ == '__main__':
    app.run(port=5000)

