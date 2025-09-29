from flask import Flask

app = Flask(__name__)

@app.route('/Bienvenido')
def bienvenida():
    mensaje1 = '''
    <h1>Bienvenido a la calculadora de Python</h1>
    
    '''
    return mensaje1

@app.route('/factorial/<v1>')
def factorial(v1):
    fact=1
    for x in range(1,int(v1)+1):
        fact*=x
    return f"el factorial de {v1} es {fact}"

@app.route('/')
def holamundo():
    mensaje = '''
    <h1>Hola Mundo</h1>
    <p>Mi primer aplicación web con Flask</p>
    <p>Autor: Wendy</p>
    <p>Fecha: 2024-06-10</p>
    <p>Versión: 1.0</p>
    <p>Licencia: MIT</p>
    '''
    return mensaje



if __name__ == '__main__':
    app.run(debug=True)
    