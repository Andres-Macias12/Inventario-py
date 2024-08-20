from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Lista para almacenar los productos
productos = [
    Producto("Laptop", 10, 999.99),
    Producto("Teclado", 25, 49.99),
    Producto("Ratón", 30, 29.99)
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar_producto():
    try:
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        nuevo_producto = Producto(nombre, cantidad, precio)
        productos.append(nuevo_producto)
        return redirect(url_for('index'))
    except ValueError:
        return "Error: Cantidad y precio deben ser números válidos."

@app.route('/buscar', methods=['POST'])
def buscar_producto():
    nombre = request.form['nombre']
    resultado = [producto for producto in productos if producto.nombre.lower() == nombre.lower()]
    return render_template('index.html', productos=resultado)

@app.route('/actualizar', methods=['POST'])
def actualizar_producto():
    try:
        nombre = request.form['nombre']
        nueva_cantidad = int(request.form['cantidad'])
        for producto in productos:
            if producto.nombre.lower() == nombre.lower():
                producto.cantidad = nueva_cantidad
                return redirect(url_for('index'))
        return "Producto no encontrado."
    except ValueError:
        return "Error: La cantidad debe ser un número válido."

@app.route('/eliminar', methods=['POST'])
def eliminar_producto():
    nombre = request.form['nombre']
    global productos
    productos = [producto for producto in productos if producto.nombre.lower() != nombre.lower()]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
