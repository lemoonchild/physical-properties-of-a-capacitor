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
import math
# ---------------------------------------------------------------------------

# Variables for all 3 figures
dielectricDistro = ""
entryVoltage = 0.0

# Important variables for parallel plates
platesArea = 0.0
platesDistance: 0.0

# Important variables for concentric spheres
smallRadius = 0.0
bigRadius = 0.0

# and cylinders
cylinderLength = 0.0

epsilonZero = 8.85e-12

dielectricConstant = 3.40

PI = 3.14159265359


def getData(typeVar, canvas, lengthEntry, widthEntry, platesDistanceEntry, outerRadiusEntry, innerRadiusEntry, cylOuterRadiusEntry, cylInnerRadiusEntry, cylLengthEntry, voltageEntry, dielecVar, coverageVar):
    capacitorType = typeVar.get()
    if capacitorType == "Paralelo":
        length = float(lengthEntry.get()) if lengthEntry.get() else 0.0
        width = float(widthEntry.get()) if widthEntry.get() else 0.0
        platesDistance = float(platesDistanceEntry.get()) if platesDistanceEntry.get() else 0.0
        # You can add your calculations for the parallel capacitor here
    elif capacitorType == "Spherical":
        outerRadius = float(outerRadiusEntry.get()) if outerRadiusEntry.get() else 0.0
        innerRadius = float(innerRadiusEntry.get()) if innerRadiusEntry.get() else 0.0
        # You can add your calculations for the spherical capacitor here
    elif capacitorType == "Cylindric":
        cylOuterRadius = float(cylOuterRadiusEntry.get()) if cylOuterRadiusEntry.get() else 0.0
        cylInnerRadius = float(cylInnerRadiusEntry.get()) if cylInnerRadiusEntry.get() else 0.0
        cylLength = float(cylLengthEntry.get()) if cylLengthEntry.get() else 0.0
        # You can add your calculations for the cylindrical capacitor here

    voltage = float(voltageEntry.get()) if voltageEntry.get() else 0.0
    hasDielectric = dielecVar.get()
    if hasDielectric:
        coverage = coverageVar.get()
        # You can add your calculations for the dielectric here

    # Finally, display results or carry out desired operations

    #if capacitorType == "Paralelo":
      #  drawCapacitor("Paralelo", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), length=float(lengthEntry.get()), width=float(widthEntry.get()))
   # elif capacitorType == "Spherical":
     #   drawCapacitor("Spherical", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), outerRadius=float(outerRadiusEntry.get()), innerRadius=float(innerRadiusEntry.get()))
    #elif capacitorType == "Cylindric":
    #    drawCapacitor("Cylindric", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), outerRadius=float(cylOuterRadiusEntry.get()), innerRadius=float(cylInnerRadiusEntry.get()), cylLength=float(cylLengthEntry.get()))

def updateInterface(typeVar, detailFrame, lengthLabel, lengthEntry, widthLabel, platesDistanceLabel, platesDistanceEntry, widthEntry, outerRadiusLabel, outerRadiusEntry, innerRadiusLabel, innerRadiusEntry, cylOuterRadiusLabel, cylOuterRadiusEntry, cylInnerRadiusLabel, cylInnerRadiusEntry, cylLengthLabel, cylLengthEntry):

    capacitorType = typeVar.get()
    for widget in detailFrame.winfo_children():
        widget.grid_forget()

    if capacitorType == "Paralelo":
        lengthLabel.grid(row=0, column=0)
        lengthEntry.grid(row=0, column=1)
        widthLabel.grid(row=1, column=0)
        widthEntry.grid(row=1, column=1)
        platesDistanceLabel.grid(row=2, column=0)   
        platesDistanceEntry.grid(row=2, column=1)

    elif capacitorType == "Spherical":
        outerRadiusLabel.grid(row=0, column=0)
        outerRadiusEntry.grid(row=0, column=1)
        innerRadiusLabel.grid(row=1, column=0)
        innerRadiusEntry.grid(row=1, column=1)

    elif capacitorType == "Cylindric":
        cylOuterRadiusLabel.grid(row=0, column=0)
        cylOuterRadiusEntry.grid(row=0, column=1)
        cylInnerRadiusLabel.grid(row=1, column=0)
        cylInnerRadiusEntry.grid(row=1, column=1)
        cylLengthLabel.grid(row=2, column=0)
        cylLengthEntry.grid(row=2, column=1)

def drawCapacitor(capacitorType, canvas, isDielectric=False, coverage="Full", **kwargs):
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
            if coverage == "Full":
                ax.add_patch(patches.Rectangle((0, bottom_plate_y + width), length, space, fill=True, color='gray'))
            elif coverage == "Half":
                ax.add_patch(patches.Rectangle((0, bottom_plate_y + width), length/2, space, fill=True, color='gray'))

    elif capacitorType == "Spherical":
        outerRadius = kwargs.get("outerRadius", 1.3)
        innerRadius = kwargs.get("innerRadius", 0.9)
        
        # Grosor de las líneas para representar las placas
        line_width = 2
        
        # Agregar las placas exterior (rb) e interior (ra)
        ax.add_patch(patches.Circle((0, 0), outerRadius, fill=False, color='black', linewidth=line_width))
        ax.add_patch(patches.Circle((0, 0), innerRadius, fill=False, color='black', linewidth=line_width))
        
        if isDielectric:
            if coverage == "Full":
                # Solo rellenar hasta el radio exterior, manteniendo el interior vacío
                ax.add_patch(patches.Circle((0, 0), outerRadius, fill=True, color='gray'))
                ax.add_patch(patches.Circle((0, 0), innerRadius, fill=True, color='white'))
            elif coverage == "Half":
                # Agregar cuña (wedge) para rellenar solo la Half inferior entre rb y ra
                ax.add_patch(patches.Wedge(center=(0, 0), r=outerRadius, theta1=180, theta2=360, width=outerRadius-innerRadius, color='gray'))

    elif capacitorType == "Cylindric":
        outerRadius = kwargs.get("outerRadius", 1.3)
        innerRadius = kwargs.get("innerRadius", 0.9)
        
        # Grosor de las líneas para representar las placas
        line_width = 2
        
        # Agregar las placas exterior (rb) e interior (ra)
        ax.add_patch(patches.Circle((0, 0), outerRadius, fill=False, color='black', linewidth=line_width))
        ax.add_patch(patches.Circle((0, 0), innerRadius, fill=False, color='black', linewidth=line_width))
        
        if isDielectric:
            if coverage == "Full":
                # Solo rellenar hasta el radio exterior, manteniendo el interior vacío
                ax.add_patch(patches.Circle((0, 0), outerRadius, fill=True, color='gray'))
                ax.add_patch(patches.Circle((0, 0), innerRadius, fill=True, color='white'))
            elif coverage == "Half":
                # Agregar cuña (wedge) para rellenar solo la Half inferior entre rb y ra
                ax.add_patch(patches.Wedge(center=(0, 0), r=outerRadius, theta1=180, theta2=360, width=outerRadius-innerRadius, color='gray'))

    ax.set_aspect('equal')
    ax.autoscale_view()
    plt.axis('off')

    for widget in canvas.winfo_children():
        widget.destroy()

    chart = FigureCanvasTkAgg(fig, canvas)
    chart.get_tk_widget().pack()

    plt.show()


def calculateParallelPlates(plateLength, plateWidth, platesD, dielectricDist,  entVoltage):
    
    initialCapacitance = (epsilonZero * plateLength * plateWidth)/(platesD)

    
    if(dielectricDist == "Half"):
        initialCapacitanceHalf = 0.5 * initialCapacitance
        dielectricCapacitance = initialCapacitanceHalf * dielectricConstant
        equivalentCapacitance = initialCapacitanceHalf + dielectricCapacitance
        capacitorCharge = equivalentCapacitance * entVoltage
        capacitorEnergy = (0.5) * equivalentCapacitance * (entVoltage*entVoltage)

        freeChargeAir = (capacitorCharge/(1+dielectricConstant))*(1/(plateLength*plateWidth))
        freeChargeDielectric = freeChargeAir * dielectricConstant
        boundChargeDielectric = freeChargeDielectric * (1-(1/dielectricConstant))

        print("\n\nCapacitancia Equivalente: " , equivalentCapacitance , "Carga del Capacitor: " , capacitorCharge , ", Energia del Capacitor" , capacitorEnergy)
        print("Carga Libre Aire: " , freeChargeAir , ", Carga Libre Dielectrico: " , freeChargeDielectric , "Carga Ligada Dielectrico: " , boundChargeDielectric)

    elif(dielectricDist == "Full"):
        dielectricCapacitance = initialCapacitance * dielectricConstant
        capacitorCharge = dielectricCapacitance * entVoltage
        capacitorEnergy = (0.5) * dielectricCapacitance * (entVoltage*entVoltage)

        freeChargeDielectric = dielectricConstant*(capacitorCharge/(1+dielectricConstant))*(1/(plateLength*plateWidth))
        boundChargeDielectric = freeChargeDielectric * (1-(1/dielectricConstant))
        
        print("\n\nCapacitancia Equivalente: " , dielectricCapacitance , "Carga del Capacitor: " , capacitorCharge , ", Energia del Capacitor" , capacitorEnergy)
        print("Carga Libre Dielectrico: " , freeChargeDielectric , "Carga Ligada Dielectrico: " , boundChargeDielectric)


    else:
        capacitorCharge = initialCapacitance * entVoltage
        capacitorEnergy = (0.5) * initialCapacitance * (entVoltage*entVoltage)
        print("\n\nCapacitancia Equivalente: ", initialCapacitance, ", Carga del Capacitor: ", capacitorCharge, ", Energia del Capacitor: ", capacitorEnergy)
    

def calculateConcentricSpheres(smallRad, bigRad, dielectricDist, entVoltage):

    initialCapacitance = 4*PI*epsilonZero*((smallRad*bigRad)/(bigRad - smallRad))

    
    if(dielectricDist == "Half"):
        initialCapacitanceHalf = 0.5 * initialCapacitance
        dielectricCapacitance = initialCapacitanceHalf * dielectricConstant
        equivalentCapacitance = initialCapacitanceHalf + dielectricCapacitance
        capacitorCharge = equivalentCapacitance * entVoltage
        capacitorEnergy = (0.5) * equivalentCapacitance * (entVoltage*entVoltage)
        print(equivalentCapacitance, capacitorCharge, capacitorEnergy)

        freeChargeAir_smallRadius = (capacitorCharge/(1+dielectricConstant))*(1/(2*PI*smallRad*smallRad))
        freeChargeAir_bigRadius = (capacitorCharge/(1+dielectricConstant))*(1/(2*PI*bigRad*bigRad))
        freeChargeDielectric_smallRadius = freeChargeAir_smallRadius * dielectricConstant
        freeChargeDielectric_bigRadius = freeChargeAir_bigRadius * dielectricConstant

        boundChargeDielectric_smallRadius = freeChargeDielectric_smallRadius * (1-(1/dielectricConstant))
        boundChargeDielectric_bigRadius = freeChargeDielectric_bigRadius * (1-(1/dielectricConstant))
        
        print("\n\nCapacitancia Equivalente", equivalentCapacitance, "Carga del Capacitor", capacitorCharge, "Energia Almacenada", capacitorEnergy)
        print("Carga Libre Aire Ra", freeChargeAir_smallRadius, "Carga Libre Aire Rb", freeChargeAir_bigRadius, "Carga Libre Dielectrico Ra", freeChargeDielectric_smallRadius)
        print("Carga Libre Dielectric Rb", freeChargeDielectric_bigRadius, "Carga Ligada Dielectrico Ra", boundChargeDielectric_smallRadius, "Carga Ligada Dielectrico Rb", boundChargeDielectric_bigRadius)

    elif(dielectricDist == "Full"):
        dielectricCapacitance = initialCapacitance * dielectricConstant
        capacitorCharge = dielectricCapacitance * entVoltage
        capacitorEnergy = (0.5) * dielectricCapacitance * (entVoltage*entVoltage)
        print(dielectricCapacitance, capacitorCharge, capacitorEnergy)

        freeChargeAir_smallRadius = (capacitorCharge/(1+dielectricConstant))*(1/(4*PI*smallRad*smallRad))
        freeChargeAir_bigRadius = (capacitorCharge/(1+dielectricConstant))*(1/(4*PI*bigRad*bigRad))
        freeChargeDielectric_smallRadius = freeChargeAir_smallRadius * dielectricConstant
        freeChargeDielectric_bigRadius = freeChargeAir_bigRadius * dielectricConstant

        boundChargeDielectric_smallRadius = freeChargeDielectric_smallRadius * (1-(1/dielectricConstant))
        boundChargeDielectric_bigRadius = freeChargeDielectric_bigRadius * (1-(1/dielectricConstant))

        print("\n\nCapacitancia Equivalente", dielectricCapacitance, "Carga del Capacitor", capacitorCharge, "Energia Almacenada", capacitorEnergy)
        print("Carga Libre Dielectrico Ra", freeChargeDielectric_smallRadius, "Carga Libre Dielectrico Rb", freeChargeDielectric_bigRadius)
        print("Carga Ligada Dielectrico Ra", boundChargeDielectric_smallRadius, "Carga Ligada Dielectrico Rb", boundChargeDielectric_bigRadius)



    else:
        capacitorCharge = initialCapacitance * entVoltage
        capacitorEnergy = (0.5) * initialCapacitance * (entVoltage*entVoltage)
        print("\n\nCapacitancia Equivalente", initialCapacitance, "Carga del Capacitor", capacitorCharge, "Energia Almacenada", capacitorEnergy)

def calculateCylinder(innerRad, outerRad, cylLength, dielectricDist, entVoltage):
    
    initialCapacitance = (2*PI*epsilonZero*cylLength)/(math.log(outerRad/innerRad))

    
    if(dielectricDist == "Half"):
        initialCapacitanceHalf = 0.5 * initialCapacitance
        dielectricCapacitance = initialCapacitanceHalf * dielectricConstant
        equivalentCapacitance = initialCapacitanceHalf + dielectricCapacitance
        capacitorCharge = equivalentCapacitance * entVoltage
        capacitorEnergy = (0.5) * equivalentCapacitance * (entVoltage*entVoltage)

        freeChargeAir_smallRadius = (capacitorCharge/(1+dielectricConstant))*(1/(PI*innerRad*cylLength))
        freeChargeAir_bigRadius = (capacitorCharge/(1+dielectricConstant))*(1/(PI*outerRad*cylLength))
        freeChargeDielectric_smallRadius = freeChargeAir_smallRadius * dielectricConstant
        freeChargeDielectric_bigRadius = freeChargeAir_bigRadius * dielectricConstant

        boundChargeDielectric_smallRadius = freeChargeDielectric_smallRadius * (1-(1/dielectricConstant))
        boundChargeDielectric_bigRadius = freeChargeDielectric_bigRadius * (1-(1/dielectricConstant))
        
        print("\n\nCapacitancia Equivalente", equivalentCapacitance, "Carga del Capacitor", capacitorCharge, "Energia del Capacitor", capacitorEnergy)
        print("Carga Libre Aire Ra", freeChargeAir_smallRadius, "Carga Libre Aire Rb", freeChargeAir_bigRadius, "Carga Libre Dielectrico Ra", freeChargeDielectric_smallRadius)
        print("Carga Libre Dielectric Rb", freeChargeDielectric_bigRadius, "Carga Ligada Dielectrico Ra", boundChargeDielectric_smallRadius, "Carga Ligada Dielectrico Rb", boundChargeDielectric_bigRadius)


    elif(dielectricDist == "Full"):
        dielectricCapacitance = initialCapacitance * dielectricConstant
        capacitorCharge = dielectricCapacitance * entVoltage
        capacitorEnergy = (0.5) * dielectricCapacitance * (entVoltage*entVoltage)
        print(dielectricCapacitance, capacitorCharge, capacitorEnergy)

        freeChargeAir_smallRadius = (capacitorCharge/(1+dielectricConstant))*(1/(2*PI*innerRad*cylLength))
        freeChargeAir_bigRadius = (capacitorCharge/(1+dielectricConstant))*(1/(2*PI*outerRad*cylLength))
        freeChargeDielectric_smallRadius = freeChargeAir_smallRadius * dielectricConstant
        freeChargeDielectric_bigRadius = freeChargeAir_bigRadius * dielectricConstant
        boundChargeDielectric_smallRadius = freeChargeDielectric_smallRadius * (1-(1/dielectricConstant))
        boundChargeDielectric_bigRadius = freeChargeDielectric_bigRadius * (1-(1/dielectricConstant))

        print("\n\nCapacitancia Equivalente", dielectricCapacitance, "Carga del Capacitor", capacitorCharge, "Energia del Capacitor", capacitorEnergy)
        print("Carga Libre Dielectrico Ra", freeChargeDielectric_smallRadius, "Carga Libre Dielectrico Rb", freeChargeDielectric_bigRadius)
        print("Carga Ligada Dielectrico Ra", boundChargeDielectric_smallRadius, "Carga Ligada Dielectrico Rb", boundChargeDielectric_bigRadius)

    else:
        capacitorCharge = initialCapacitance * entVoltage
        capacitorEnergy = (0.5) * initialCapacitance * (entVoltage*entVoltage)
        print("\n\nCapacitancia Equivalente", initialCapacitance, "Carga del Capacitor", capacitorCharge, "Energia Almacenada", capacitorEnergy)

    


def main():

    app = tk.Tk()
    app.title("Calculadora de Capacitores")

    # Centrar el título y hacerlo negrita
    ttk.Label(app, text="Calculadora de Capacitores", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

    typeVar = ttk.Combobox(app, values=["Paralelo", "Spherical", "Cylindric"])
    typeVar.grid(row=1, column=1, pady=10)
    ttk.Label(app, text="Tipo de capacitor:").grid(row=1, column=0, pady=10, sticky=tk.W)

    detailFrame = ttk.Frame(app)
    detailFrame.grid(row=2, column=0, columnspan=2, pady=10)

    # Widgets para capacitor paralelo
    lengthLabel = ttk.Label(detailFrame, text="Largo (m):")
    lengthEntry = ttk.Entry(detailFrame)
    widthLabel = ttk.Label(detailFrame, text="Ancho (m):")
    widthEntry = ttk.Entry(detailFrame)
    platesDistanceLabel = ttk.Label(detailFrame, text="Distancia entre placas (m):")
    platesDistanceEntry = ttk.Entry(detailFrame)

    # Widgets para capacitor Spherical
    outerRadiusLabel = ttk.Label(detailFrame, text="Radio exterior (m):")
    outerRadiusEntry = ttk.Entry(detailFrame)
    innerRadiusLabel = ttk.Label(detailFrame, text="Radio interior (m):")
    innerRadiusEntry = ttk.Entry(detailFrame)

    # Widgets para capacitor Cylindric
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
    coverageVar = ttk.Combobox(app, values=["Full", "Half"])

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
        updateInterface(typeVar, detailFrame, lengthLabel, lengthEntry, widthLabel, platesDistanceLabel, platesDistanceEntry, widthEntry, outerRadiusLabel, outerRadiusEntry, innerRadiusLabel, innerRadiusEntry, cylOuterRadiusLabel, cylOuterRadiusEntry, cylInnerRadiusLabel,  cylInnerRadiusEntry, cylLengthLabel,  cylLengthEntry)
        getData(typeVar, canvas, lengthEntry, widthEntry, outerRadiusEntry, platesDistanceEntry, innerRadiusEntry, cylOuterRadiusEntry,  cylInnerRadiusEntry,  cylLengthEntry, voltageEntry, dielecVar, coverageVar)
        
        if typeVar.get() == "Paralelo":
            plateLength = float(lengthEntry.get()) if lengthEntry.get() else 0.0
            plateWidth = float(widthEntry.get()) if widthEntry.get() else 0.0
            platesD = float(platesDistanceEntry.get()) if platesDistanceEntry.get() else 0.0
            dielectricDist = "" if not dielecVar.get() else coverageVar.get()
            entVoltage = float(voltageEntry.get())
            calculateParallelPlates(plateLength, plateWidth, platesD, dielectricDist, entVoltage)
            drawCapacitor("Paralelo", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), length=float(lengthEntry.get()), width=float(widthEntry.get()))


        elif typeVar.get() == "Spherical":
            bigR = float(outerRadiusEntry.get()) if outerRadiusEntry.get() else 0.0
            smallR = float(innerRadiusEntry.get()) if innerRadiusEntry.get() else 0.0
            dielectricDist = "" if not dielecVar.get() else coverageVar.get()
            entVoltage = float(voltageEntry.get())
            calculateConcentricSpheres(smallR, bigR, dielectricDist, entVoltage)
            drawCapacitor("Spherical", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), outerRadius=float(outerRadiusEntry.get()), innerRadius=float(innerRadiusEntry.get()))

        elif typeVar.get() == "Cylindric":
            oRadius = float(cylOuterRadiusEntry.get()) if cylOuterRadiusEntry.get() else 0.0
            iRadius = float(cylInnerRadiusEntry.get()) if cylInnerRadiusEntry.get() else 0.0
            cylLength = float(cylLengthEntry.get()) if cylLengthEntry.get() else 0.0
            dielectricDist = "" if not dielecVar.get() else coverageVar.get()
            entVoltage = float(voltageEntry.get())
            calculateCylinder(iRadius, oRadius, cylLength, dielectricDist, entVoltage)
            drawCapacitor("Cylindric", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), outerRadius=float(cylOuterRadiusEntry.get()), innerRadius=float(cylInnerRadiusEntry.get()), cylLength=float(cylLengthEntry.get()))
        
        
    
    typeVar.bind("<<ComboboxSelected>>", combined_functions)

    ttk.Button(app, text="Calcular", command=lambda: combined_functions(None)).grid(row=7, column=0, columnspan=2, pady=10)

    app.mainloop()

if __name__ == "__main__":
    main()