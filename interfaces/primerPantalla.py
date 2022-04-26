from tkinter import *
from tkinter import messagebox


class Ventana:

    def __init__(self, inter):
        self.interfaz = inter
        self.interfaz.geometry("800x600")
        self.interfaz.title("Alquila YA")
        self.dibujarVentana()

    def dibujarVentana(self):
        Button(self.interfaz, command=self.loginAdmin,
               text="Login Admin").place(x=700, y=10)
        Button(self.interfaz, command=self.alquilar,
               text="Alquilar").place(x=325, y=250)
        Button(self.interfaz, command=self.devolucion,
               text="Devolucion").place(x=425, y=250)

    def loginAdmin(self):
        print("Hola")

    def alquilar(self):
        print("Hola")

    def devolucion(self):
        print("Hola")


obj = Ventana(Tk())
obj.interfaz.mainloop()
