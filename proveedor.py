from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from connect_sql_server import *

class Proveedor(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1500, height=70)

        titulo = tk.Label(self, text="PROVEEDORES", bg="#dddddd", font="sans 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x=5, y=0, width=1490, height=60)

        frame2 = tk.Frame(self, bg="#7AD2EC", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=70, width=1500, height=650)

        lblframe = LabelFrame(frame2, text="Proveedores", font="sans 22 bold", bg="#7AD2EC")
        lblframe.place(x=20, y=5, width=400, height=640)

        lblproveedor = Label(lblframe, text="Proveedor: ", font="sans 14 bold", bg="#7AD2EC")
        lblproveedor.place(x=10, y=20)
        self.proveedor = ttk.Entry(lblframe, font="sans 14 bold")
        self.proveedor.place(x=140, y=20, width=240, height=40)
        
        lblnombre_contacto = Label(lblframe, text="Nombre\n Contacto: ", font="sans 14 bold", bg="#7AD2EC")
        lblnombre_contacto.place(x=10, y=80)
        self.nombre_contacto = ttk.Entry(lblframe, font="sans 14 bold")
        self.nombre_contacto.place(x=140, y=80, width=240, height=40)

        lbltelefono = Label(lblframe, text="Teléfono: ", font="sans 14 bold", bg="#7AD2EC")
        lbltelefono.place(x=10, y=140)
        self.telefono = ttk.Entry(lblframe, font="sans 14 bold")
        self.telefono.place(x=140, y=140, width=240, height=40)

        lbldireccion = Label(lblframe, text="Dirección: ", font="sans 14 bold", bg="#7AD2EC")
        lbldireccion.place(x=10, y=200)
        self.direccion = ttk.Entry(lblframe, font="sans 14 bold")
        self.direccion.place(x=140, y=200, width=240, height=40)
        
        lblURLCatalogo = Label(lblframe, text="URL Catálogo: ", font="sans 14 bold", bg="#7AD2EC")
        lblURLCatalogo.place(x=10, y=260)
        self.url_catalogo = ttk.Entry(lblframe, font="sans 14 bold")
        self.url_catalogo.place(x=140, y=260, width=240, height=40)
        
        lblcorreo = Label(lblframe, text="Correo: ", font="sans 14 bold", bg="#7AD2EC")
        lblcorreo.place(x=10, y=320)
        self.correo = ttk.Entry(lblframe, font="sans 14 bold")
        self.correo.place(x=140, y=260, width=240, height=40)
               
        #TABLA
        treframe = Frame(frame2, bg="white")
        treframe.place(x=440, y=50, width=740, height=580)

        scrol_y = ttk.Scrollbar(treframe, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treframe, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tre = ttk.Treeview(treframe, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40, columns=("ID", "PROVEEDOR", "CONTACTO", "TELEFONO", "DIRECCION","URL", "CORREO"), show="headings")
        self.tre.pack(expand=True, fill=BOTH)

        scrol_y.config(command=self.tre.yview)
        scrol_x.config(command=self.tre.xview)

        self.tre.heading("ID", text="Id")
        self.tre.heading("PROVEEDOR", text="Proveedor")
        self.tre.heading("CONTACTO", text="Contacto")
        self.tre.heading("TELEFONO", text="Telefono")
        self.tre.heading("DIRECCION", text="Dirección")
        self.tre.heading("URL", text="URL Catálogo")
        self.tre.heading("CORREO", text="Correo")
        
        self.tre.column("ID", width=70, anchor="center")
        self.tre.column("PROVEEDOR", width=100, anchor="center")
        self.tre.column("CONTACTO", width=100, anchor="center")
        self.tre.column("TELEFONO", width=100, anchor="center") 
        self.tre.column("DIRECCION", width=100, anchor="center")
        self.tre.column("URL", width=100, anchor="center")
        self.tre.column("CORREO", width=100, anchor="center")
        
        btn_guardar = Button(lblframe, text="Guardar Proveedor", command=self.guardar_proveedor)
        btn_guardar.place(x=140, y=380, width=240, height=40)
        
    def guardar_proveedor(self):
        proveedor = self.proveedor.get()
        telefono = self.telefono.get()
        direccion = self.direccion.get()

        if proveedor and telefono and direccion:
            try:
                # Aquí se llamaría a la función para guardar el proveedor en la base de datos
                # Por ejemplo: guardar_proveedor_en_db(proveedor, telefono, direccion)
                messagebox.showinfo("Éxito", "Proveedor guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el proveedor: {e}")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")