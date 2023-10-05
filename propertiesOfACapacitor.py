#----------------------------------------------------------------------------
# Physics 3 - Problem 5 
# Created By  : Xavier Lopez & Madeline Castro
# Created Date: 06/10/2023
# ---------------------------------------------------------------------------
""" Description: Create a user-friendly graphical interface for analyzing three capacitor types: 
parallel plate, spherical, and cylindrical. The interface allows users to customize dimensions, 
voltage, and dielectric presence, displaying real-time updates of physical properties and a cross-sectional capacitor image."""  
# ---------------------------------------------------------------------------
# Imports 
import tkinter as tk  
from tkinter import ttk  
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# ---------------------------------------------------------------------------

def obtener_datos(tipo_var, largo_entry, ancho_entry, radio_ext_entry, radio_int_entry, cil_radio_ext_entry, cil_radio_int_entry, cil_largo_entry, voltaje_entry, diel_var, cobertura_var):
    tipo_capacitor = tipo_var.get()
    if tipo_capacitor == "Paralelo":
        largo = float(largo_entry.get())
        ancho = float(ancho_entry.get())
        # Aquí puedes agregar tus cálculos para el capacitor paralelo
    elif tipo_capacitor == "Esférico":
        radio_exterior = float(radio_ext_entry.get())
        radio_interior = float(radio_int_entry.get())
        # Aquí puedes agregar tus cálculos para el capacitor esférico
    elif tipo_capacitor == "Cilíndrico":
        cil_radio_exterior = float(cil_radio_ext_entry.get())
        cil_radio_interior = float(cil_radio_int_entry.get())
        cil_largo = float(cil_largo_entry.get())
        # Aquí puedes agregar tus cálculos para el capacitor cilíndrico

    voltaje = float(voltaje_entry.get())
    es_dielelectrico = diel_var.get()
    if es_dielelectrico:
        cobertura = cobertura_var.get()
        # Aquí puedes agregar tus cálculos para el dieléctrico

    # Finalmente, muestra los resultados o realiza las operaciones que desees

        # Llamada a dibujar_capacitor
    if tipo_capacitor == "Paralelo":
        dibujar_capacitor(tipo_capacitor, largo=largo, ancho=ancho)
    elif tipo_capacitor == "Esférico":
        dibujar_capacitor(tipo_capacitor, radio_exterior=radio_exterior, radio_interior=radio_interior)
    elif tipo_capacitor == "Cilíndrico":
        dibujar_capacitor(tipo_capacitor, cil_radio_exterior=cil_radio_exterior, cil_radio_interior=cil_radio_interior, cil_largo=cil_largo)

def actualizar_interfaz(tipo_var, frame_detalles, largo_label, largo_entry, ancho_label, ancho_entry, radio_ext_label, radio_ext_entry, radio_int_label, radio_int_entry, cil_radio_ext_label, cil_radio_ext_entry, cil_radio_int_label, cil_radio_int_entry, cil_largo_label, cil_largo_entry):
   
    tipo_capacitor = tipo_var.get()
    for widget in frame_detalles.winfo_children():
        widget.grid_forget()

    if tipo_capacitor == "Paralelo":
        largo_label.grid(row=0, column=0)
        largo_entry.grid(row=0, column=1)
        ancho_label.grid(row=1, column=0)
        ancho_entry.grid(row=1, column=1)

    elif tipo_capacitor == "Esférico":
        radio_ext_label.grid(row=0, column=0)
        radio_ext_entry.grid(row=0, column=1)
        radio_int_label.grid(row=1, column=0)
        radio_int_entry.grid(row=1, column=1)

    elif tipo_capacitor == "Cilíndrico":
        cil_radio_ext_label.grid(row=0, column=0)
        cil_radio_ext_entry.grid(row=0, column=1)
        cil_radio_int_label.grid(row=1, column=0)
        cil_radio_int_entry.grid(row=1, column=1)
        cil_largo_label.grid(row=2, column=0)
        cil_largo_entry.grid(row=2, column=1)

def dibujar_capacitor(tipo, canvas, es_dielelectrico=False, cobertura="Todo", **kwargs):
    fig = plt.Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)

    if tipo == "Paralelo":
        largo = kwargs.get("largo", 1)
        ancho = kwargs.get("ancho", 1)
        ax.add_patch(patches.Rectangle((0, 0), largo, ancho, fill=True))

        if es_dielelectrico:
            if cobertura == "Todo":
                ax.add_patch(patches.Rectangle((0, 0), largo, ancho, fill=True, color='lightblue'))
            elif cobertura == "Mitad":
                ax.add_patch(patches.Rectangle((0, 0), largo/2, ancho, fill=True, color='lightblue'))

    elif tipo == "Esférico":
        radio_exterior = kwargs.get("radio_exterior", 1)
        radio_interior = kwargs.get("radio_interior", 0.7)
        ax.add_patch(patches.Circle((0, 0), radio_exterior, fill=True, color='blue'))
        ax.add_patch(patches.Circle((0, 0), radio_interior, fill=True, color='white'))

        if es_dielelectrico:
            if cobertura == "Todo":
                ax.add_patch(patches.Circle((0, 0), radio_interior, fill=True, color='lightblue'))
            elif cobertura == "Mitad":

    elif tipo == "Cilíndrico":
        cil_radio_exterior = kwargs.get("cil_radio_exterior", 1)
        cil_radio_interior = kwargs.get("cil_radio_interior", 0.7)
        cil_largo = kwargs.get("cil_largo", 3)
        ax.add_patch(patches.Rectangle((-cil_largo/2, -cil_radio_exterior), cil_largo, 2*cil_radio_exterior, fill=True, color='blue'))
        ax.add_patch(patches.Rectangle((-cil_largo/2, -cil_radio_interior), cil_largo, 2*cil_radio_interior, fill=True, color='white'))

        if es_dielelectrico:
            if cobertura == "Todo":
                ax.add_patch(patches.Rectangle((-cil_largo/2, -cil_radio_interior), cil_largo, 2*cil_radio_interior, fill=True, color='lightblue'))
            elif cobertura == "Mitad":
            
    ax.set_aspect('equal')
    ax.autoscale_view()
    plt.axis('off')

    for widget in canvas.winfo_children():
        widget.destroy()
    
    chart = FigureCanvasTkAgg(fig, canvas)
    chart.get_tk_widget().pack()

    plt.show()

def main():

    app = tk.Tk()
    app.title("Calculadora de Capacitores")

    # Centrar el título y hacerlo negrita
    ttk.Label(app, text="Calculadora de Capacitores", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

    tipo_var = ttk.Combobox(app, values=["Paralelo", "Esférico", "Cilíndrico"])
    tipo_var.grid(row=1, column=1, pady=10)
    ttk.Label(app, text="Tipo de capacitor:").grid(row=1, column=0, pady=10, sticky=tk.W)

    frame_detalles = ttk.Frame(app)
    frame_detalles.grid(row=2, column=0, columnspan=2, pady=10)

    # Widgets para capacitor paralelo
    largo_label = ttk.Label(frame_detalles, text="Largo:")
    largo_entry = ttk.Entry(frame_detalles)
    ancho_label = ttk.Label(frame_detalles, text="Ancho:")
    ancho_entry = ttk.Entry(frame_detalles)

    # Widgets para capacitor esférico
    radio_ext_label = ttk.Label(frame_detalles, text="Radio exterior:")
    radio_ext_entry = ttk.Entry(frame_detalles)
    radio_int_label = ttk.Label(frame_detalles, text="Radio interior:")
    radio_int_entry = ttk.Entry(frame_detalles)

    # Widgets para capacitor cilíndrico
    cil_radio_ext_label = ttk.Label(frame_detalles, text="Radio exterior:")
    cil_radio_ext_entry = ttk.Entry(frame_detalles)
    cil_radio_int_label = ttk.Label(frame_detalles, text="Radio interior:")
    cil_radio_int_entry = ttk.Entry(frame_detalles)
    cil_largo_label = ttk.Label(frame_detalles, text="Largo:")
    cil_largo_entry = ttk.Entry(frame_detalles)

    ttk.Label(app, text="Voltaje:").grid(row=3, column=0, pady=10, sticky=tk.W)
    voltaje_entry = ttk.Entry(app)
    voltaje_entry.grid(row=3, column=1, pady=10)

    diel_var = tk.BooleanVar()

    cobertura_label = ttk.Label(app, text="Cobertura del dieléctrico:")
    cobertura_var = ttk.Combobox(app, values=["Todo", "Mitad"])

    def mostrar_cobertura(*args):
        if diel_var.get():
            cobertura_label.grid(row=6, column=0, pady=10, sticky=tk.W)
            cobertura_var.grid(row=6, column=1, pady=10)
        else:
            cobertura_label.grid_forget()
            cobertura_var.grid_forget()

    diel_var.trace_add("write", mostrar_cobertura)
    ttk.Checkbutton(app, text="¿Usar dieléctrico?", variable=diel_var).grid(row=5, column=0, columnspan=2, pady=10)


    def combined_functions(event):
        actualizar_interfaz(tipo_var, frame_detalles, largo_label, largo_entry, ancho_label, ancho_entry, radio_ext_label, radio_ext_entry, radio_int_label, radio_int_entry, cil_radio_ext_label, cil_radio_ext_entry, cil_radio_int_label, cil_radio_int_entry, cil_largo_label, cil_largo_entry)
        obtener_datos(tipo_var, largo_entry, ancho_entry, radio_ext_entry, radio_int_entry, cil_radio_ext_entry, cil_radio_int_entry, cil_largo_entry, voltaje_entry, diel_var, cobertura_var)


    tipo_var.bind("<<ComboboxSelected>>", combined_functions)

    ttk.Button(app, text="Calcular", command=lambda: obtener_datos(tipo_var, largo_entry, ancho_entry, radio_ext_entry, radio_int_entry, pendiente_entry, voltaje_entry, diel_var, cobertura_var)).grid(row=7, column=0, columnspan=2, pady=10)

    canvas = tk.Canvas(app)
    canvas.grid(row=8, column=0, columnspan=2, pady=10)


    app.mainloop()

if __name__ == "__main__":
    main()