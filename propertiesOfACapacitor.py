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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# ---------------------------------------------------------------------------

def getData(typeVar, canvas, lengthEntry, widthEntry, outerRadiusEntry, innerRadiusEntry, cylOuterRadiusEntry, cylInnerRadiusEntry, cylLengthEntry, voltageEntry, dielecVar, coverageVar):
    capacitorType = typeVar.get()
    if capacitorType == "Paralelo":
        length = float(lengthEntry.get())
        width = float(widthEntry.get())
        # You can add your calculations for the parallel capacitor here
    elif capacitorType == "Esférico":
        outerRadius = float(outerRadiusEntry.get())
        innerRadius = float(innerRadiusEntry.get())
        # You can add your calculations for the spherical capacitor here
    elif capacitorType == "Cilíndrico":
        cylOuterRadius = float(cylOuterRadiusEntry.get())
        cylInnerRadius = float(cylInnerRadiusEntry.get())
        cylLength = float(cylLengthEntry.get())
        # You can add your calculations for the cylindrical capacitor here

    voltage = float(voltageEntry.get())
    hasDielectric = dielecVar.get()
    if hasDielectric:
        coverage = coverageVar.get()
        # You can add your calculations for the dielectric here

    # Finally, display results or carry out desired operations

    if capacitorType == "Paralelo":
        drawCapacitor("Paralelo", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), length=float(lengthEntry.get()), width=float(widthEntry.get()))
    elif capacitorType == "Esférico":
        drawCapacitor("Esférico", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), outerRadius=float(outerRadiusEntry.get()), innerRadius=float(innerRadiusEntry.get()))
    elif capacitorType == "Cilíndrico":
        drawCapacitor("Cilíndrico", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), outerRadius=float(cylOuterRadiusEntry.get()), innerRadius=float(cylInnerRadiusEntry.get()), cylLength=float(cylLengthEntry.get()))

def updateInterface(typeVar, detailFrame, lengthLabel, lengthEntry, widthLabel, widthEntry, outerRadiusLabel, outerRadiusEntry, innerRadiusLabel, innerRadiusEntry, cylOuterRadiusLabel, cylOuterRadiusEntry, cylInnerRadiusLabel, cylInnerRadiusEntry, cylLengthLabel, cylLengthEntry):

    capacitorType = typeVar.get()
    for widget in detailFrame.winfo_children():
        widget.grid_forget()

    if capacitorType == "Paralelo":
        lengthLabel.grid(row=0, column=0)
        lengthEntry.grid(row=0, column=1)
        widthLabel.grid(row=1, column=0)
        widthEntry.grid(row=1, column=1)

    elif capacitorType == "Esférico":
        outerRadiusLabel.grid(row=0, column=0)
        outerRadiusEntry.grid(row=0, column=1)
        innerRadiusLabel.grid(row=1, column=0)
        innerRadiusEntry.grid(row=1, column=1)

    elif capacitorType == "Cilíndrico":
        cylOuterRadiusLabel.grid(row=0, column=0)
        cylOuterRadiusEntry.grid(row=0, column=1)
        cylInnerRadiusLabel.grid(row=1, column=0)
        cylInnerRadiusEntry.grid(row=1, column=1)
        cylLengthLabel.grid(row=2, column=0)
        cylLengthEntry.grid(row=2, column=1)

def drawCapacitor(capacitorType, canvas, isDielectric=False, coverage="Todo", **kwargs):
    fig, ax = plt.subplots(figsize=(5, 5))


    if capacitorType == "Paralelo":
        length = kwargs.get("length", 1)
        width = kwargs.get("width", 1)
        
        # Limitar el grosor de las placas a un máximo de 0.2
        width = min(0.3, width)
        
        # Espacio entre las placas
        space = 0.7
        
        # Coordenadas para las placas
        top_plate_y = length/2 + space/2
        bottom_plate_y = length/2 - width - space/2
        
        # Agregar las placas superior (roja) e inferior (azul)
        ax.add_patch(patches.Rectangle((0, top_plate_y), length, width, fill=True, color='red'))
        ax.add_patch(patches.Rectangle((0, bottom_plate_y), length, width, fill=True, color='blue'))
        
        # Verificar si se debe agregar el dieléctrico
        if isDielectric:
            if coverage == "Todo":
                ax.add_patch(patches.Rectangle((0, bottom_plate_y + width), length, space, fill=True, color='gray'))
            elif coverage == "Mitad":
                ax.add_patch(patches.Rectangle((0, bottom_plate_y + width), length/2, space, fill=True, color='gray'))

    elif capacitorType == "Esférico":
        outerRadius = kwargs.get("outerRadius", 1.3)
        innerRadius = kwargs.get("innerRadius", 0.9)
        
        # Grosor de las líneas para representar las placas
        line_width = 2
        
        # Agregar las placas exterior (rb) e interior (ra)
        ax.add_patch(patches.Circle((0, 0), outerRadius, fill=False, color='black', linewidth=line_width))
        ax.add_patch(patches.Circle((0, 0), innerRadius, fill=False, color='black', linewidth=line_width))
        
        if isDielectric:
            if coverage == "Todo":
                # Solo rellenar hasta el radio exterior, manteniendo el interior vacío
                ax.add_patch(patches.Circle((0, 0), outerRadius, fill=True, color='gray'))
                ax.add_patch(patches.Circle((0, 0), innerRadius, fill=True, color='white'))
            elif coverage == "Mitad":
                # Agregar cuña (wedge) para rellenar solo la mitad inferior entre rb y ra
                ax.add_patch(patches.Wedge(center=(0, 0), r=outerRadius, theta1=180, theta2=360, width=outerRadius-innerRadius, color='gray'))

    elif capacitorType == "Cilíndrico":
        outerRadius = kwargs.get("outerRadius", 1.3)
        innerRadius = kwargs.get("innerRadius", 0.9)
        
        # Grosor de las líneas para representar las placas
        line_width = 2
        
        # Agregar las placas exterior (rb) e interior (ra)
        ax.add_patch(patches.Circle((0, 0), outerRadius, fill=False, color='black', linewidth=line_width))
        ax.add_patch(patches.Circle((0, 0), innerRadius, fill=False, color='black', linewidth=line_width))
        
        if isDielectric:
            if coverage == "Todo":
                # Solo rellenar hasta el radio exterior, manteniendo el interior vacío
                ax.add_patch(patches.Circle((0, 0), outerRadius, fill=True, color='gray'))
                ax.add_patch(patches.Circle((0, 0), innerRadius, fill=True, color='white'))
            elif coverage == "Mitad":
                # Agregar cuña (wedge) para rellenar solo la mitad inferior entre rb y ra
                ax.add_patch(patches.Wedge(center=(0, 0), r=outerRadius, theta1=180, theta2=360, width=outerRadius-innerRadius, color='gray'))

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

    typeVar = ttk.Combobox(app, values=["Paralelo", "Esférico", "Cilíndrico"])
    typeVar.grid(row=1, column=1, pady=10)
    ttk.Label(app, text="Tipo de capacitor:").grid(row=1, column=0, pady=10, sticky=tk.W)

    detailFrame = ttk.Frame(app)
    detailFrame.grid(row=2, column=0, columnspan=2, pady=10)

    # Widgets para capacitor paralelo
    lengthLabel = ttk.Label(detailFrame, text="Largo (m):")
    lengthEntry = ttk.Entry(detailFrame)
    widthLabel = ttk.Label(detailFrame, text="Ancho (m):")
    widthEntry = ttk.Entry(detailFrame)

    # Widgets para capacitor esférico
    outerRadiusLabel = ttk.Label(detailFrame, text="Radio exterior (m):")
    outerRadiusEntry = ttk.Entry(detailFrame)
    innerRadiusLabel = ttk.Label(detailFrame, text="Radio interior (m):")
    innerRadiusEntry = ttk.Entry(detailFrame)

    # Widgets para capacitor cilíndrico
    cylOuterRadiusLabel = ttk.Label(detailFrame, text="Radio exterior (m):")
    cylOuterRadiusEntry = ttk.Entry(detailFrame)
    cylInnerRadiusLabel = ttk.Label(detailFrame, text="Radio interior (m):")
    cylInnerRadiusEntry = ttk.Entry(detailFrame)
    cylLengthLabel = ttk.Label(detailFrame, text="Largo (m):")
    cylLengthEntry = ttk.Entry(detailFrame)

    ttk.Label(app, text="Voltaje (V):").grid(row=3, column=0, pady=10, sticky=tk.W)
    voltageEntry = ttk.Entry(app)
    voltageEntry.grid(row=3, column=1, pady=10)

    dielecVar = tk.BooleanVar()

    coverageLabel = ttk.Label(app, text="Cobertura del dieléctrico:")
    coverageVar = ttk.Combobox(app, values=["Todo", "Mitad"])

    def mostrar_cobertura(*args):
        if dielecVar.get():
            coverageLabel.grid(row=6, column=0, pady=10, sticky=tk.W)
            coverageVar.grid(row=6, column=1, pady=10)
        else:
            coverageLabel.grid_forget()
            coverageVar.grid_forget()

    dielecVar.trace_add("write", mostrar_cobertura)
    ttk.Checkbutton(app, text="¿Usar dieléctrico?", variable=dielecVar).grid(row=5, column=0, columnspan=2, pady=10)

    canvas = tk.Canvas(app)
    canvas.grid(row=8, column=0, columnspan=2, pady=10)

    def combined_functions(event):
        updateInterface(typeVar, detailFrame, lengthLabel, lengthEntry, widthLabel, widthEntry, outerRadiusLabel, outerRadiusEntry, innerRadiusLabel, innerRadiusEntry, cylOuterRadiusLabel, cylOuterRadiusEntry, cylInnerRadiusLabel,  cylInnerRadiusEntry, cylLengthLabel,  cylLengthEntry)
        getData(typeVar, canvas, lengthEntry, widthEntry, outerRadiusEntry, innerRadiusEntry, cylOuterRadiusEntry,  cylInnerRadiusEntry,  cylLengthEntry, voltageEntry, dielecVar, coverageVar)
    
    typeVar.bind("<<ComboboxSelected>>", combined_functions)

    ttk.Button(app, text="Calcular", command=lambda: combined_functions(None)).grid(row=7, column=0, columnspan=2, pady=10)

    app.mainloop()

if __name__ == "__main__":
    main()