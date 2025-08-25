from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from ferreteriaTorCuaDB import dbm

class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.widgets()

    def widgets(self):

        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        #frame1.pack()
        frame1.place(x=0, y=0, width=1500, height=70)

        titulo =tk.Label(self, text="INVETARIOS", bg="#dddddd", font="sans 30 bold", anchor="center")
        #titulo.pack()
        titulo.place(x=5, y=0, width=1490, height=60)

        frame2 = tk.Frame(self, bg="#7AD2EC", highlightbackground="gray", highlightthickness = 1)
        frame2.place(x=0, y=70, width=1500, height=650)

        lblframe = LabelFrame(frame2, text="Productos", font="sans 22 bold", bg="#7AD2EC")
        lblframe.place(x=20, y=5, width=400, height=640)

        lblproducto = Label(lblframe, text="Producto: ", font="sans 14 bold", bg="#7AD2EC")
        lblproducto.place(x=10, y=20)
        self.producto = ttk.Entry(lblframe, font="sans 14 bold")
        self.producto.place(x=140, y=20, width=240, height=40)

        lblproveedor = Label(lblframe, text="Proveedor: ", font="sans 14 bold", bg="#7AD2EC")
        lblproveedor.place(x=10, y=80)
        self.proveedor = ttk.Entry(lblframe, font="sans 14 bold")
        self.proveedor.place(x=140, y=80, width=240, height=40)
        
        options_marca = tk.StringVar()
        options_marca.set("Seleccione una marca")
        
        lblmarca= Label(lblframe, text="Marca: ", font="sans 14 bold", bg="#7AD2EC")
        lblmarca.place(x=10, y=140)
        self.marca = ttk.Combobox(lblframe, textvariable=options_marca, font="sans 14 bold", state="readonly")
        #self.marca['values'] = ["Marca1", "Marca2", "Marca3"]  # Puedes modificar las marcas según tus necesidades
        self.marca.place(x=140, y=140, width=240, height=40)
        
        lblmodelo= Label(lblframe, text="Modelo: ", font="sans 14 bold", bg="#7AD2EC")
        lblmodelo.place(x=10, y=200)
        self.modelo = ttk.Entry(lblframe, font="sans 14 bold")
        self.modelo.place(x=140, y=200, width=240, height=40)
        
        lblcodigo= Label(lblframe, text="Codigo: ", font="sans 14 bold", bg="#7AD2EC") 
        lblcodigo.place(x=10, y=260)
        self.codigo = ttk.Entry(lblframe, font="sans 14 bold")
        self.codigo.place(x=140, y=260, width=240, height=40)

        lblprecio= Label(lblframe, text="Precio: ", font="sans 14 bold", bg="#7AD2EC")
        lblprecio.place(x=10, y=320)
        self.precio = ttk.Entry(lblframe, font="sans 14 bold")
        self.precio.place(x=140, y=320, width=240, height=40)

        lblcosto= Label(lblframe, text="Costo: ", font="sans 14 bold", bg="#7AD2EC")
        lblcosto.place(x=10, y=380)
        self.costo = ttk.Entry(lblframe, font="sans 14 bold")
        self.costo.place(x=140, y=380, width=240, height=40)

        lblstock= Label(lblframe, text="Stock: ", font="sans 14 bold", bg="#7AD2EC")
        lblstock.place(x=10, y=440)
        self.stock = ttk.Entry(lblframe, font="sans 14 bold")
        self.stock.place(x=140, y=440, width=240, height=40)

        boton_agregar =tk.Button(lblframe, text="Ingresa", font="sans 12 bold", bg="#C6D9E3")
        boton_agregar.place(x=10, y=550, width=120, height=40)

        boton_editar =tk.Button(lblframe, text="Editar", font="sans 12 bold", bg="#C6D9E3")
        boton_editar.place(x=140, y=550, width=120, height=40)

        boton_eliminar =tk.Button(lblframe, text="Eliminar", font="sans 12 bold", bg="#C6D9E3")
        boton_eliminar.place(x=270, y=550, width=120, height=40)

        #tabla
        treframe = Frame(frame2, bg="white")
        treframe.place(x=440, y=50, width=740, height=580)

        scrol_y = ttk.Scrollbar(treframe, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treframe, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tre = ttk.Treeview(treframe, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40, columns=("ID", "PRODUCTO", "PROVEEDOR", "MARCA", "MODELO", "CODIGO","PRECIO", "COSTO", "STOCK"), show="headings")
        self.tre.pack(expand=True, fill=BOTH)

        scrol_y.config(command=self.tre.yview)
        scrol_x.config(command=self.tre.xview)

        self.tre.heading("ID", text="Id")
        self.tre.heading("PRODUCTO", text="Producto")
        self.tre.heading("PROVEEDOR", text="Proveedor")
        self.tre.heading("MARCA", text="Marca")
        self.tre.heading("MODELO", text="Modelo")
        self.tre.heading("CODIGO", text="Codigo")
        self.tre.heading("PRECIO", text="Precio")
        self.tre.heading("COSTO", text="Costo")
        self.tre.heading("STOCK", text="Stock")

        self.tre.column("ID", width=70, anchor="center")
        self.tre.column("PRODUCTO", width=100, anchor="center")
        self.tre.column("PROVEEDOR", width=100, anchor="center")
        self.tre.column("MARCA", width=100, anchor="center")
        self.tre.column("MODELO", width=100, anchor="center") 
        self.tre.column("CODIGO", width=100, anchor="center")
        self.tre.column("PRECIO", width=100, anchor="center")
        self.tre.column("COSTO", width=100, anchor="center")
        self.tre.column("STOCK", width=70, anchor="center")
        
    def limpiar_campos(self):
        self.producto.delete(0, END)
        self.proveedor.delete(0, END)
        self.marca.set("Seleccione una marca")
        self.modelo.delete(0, END)
        self.codigo.delete(0, END)
        self.precio.delete(0, END)
        self.costo.delete(0, END)
        self.stock.delete(0, END)
        
    def ordenar_treeview(self, column_name, documentos,reversed=False):
        datos_ordenados = sorted(self.tre.get_children(), key=lambda x: self.tre.set(x, documentos), reverse=reversed)
        self.tre.cargar_datos_en_treeview(datos_ordenados)
        
    def cargar_datos_en_treeview(self, datos):
        for item in self.tre.get_children():
            self.tre.delete(item)
            
        for fila in datos:
            self.tre.insert("", "end", values=(fila["ID"], fila["PRODUCTO"], fila["PROVEEDOR"], fila["MARCA"], fila["MODELO"], fila["CODIGO"], fila["PRECIO"], fila["COSTO"], fila["STOCK"]))
        
    def get_collection_inventario(self):
        self.tre.delete(*self.tre.get_children())
        
                
        self.ordenar_treeview(self, "ID", reversed=True)
            
    
        
    
    def boton_agregar_clicked(self):
        producto = self.producto.get()
        proveedor = self.proveedor.get()
        marca = self.marca.get()
        modelo = self.modelo.get()
        codigo = self.codigo.get()
        precio = self.precio.get()
        costo = self.costo.get()
        stock = self.stock.get()
        
        new_producto = {
            "producto": producto,
            "proveedor": proveedor,
            "marca": marca,
            "modelo": modelo,
            "codigo": codigo,
            "precio": precio,
            "costo": costo,
            "stock": stock
        }

        if not all([producto, proveedor, marca, modelo, codigo, precio, costo, stock]):
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return

        # Aquí agregarías la lógica para insertar el producto en la base de datos o lista
        # Por ejemplo:
        #insertar_producto(producto, proveedor, marca, modelo, codigo, precio, costo, stock)
        #conn = dbm.conectar()
        id_insert = dbm.insert_document("inventario", new_producto)
        if id_insert is None:
            messagebox.showerror("Error", "No se pudo agregar el producto. Intente nuevamente.")
            return
        else:   
            messagebox.showinfo("Éxito", "Producto agregado correctamente." + str(id_insert))
        self.limpiar_campos()
        self.get_collection_inventario()