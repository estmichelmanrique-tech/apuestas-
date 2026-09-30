import random
import time


class Carro:

    def __init__(self, app, numero, color, y):
        self.app = app      
        self.numero = numero
        self.color = color
        self.y = y
        self.x = app.margen_izq
        self.direccion = 1
        self.vueltas_hechas = 0
        self.tiempo_inicio = None
        self.tiempo_final = None
        self.terminado = False
        self.after_id = None

        self.id_dibujo = app.canvas.create_rectangle(
            self.x, self.y, self.x + 40, self.y + app.alto_carro,
            fill=app.colores[self.color]
        )
        color_texto = "black" if self.color in app.colores_claros else "white"
        self.id_texto = app.canvas.create_text(
            self.x + 20, self.y + app.alto_carro // 2,
            text=str(numero), fill=color_texto
        )

    def iniciar(self):
        self.tiempo_inicio = time.time()
        self.programar_siguiente_movimiento()

    def programar_siguiente_movimiento(self):
        intervalo_base = random.randint(40, 150)
        intervalo_final = int(intervalo_base / self.app.multiplicador_velocidad.get())
        intervalo_final = max(5, intervalo_final)

        self.after_id = self.app.root.after(intervalo_final, self.mover)

    def mover(self):
        if self.terminado:
            return

        paso = 8
        self.x += paso * self.direccion

        self.app.canvas.move(self.id_dibujo, paso * self.direccion, 0)
        self.app.canvas.move(self.id_texto, paso * self.direccion, 0)

        if self.x <= self.app.margen_izq or self.x >= self.app.margen_der:
            self.direccion *= -1
            self.vueltas_hechas += 1

            if self.vueltas_hechas >= self.app.vueltas_objetivo:
                self.terminar()
                return

        self.programar_siguiente_movimiento()

    def terminar(self):
        self.terminado = True
        self.tiempo_final = time.time()
        tiempo_total = self.tiempo_final - self.tiempo_inicio
        self.app.registrar_llegada(self.numero, tiempo_total)