from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3, 1)
        estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"

        return render_template('resultado1.html',
                               promedio=promedio,
                               estado=estado,
                               asistencia=asistencia)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        caracteres = len(nombre_mas_largo)

        return render_template('resultado2.html',
                               nombre=nombre_mas_largo,
                               caracteres=caracteres)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)