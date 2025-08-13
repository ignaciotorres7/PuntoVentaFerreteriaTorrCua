from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from data_mogodb import *

class Reportes(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):

        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        #frame1.pack()
        frame1.place(x=0, y=0, width=1200, height=100)

        titulo =tk.Label(self, text="Reportes", bg="#dddddd", font="sans 30 bold", anchor="center")
        #titulo.pack()
        titulo.place(x=5, y=0, width=1190, height=90)
        
        frame2 = tk.Frame(self, bg="#7AD2EC", highlightbackground="gray", highlightthickness=1)
        #frame2.pack()
        frame2.place(x=0, y=100, width=1200, height=150)
        
        lblframe=tk.LabelFrame(frame2, text="Reportes", bg="#7AD2EC", font="sans 16 bold")
        lblframe.place(x=10, y=10, width=1180, height=30)
        
        lbl_tipo_reporte = tk.Label(lblframe, text="Tipo de Reporte: ", bg="#7AD2EC", font="sans 12 bold")
        lbl_tipo_reporte.place(x=10, y=50)
        
        self.tipo_reporte = ttk.Combobox(lblframe, font="sans 12 bold", state="readonly")
        self.tipo_reporte['values'] = ["Selecciona una opción", "Ventas", "Stok", "Proveedores", "Marcas", "Faltantes"]
        self.tipo_reporte.place(x=150, y=50, width=40)
        
        lbl_fecha_inicio = tk.Label(lblframe, text="Fecha Inicio: ", bg="#7AD2EC", font="sans 12 bold")
        lbl_fecha_inicio.place(x=250, y=50)
        
        self.fecha_inicio = DateEntry(lblframe, date_pattern="dd/MM/yyyy" , font="sans 12 bold")
        self.fecha_inicio.place(x=350, y=50, width=40)
        
        lbl_fecha_fin = tk.Label(lblframe, text="Fecha Fin: ", bg="#7AD2EC", font="sans 12 bold")
        lbl_fecha_fin.place(x=470, y=50)    
        
        self.fecha_fin = DateEntry(lblframe, date_pattern="dd/MM/yyyy", font="sans 12 bold")
        self.fecha_fin.place(x=550, y=50, width=40)
        
        self.btn_generar = tk.Button(lblframe, text="Generar Reporte", font="sans 12 bold", command=self.generar_reporte)
        self.btn_generar.place(x=700, y=45, width=150, height=40)
        
    def generar_reporte(self, tipo, fecha_inicio, fecha_fin):             
        #def generar_reporte():
        tipo = self.tipo_reporte.get()
        fecha_inicio = self.fecha_inicio.get_date()
        fecha_fin = self.fecha_fin.get_date()
            
        match tipo: #== "Selecciona una opción":
            case "Selecciona una opción":
                messagebox.showwarning("Advertencia", "Por favor, selecciona un tipo de reporte.")
                #return None
            case "Ventas":
                #generar_reporte(self, tipo, fecha_inicio, fecha_fin)
            #case "Stok":
                #generar_reporte(self, tipo, fecha_inicio, fecha_fin)
            #case "Proveedores":
                #generar_reporte(self, tipo, fecha_inicio, fecha_fin)
            #case "Marcas":
                #generar_reporte(self, tipo, fecha_inicio, fecha_fin)
            #case "Faltantes":
                #generar_reporte(self, tipo, fecha_inicio, fecha_fin)
            #case _:
                messagebox.showerror("Error", "Tipo de reporte no reconocido.") 
                
        #def generar_reporte(tipo, fecha_inicio, fecha_fin):
            
            
            
            
            
        # Aquí se llamaría a la función que genera el reporte según el tipo y las fechas
        # Por ejemplo:
        # generar_reporte(tipo, fecha_inicio, fecha_fin)
        #messagebox.showinfo("Información", f"Generando reporte de {tipo} desde {fecha_inicio} hasta {fecha_fin}.")