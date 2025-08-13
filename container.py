from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from reportes import Reportes
#from catalogos import Catalogos
from marca import Marca
from proveedor import Proveedor
from faltantes import Faltantes
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=1200, height=750)
        self.config(bg="#7AD2EC")
        self.widgets()

    def show_frames(self, container):
        top_level= tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#7AD2EC")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1200x750+120+20")
        top_level.resizable(False, False)

    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        self.show_frames(Inventario)

    def reportes(self):
        self.show_frames(Reportes)
        
    def proveedor(self):
        self.show_frames(Proveedor)

    def marcas(self):
        self.show_frames(Marca)

    def faltantes(self):
        self.show_frames(Faltantes)

    def widgets(self):
        frame1 = tk.Frame(self, bg="#7AD2EC" )
        frame1.pack()
        frame1.place(x=0, y=0, width=1200, height= 750)

        btventas = Button(frame1, bg="#0abf29", fg="white", font="sans 18 bold", text="Venta", command=self.ventas)
        btventas.place(x=800, y=30, width=240, height=60)

        btinventario = Button(frame1, bg="#175ee3", fg="white", font="sans 18 bold", text="Inventario", command=self.inventario)
        btinventario.place(x=800, y=130, width=240, height=60)
        
        btnproveedor = Button(frame1, bg="#17e38e", fg="white", font="sans 18 bold", text="Proveedores", command=self.proveedor)
        btnproveedor.place(x=800, y=230, width=240, height=60)

        btnmarcas = Button(frame1, bg="#eba117", fg="white", font="sans 18 bold", text="Marcas", command=self.marcas)
        btnmarcas.place(x=800, y=330, width=240, height=60)
        #btcatalogos = Button(frame1, bg="#eba117", fg="white", font="sans 18 bold", text="Catálogos en Linea", command=self.catalogos)
        #btcatalogos.place(x=800, y=230, width=240, height=60)

        btreportes = Button(frame1, bg="#ebcb17", fg="black", font="sans 18 bold", text="Reportes", command=self.reportes)
        btreportes.place(x=800, y=430, width=240, height=60)

        btfaltantes = Button(frame1, bg="#fd0101", fg="white", font="sans 18 bold", text="Faltantes", command=self.faltantes)
        btfaltantes.place(x=800, y=530, width=240, height=60)

        self.logo_image = Image.open("images/Ferreteria.jpg")
        self.logo_image = self.logo_image.resize((580,580))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")
        self.logo_label.place(x=100, y=100)

        copyright_label = tk.Label(frame1, text="© 2024 Torres TI Solutions Todos los derechos reservados", font="sans 8 bold", bg="#C6D9E3", fg="gray")
        copyright_label.place(x=700, y=700)
        
