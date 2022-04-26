from tkinter import *
from functools import partial
from tkinter import messagebox

root = Tk()
root.title("Principal")
root.geometry("800x600")


def validacion(valor, ventana):

    if valor == "Rodrigo":
        ventanaAdmin()
    else:
        messagebox.showwarning("Error", "Contraseña incorrecta")


def nuevaVentana():
    root.withdraw()
    ventana2 = Toplevel()
    ventana2.geometry("800x600")
    ventana2.configure(background="black")
    ventana2.title("Iniciar Sesion")
    etiqueta = Label(ventana2, text="Ingrese contraseña").place(x=10, y=10)
    valorEntrada = Entry(ventana2).place(x=10, y=50)
    Button(ventana2, text="valida",
           command=partial(validacion, valorEntrada, ventana2)).place(x=10, y=90)


def ventanaAdmin():
    ventana2.withdraw()
    ventana3 = Toplevel()
    ventana3.geometry("800x600")
    ventana3.title("Ventana Admin")
    etiquetaAdmin = Label(ventana3, text="Exito!!!").place(x=10, y=10)


enviar = Button(root, text="login", command=nuevaVentana).place(x=10, y=50)

mainloop()
