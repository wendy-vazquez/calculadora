from flask import Flask

app = Flask(__name__)

@app.route('/')
def bienvenida():
    mensaje1 = '''
    <h1>Bienvenido a la calculadora de Python</h1>
    <h2>para sumar teclear presiona o escribe en el navegador 127.0.0.1:5000/sumar/10/20</h2>
    <h2>para restar teclear presiona o escribe en el navegador 127.0.0.1:5000/res/10/20</h2>
    <h2>para multiplicar teclear presiona o escribe en el navegador 127.0.0.1:5000/mult/10/20</h2>
    <h2>para dividir teclear presiona o escribe en el navegador 127.0.0.1:5000/div/10/20</h2>
    <h2>para numero maximo teclear presiona o escribe en el navegador 127.0.0.1:5000/min/10/20</h2>
    <h2>para numero minimo teclear presiona o escribe en el navegador 127.0.0.1:5000/max/10/20</h2>
    <h2>para calcular el factorial teclear presiona o escribe en el navegador 127.0.0.1:500/factorial/10/20<h2>
    '''
    return mensaje1

@app.route('/sumar/<v1>/<v2>')
def sumar(v1,v2):
    return f"la suma de {v1} + {v2} es {int(v1)+int(v2)}"

@app.route('/res/<v1>/<v2>')
def restar(v1,v2):
    return f"la resta de {v1} - {v2} es {int(v1)-int(v2)}"

    
@app.route('/mult/<v1>/<v2>')
def multiplicar(v1, v2):
    return f"la multiplicacion de {v1} * {v2} es {int(v1)*int(v2)}"

    
@app.route('/div/<v1>/<v2>')
def dividir(v1, v2):
    return f"la division de {v1} / {v2} es {int(v1)/int(v2)}"

    
@app.route('/max/<v1>/<v2>')
def maximo(v1, v2):
    if int(v1)>int(v2):
        return f"el numero maximo es {v1}"
    else:
        return f"el numero maximo es {v2}"
    
@app.route('/min/<v1>/<v2>')
def minimo(v1, v2):
    if int(v1)<int(v2):
        return f"el numero minimo es {v1}"
    else:
        return f"el numero minimo es {v2}"

@app.route('/factorial/<v1>')
def factorial(v1):
    fact=1
    for x in range(1,int(v1)+1):
        fact*=x
    return f"el factorial de {v1} es {fact}"


if __name__ == '__main__':
    app.run(debug=True)
    