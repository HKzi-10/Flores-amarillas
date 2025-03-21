from flask import Flask, render_template, Response
import matplotlib.pyplot as plt
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def home():
    # Configurar el gráfico
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Número de pétalos (puedes ajustarlo para cambiar la forma)
    num_petals = 20
    # Ángulo para crear la espiral
    theta = np.linspace(0, 2 * np.pi * num_petals, 1000)

    # Radio para la espiral logarítmica
    r = np.exp(0.1 * theta)

    # Dibujar la espiral para crear el patrón de los pétalos
    ax.plot(theta, r, color='yellow', linewidth=3)

    # Personalizar el gráfico
    ax.set_facecolor('black')  # Fondo negro para resaltar el girasol
    ax.set_rticks([])  # Eliminar las marcas del radio
    ax.set_yticklabels([])  # Eliminar las etiquetas del eje radial

    # Añadir círculos para los "pétalos" del girasol
    num_circles = 60
    for i in range(num_circles):
        angle = i * (2 * np.pi / num_circles)
        radius = np.exp(0.1 * angle)  # Radio de cada pétalo
        ax.plot(angle, radius, 'o', color='yellow', markersize=8)

    # Mostrar el gráfico
    ax.set_title("Girasol", fontsize=18, color='yellow')

    # Guardar el gráfico en un objeto de memoria
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)

    # Regresar la imagen en formato PNG como respuesta HTTP
    return Response(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
