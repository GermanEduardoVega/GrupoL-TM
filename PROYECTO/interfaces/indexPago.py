from tkinter import ttk  # biblioteca para diseniar interfaz
from tkinter import *  # botones tablas .. etc

import sqlite3  # modulo para conexion

# Obtiene ancho del área de visualización.
screenWidth = root.winfo_screenwidth()
# Obtiene altura del área de visualización.
screenHeight = root.winfo_screenheight()
# Establece ancho de la ventana.
width = 500
# Establece altura de la ventana.
height = 500
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
# Ancho x Alto + Desplazamiento x + Desplazamiento y
root.geometry("%dx%d+%d+%d" % (width, height, left, top))


# clase pago va a tener todos los metodos de mi ventana (titulo botones, entradas dde texto) funcionalidad de nuestras ventanas
class Pago:
    def __init__(self, ventana):  # funcion (constructor de nuestra clase)
        self.wind = ventana  # wind (almacenar ventana como parametro)
        self.wind.title('Pago')  # titulo de la ventana

        # interfaz creo un contenedor (Frame)
        # elemento de bibioteca ttk lo asignamos a la variable frame
        frame = LabelFrame(self.wind, text='agregar un Pago')
        frame.grid(row=0, column=0, columnspan=3, pady=20)  # metodo grid(posicionamiento)
        # fila  , columna   desplazar columnas , espaciado

        # entrada para nombre(caja de texto etiqueta)

        # Label(frame, text='Name').grid(row=1, column=0)  # metodo Label      fila 1, texto
        # self.name = Entry(frame)  # entrada
        # self.name.focus()
        # self.name.grid(row=1, column=1)  # metodo grid(posicionamiento)

        # boton de Pago
        ttk.Button(frame, text='Pagando').grid(row=3, columnspan=2, sticky=W+E)


if __name__ == '__main__':  # arrancar app
    ventana = Tk()  # ejecutar tk me devuelve ventana(de app)
    app = Pago(ventana)
    ventana.mainloop()  # final **ejecutar ventana
