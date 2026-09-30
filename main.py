import tkinter as tk

from app_carrera import AppCarrera

num_carros = 10

colores = {
    "rojo": "red",
    "azul": "blue",
    "verde": "green",
    "naranja": "orange",
    "morado": "purple",
    "marron": "brown",
    "cian": "cyan",
    "magenta": "magenta",
    "dorado": "gold",
    "negro": "black",
}
colores_claros = ["cian", "dorado"]

ancho_canvas = 700
alto_canvas = 420
margen_izq = 40
margen_der = 660
alto_carro = 20
separacion_carril = 38


if __name__ == "__main__":
    root = tk.Tk()
    app = AppCarrera(root, num_carros, colores, colores_claros, ancho_canvas,
                     alto_canvas, margen_izq, margen_der, alto_carro,
                     separacion_carril)
    root.mainloop()