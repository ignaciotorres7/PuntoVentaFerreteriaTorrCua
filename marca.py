from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from connect_sql_server import *

class Marca(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1500, height=70)

        titulo = tk.Label(self, text="MARCAS", bg="#dddddd", font="sans 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x=5, y=0, width=1490, height=60)

        frame2 = tk.Frame(self, bg="#7AD2EC", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=70, width=1500, height=650)

        lblframe = LabelFrame(frame2, text="Marcas", font="sans 22 bold", bg="#7AD2EC")
        lblframe.place(x=20, y=5, width=400, height=640)

        lblmarca = Label(lblframe, text="Marca: ", font="sans 14 bold", bg="#7AD2EC")
        lblmarca.place(x=10, y=20)
        self.marca = ttk.Entry(lblframe, font="sans 14 bold")
        self.marca.place(x=140, y=20, width=240, height=40)
        
        option_Proveedor = tk.StringVar()
        option_Proveedor.set("Seleccione un proveedor")
        
        lblproveedor = Label(lblframe, text="Proveedor: ", font="sans 14 bold", bg="#7AD2EC")
        lblproveedor.place(x=10, y=80)
        self.proveedor = ttk.Combobox(lblframe, textvariable=option_Proveedor, font="sans 14 bold", state="readonly")
        self.proveedor.place(x=140, y=80, width=240, height=40)
        
        lblCodigo = Label(lblframe, text="Código: ", font="sans 14 bold", bg="#7AD2EC")
        lblCodigo.place(x=10, y=140)
        self.codigo = ttk.Entry(lblframe, font="sans 14 bold")
        self.codigo.place(x=140, y=140, width=240, height=40)
        
        #tabla
        treframe = Frame(frame2, bg="white")
        treframe.place(x=440, y=50, width=740, height=580)
        
        scrol_y = ttk.Scrollbar(treframe, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treframe, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treframe, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40, columns=("ID", "MARCA", "PROVEEDOR", "CODIGO"), show="headings")
        self.tree.pack(expand=True, fill=BOTH)

        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)
        
        #self.tree = ttk.Treeview(treframe, columns=("Marca", "Proveedor", "Código"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("MARCA", text="Marca")
        self.tree.heading("PROVEEDOR", text="Proveedor")
        self.tree.heading("CODIGO", text="Código")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("MARCA", width=200, anchor="center")
        self.tree.column("PROVEEDOR", width=200, anchor="center")
        self.tree.column("CODIGO", width=200, anchor="center")
        #self.tree.pack(fill=BOTH, expand=True)  

        btn_guardar = Button(lblframe, text="Guardar Marca", command=self.guardar_marca)
        btn_guardar.place(x=140, y=280, width=240, height=40)

    def guardar_marca(self):
        marca = self.marca.get()
        if marca:
            try:
                # Aquí se llamaría a la función para guardar la marca en la base de datos
                # Por ejemplo: guardar_marca_en_db(marca)
                messagebox.showinfo("Éxito", "Marca guardada correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar la marca: {e}")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una marca.")   