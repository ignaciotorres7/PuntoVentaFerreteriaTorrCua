from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from connect_sql_server import *
import connect_sql_server as csql

class Ventas(tk.Frame):
    db_name = "connect_sql_server.py"
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):

        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        #frame1.pack()
        frame1.place(x=0, y=0, width=1200, height=70)

        titulo =tk.Label(self, text="VENTAS", bg="#dddddd", font="sans 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x=5, y=0, width=1190, height=60)

        frame2 = tk.Frame(self, bg="#7AD2EC", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=70, width=1200, height=650)

        lblframe = LabelFrame(frame2, text="Informacion de la venta", bg="#7AD2EC", font="sans 16 bold")
        lblframe.place(x=10, y=10, width=1160, height=80)

        label_numero_factura = tk.Label(lblframe, text="No. Factura", bg="#7AD2EC", font="sans 12 bold")
        label_numero_factura.place(x=10, y=5)
        self.num_factura = tk.StringVar()

        self.entry_num_factura = ttk.Entry(lblframe, textvariable=self.num_factura, state="readonly", font="sans 12 bold")
        self.entry_num_factura.place(x=150, y=5, width=80)

        label_producto = tk.Label(lblframe, text="Productos: ", bg="#7AD2EC", font="sans 12 bold")
        label_producto.place(x=250, y=5)

        self.entry_producto = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_producto.place(x=350, y=5, width=180)

        label_valor =tk.Label(lblframe, text="Precio: ", bg="#7AD2EC", font="sans 12 bold")
        label_valor.place(x=550, y=5)

        self.entry_precio = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_precio.place(x=620, y=5, width=180)

        label_cantidad = tk.Label(lblframe, text="Cantidad: ", bg="#7AD2EC", font="sans 12 bold")
        label_cantidad.place(x=820, y=5)

        self.entry_cantidad = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_cantidad.place(x=920, y=5)

        treFrame = tk.Frame(frame2, bg="#7AD2EC")
        treFrame.place(x=10, y=150, width=1160, height=300)

        scrol_y=ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x=ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treFrame, columns=("Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)

        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Precio")
        self.tree.heading("#3", text="Cantidad")
        self.tree.heading("#4", text="Subtotal")

        self.tree.column("Producto", anchor="center")
        self.tree.column("Precio", anchor="center")
        self.tree.column("Cantidad", anchor="center")
        self.tree.column("Subtotal", anchor="center")

        self.tree.pack(expand=True, fill=BOTH)

        lblframe1 = LabelFrame(frame2, text="Opciones", bg="#7AD2EC", font="sans 12 bold")
        lblframe1.place(x=10, y=500, width=1160, height=120)

        boton_agregar = tk.Button(lblframe1, text="Agregar Articulo", bg="#C6D9E3")
        boton_agregar.place(x=50, y=10, width=240, height=50)

        boton_pagar = tk.Button(lblframe1, text="Pagar", bg="#C6D9E3")
        boton_pagar.place(x=450, y=10, width=240, height=50)

        boton_facturas= tk.Button(lblframe1, text="Ver Facturas", bg="#C6D9E3")
        boton_facturas.place(x=850, y=10, width=240, height=50)

        self.lbl_suma_total = tk.Label(frame2, text="Total a pagar: MXN 0", bg="#7AD2EC", font="sans 25 bold")
        self.lbl_suma_total.place(x=360, y=450)
        self.lbl_suma_total.config(anchor="center")

    def cargar_Productos(self):
        try:
            conn = csql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Productos")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los productos: {e}")
        finally:
            if conn:
                conn.close()
        self.cargar_Productos()
        self.entry_num_factura.config(state="normal")
        self.entry_num_factura.delete(0, END)
        self.entry_num_factura.insert(0, str(self.generar_numero_factura()))
        self.entry_num_factura.config(state="readonly")

    #def generar_numero_factura(self):
            


