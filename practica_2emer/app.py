from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)

# Ruta principal con el menú de opciones
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para inscripción en curso
@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        # Procesar los datos recibidos
        # Aquí podrías guardar los datos en una base de datos, por ejemplo.
        return f"Inscripción recibida: {nombre} {apellido} en el curso {curso}"
    return render_template('inscripcion.html')

# Ruta para el registro de usuarios
@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        # Procesar los datos recibidos
        return f"Usuario registrado: {nombre} {apellido}, Correo: {correo}"
    return render_template('registro_usuarios.html')

# Ruta para el registro de productos
@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        # Procesar los datos recibidos
        return f"Producto registrado: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}"
    return render_template('registro_productos.html')

# Ruta para el registro de libros
@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        # Procesar los datos recibidos
        return f"Libro registrado: {titulo}, Autor: {autor}, Medio: {medio}"
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)
    