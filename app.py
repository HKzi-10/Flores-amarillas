from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import io
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Crear un gráfico simple con Matplotlib
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    
    # Crear la figura del gráfico
    fig, ax = plt.subplots()
    ax.plot(x, y, label="y = x^2")
    ax.set(xlabel='X', ylabel='Y', title='Gráfico de ejemplo')
    ax.legend()

    # Guardar el gráfico en un objeto de memoria (sin necesidad de guardar el archivo)
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)  # Volver al inicio del archivo de memoria
    
    # Enviar el gráfico al navegador como una imagen
    return render_template('index.html', graph_url=img)

if __name__ == '__main__':
    app.run(debug=True)
