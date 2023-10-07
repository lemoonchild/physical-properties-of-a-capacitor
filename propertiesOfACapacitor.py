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
from scipy import constants

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

epsilonZero = constants.epsilon_0

dielectricConstant = 3.40

PI = math.pi


def getData(typeVar, canvas, lengthEntry, widthEntry, platesDistanceEntry, outerRadiusEntry, innerRadiusEntry, cylOuterRadiusEntry, cylInnerRadiusEntry, cylLengthEntry, voltageEntry, dielecVar, coverageVar):
    capacitorType = typeVar.get()
    if capacitorType == "Parallel":
        length = float(lengthEntry.get()) if lengthEntry.get() else 0.0
        width = float(widthEntry.get()) if widthEntry.get() else 0.0
        platesDistance = float(platesDistanceEntry.get()) if platesDistanceEntry.get() else 0.0

    elif capacitorType == "Spherical":
        outerRadius = float(outerRadiusEntry.get()) if outerRadiusEntry.get() else 0.0
        innerRadius = float(innerRadiusEntry.get()) if innerRadiusEntry.get() else 0.0

    elif capacitorType == "Cylindric":
        cylOuterRadius = float(cylOuterRadiusEntry.get()) if cylOuterRadiusEntry.get() else 0.0
        cylInnerRadius = float(cylInnerRadiusEntry.get()) if cylInnerRadiusEntry.get() else 0.0
        cylLength = float(cylLengthEntry.get()) if cylLengthEntry.get() else 0.0

    voltage = float(voltageEntry.get()) if voltageEntry.get() else 0.0
    hasDielectric = dielecVar.get()
    if hasDielectric:
        coverage = coverageVar.get()

def updateInterface(typeVar, detailFrame, lengthLabel, lengthEntry, widthLabel, platesDistanceLabel, platesDistanceEntry, widthEntry, outerRadiusLabel, outerRadiusEntry, innerRadiusLabel, innerRadiusEntry, cylOuterRadiusLabel, cylOuterRadiusEntry, cylInnerRadiusLabel, cylInnerRadiusEntry, cylLengthLabel, cylLengthEntry):

    capacitorType = typeVar.get()
    for widget in detailFrame.winfo_children():
        widget.grid_forget()

    if capacitorType == "Parallel":
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

    for widget in canvas.winfo_children():
        widget.destroy()

    fig = plt.Figure(figsize=(5,5))
    ax = fig.add_subplot(111)

    if capacitorType == "Parallel":
        length = kwargs.get("length", 1)
        width = kwargs.get("width", 1)
        
        width = min(0.3, width)
        
        space = 0.7
        
        top_plate_y = length/2 + space/2
        bottom_plate_y = length/2 - width - space/2
        
        ax.add_patch(patches.Rectangle((0, top_plate_y), length, width, fill=True, color='red'))
        ax.add_patch(patches.Rectangle((0, bottom_plate_y), length, width, fill=True, color='blue'))
        
        if isDielectric:
            if coverage == "Full":
                ax.add_patch(patches.Rectangle((0, bottom_plate_y + width), length, space, fill=True, color='gray'))
            elif coverage == "Half":
                ax.add_patch(patches.Rectangle((0, bottom_plate_y + width), length/2, space, fill=True, color='gray'))

    elif capacitorType == "Spherical":
        outerRadius = kwargs.get("outerRadius", 1.3)
        innerRadius = kwargs.get("innerRadius", 0.9)
        
        line_width = 2
        
        ax.add_patch(patches.Circle((0, 0), outerRadius, fill=False, color='black', linewidth=line_width))
        ax.add_patch(patches.Circle((0, 0), innerRadius, fill=False, color='black', linewidth=line_width))
        
        if isDielectric:
            if coverage == "Full":
                ax.add_patch(patches.Circle((0, 0), outerRadius, fill=True, color='gray'))
                ax.add_patch(patches.Circle((0, 0), innerRadius, fill=True, color='white'))
            elif coverage == "Half":
                ax.add_patch(patches.Wedge(center=(0, 0), r=outerRadius, theta1=180, theta2=360, width=outerRadius-innerRadius, color='gray'))

    elif capacitorType == "Cylindric":
        outerRadius = kwargs.get("outerRadius", 1.3)
        innerRadius = kwargs.get("innerRadius", 0.9)
        
        line_width = 2
        
        ax.add_patch(patches.Circle((0, 0), outerRadius, fill=False, color='black', linewidth=line_width))
        ax.add_patch(patches.Circle((0, 0), innerRadius, fill=False, color='black', linewidth=line_width))
        
        if isDielectric:
            if coverage == "Full":
                ax.add_patch(patches.Circle((0, 0), outerRadius, fill=True, color='gray'))
                ax.add_patch(patches.Circle((0, 0), innerRadius, fill=True, color='white'))
            elif coverage == "Half":
                ax.add_patch(patches.Wedge(center=(0, 0), r=outerRadius, theta1=180, theta2=360, width=outerRadius-innerRadius, color='gray'))

    ax.set_aspect('equal')
    ax.autoscale_view()
    plt.axis('off')

    chart = FigureCanvasTkAgg(fig, canvas)
    chart.get_tk_widget().grid()
    
    chart.draw()

def calculateParallelPlates(plateLength, plateWidth, platesD, dielectricDist,  entVoltage):
    
    initialCapacitance = (epsilonZero * (plateLength) * plateWidth)/(platesD)
    capacitorCharge = initialCapacitance * entVoltage

    if(dielectricDist == "Half"):
        initialCapacitanceHalf = (epsilonZero * (plateLength/2) * plateWidth)/(platesD)
        dielectricCapacitance = initialCapacitanceHalf * dielectricConstant
        equivalentCapacitance = initialCapacitanceHalf + dielectricCapacitance
        capacitorEnergy = ((entVoltage**2)*initialCapacitance/2)/2 + ((((entVoltage/dielectricConstant)**2)*equivalentCapacitance/2))/2
        freeChargeAir = (capacitorCharge)/((dielectricConstant+1)*(plateLength)*plateWidth) 
        freeChargeDielectric = freeChargeAir * dielectricConstant
        boundChargeDielectric = freeChargeDielectric * (1-(1/dielectricConstant))
        
        resultsLabel.config(text = "Capacitancia Equivalente: {} \nCarga del Capacitor: {} \nEnergia del Capacitor {}\nCarga Libre Aire: {} \nCarga Libre Dielectrico: {} \nCarga Ligada Dielectrico: {}\n".format(equivalentCapacitance, capacitorCharge, capacitorEnergy, freeChargeAir, freeChargeDielectric, boundChargeDielectric))

    elif(dielectricDist == "Full"):
        dielectricCapacitance = initialCapacitance * dielectricConstant
        capacitorEnergy = (0.5*dielectricCapacitance*(entVoltage/dielectricConstant)**2)
        freeChargeDielectric = (capacitorCharge)/(plateLength*plateWidth)
        boundChargeDielectric = freeChargeDielectric * (1-(1/dielectricConstant))

        resultsLabel.config(text = "Capacitancia Equivalente: {} \nCarga del Capacitor: {} \nEnergia del Capacitor {}\nCarga Libre Dielectrico: {} \nCarga Ligada Dielectrico: {}\n".format(dielectricCapacitance, capacitorCharge, capacitorEnergy,freeChargeDielectric, boundChargeDielectric))
    else:
        capacitorEnergy = (0.5) * initialCapacitance * (entVoltage*entVoltage)
        resultsLabel.config(text = "Capacitancia Equivalente: {}\n Carga del Capacitor: {} \nEnergia del Capacitor: {}\n".format(initialCapacitance, capacitorCharge, capacitorEnergy))


def calculateConcentricSpheres(smallRad, bigRad, dielectricDist, entVoltage):

    initialCapacitance = 4*PI*epsilonZero*((smallRad*bigRad)/(bigRad - smallRad))
    capacitorCharge = initialCapacitance * entVoltage


    if(dielectricDist == "Half"):
        initialCapacitanceHalf = 0.5 * initialCapacitance
        dielectricCapacitance = initialCapacitanceHalf * dielectricConstant
        equivalentCapacitance = initialCapacitanceHalf + dielectricCapacitance
        capacitorEnergy = ((entVoltage**2)*initialCapacitance/2)/2 + ((((entVoltage/dielectricConstant)**2)*equivalentCapacitance/2))/2

        freeChargeAir_smallRadius = (capacitorCharge/(1+dielectricConstant))*(1/(2*PI*smallRad*smallRad))
        freeChargeAir_bigRadius = (capacitorCharge/(1+dielectricConstant))*(1/(2*PI*bigRad*bigRad))
        freeChargeDielectric_smallRadius = freeChargeAir_smallRadius * dielectricConstant
        freeChargeDielectric_bigRadius = freeChargeAir_bigRadius * dielectricConstant

        boundChargeDielectric_smallRadius = freeChargeDielectric_smallRadius * (1-(1/dielectricConstant))
        boundChargeDielectric_bigRadius = freeChargeDielectric_bigRadius * (1-(1/dielectricConstant))

        resultsLabel.config(text ="Capacitancia Equivalente: {} \nCarga del Capacitor: {} \nEnergia del Capacitor {}\nCarga Libre Aire Ra: {} \nCarga Libre Aire Rb: {} \nCarga Libre Dielectrico Ra: {} \nCarga Libre Dielectrico Rb: {} \nCarga Ligada Dielectrico Ra: {} \nCarga Ligada Dielectrico Rb: {}\n".format(equivalentCapacitance, capacitorCharge, capacitorEnergy, freeChargeAir_smallRadius, freeChargeAir_bigRadius, freeChargeDielectric_smallRadius, freeChargeDielectric_bigRadius, boundChargeDielectric_smallRadius, boundChargeDielectric_bigRadius))

    elif(dielectricDist == "Full"):
        dielectricCapacitance = initialCapacitance * dielectricConstant
        capacitorEnergy = (0.5*dielectricCapacitance*(entVoltage/dielectricConstant)**2)

        freeChargeDielectric_smallRadius = (capacitorCharge/(4*PI*smallRad*smallRad))
        freeChargeDielectric_bigRadius = (capacitorCharge/(4*PI*bigRad*bigRad))

        boundChargeDielectric_smallRadius = freeChargeDielectric_smallRadius * (1-(1/dielectricConstant))
        boundChargeDielectric_bigRadius = freeChargeDielectric_bigRadius * (1-(1/dielectricConstant))

        resultsLabel.config(text ="Capacitancia Equivalente: {} \nCarga del Capacitor: {} \nEnergia del Capacitor {}\nCarga Libre Dielectrico Ra: {} \nCarga Libre Dielectrico Rb: {} \nCarga Ligada Dielectrico Ra: {} \nCarga Ligada Dielectrico Rb: {}\n".format(dielectricCapacitance, capacitorCharge, capacitorEnergy, freeChargeDielectric_smallRadius, freeChargeDielectric_bigRadius, boundChargeDielectric_smallRadius, boundChargeDielectric_bigRadius))

    else:
        capacitorEnergy = (0.5) * initialCapacitance * (entVoltage*entVoltage)
        resultsLabel.config(text ="\n\nCapacitancia Equivalente: {}\nCarga del Capacitor: {} \nEnergia del Capacitor: {}\n".format(initialCapacitance, capacitorCharge, capacitorEnergy))


def calculateCylinder(innerRad, outerRad, cylLength, dielectricDist, entVoltage):

    initialCapacitance = (2*PI*epsilonZero*cylLength)/(math.log(outerRad/innerRad))
    capacitorCharge = initialCapacitance * entVoltage

    
    if(dielectricDist == "Half"):
        initialCapacitanceHalf = 0.5 * initialCapacitance
        dielectricCapacitance = initialCapacitanceHalf * dielectricConstant
        equivalentCapacitance = initialCapacitanceHalf + dielectricCapacitance
        capacitorEnergy = ((entVoltage**2)*initialCapacitance/2)/2 + ((((entVoltage/dielectricConstant)**2)*equivalentCapacitance/2))/2

        freeChargeAir_smallRadius = (capacitorCharge/(1+dielectricConstant))*(1/(PI*innerRad*cylLength))
        freeChargeAir_bigRadius = (capacitorCharge/(1+dielectricConstant))*(1/(PI*outerRad*cylLength))
        freeChargeDielectric_smallRadius = freeChargeAir_smallRadius * dielectricConstant
        freeChargeDielectric_bigRadius = freeChargeAir_bigRadius * dielectricConstant

        boundChargeDielectric_smallRadius = freeChargeDielectric_smallRadius * (1-(1/dielectricConstant))
        boundChargeDielectric_bigRadius = freeChargeDielectric_bigRadius * (1-(1/dielectricConstant))
        
        resultsLabel.config(text ="Capacitancia Equivalente: {} \nCarga del Capacitor: {} \nEnergia del Capacitor: {}\nCarga Libre Aire Ra: {} \nCarga Libre Aire Rb: {} \nCarga Libre Dielectrico Ra: {} \nCarga Libre Dielectrico Rb: {} \nCarga Ligada Dielectrico Ra: {} \nCarga Ligada Dielectrico Rb: {}\n".format(equivalentCapacitance, capacitorCharge, capacitorEnergy, freeChargeAir_smallRadius, freeChargeAir_bigRadius, freeChargeDielectric_smallRadius, freeChargeDielectric_bigRadius, boundChargeDielectric_smallRadius, boundChargeDielectric_bigRadius))

    elif(dielectricDist == "Full"):
        dielectricCapacitance = initialCapacitance * dielectricConstant
        capacitorEnergy = (0.5*dielectricCapacitance*(entVoltage/dielectricConstant)**2)

        freeChargeDielectric_smallRadius = (capacitorCharge/(2*PI*innerRad*cylLength))
        freeChargeDielectric_bigRadius = (capacitorCharge/(2*PI*outerRad*cylLength))
        boundChargeDielectric_smallRadius = freeChargeDielectric_smallRadius * (1-(1/dielectricConstant))
        boundChargeDielectric_bigRadius = freeChargeDielectric_bigRadius * (1-(1/dielectricConstant))

        resultsLabel.config(text ="Capacitancia Equivalente: {} \nCarga del Capacitor: {} \nEnergia del Capacitor: {}\nCarga Libre Dielectrico Ra: {} \nCarga Libre Dielectrico Rb: {} \nCarga Ligada Dielectrico Ra: {} \nCarga Ligada Dielectrico Rb: {}\n".format(dielectricCapacitance, capacitorCharge, capacitorEnergy, freeChargeDielectric_smallRadius, freeChargeDielectric_bigRadius, boundChargeDielectric_smallRadius, boundChargeDielectric_bigRadius))

    else:
        capacitorEnergy = (0.5) * initialCapacitance * (entVoltage*entVoltage)
        resultsLabel.config(text ="\n\nCapacitancia Equivalente: {} \nCarga del Capacitor: {} \nEnergia Almacenada: {}\n".format(initialCapacitance, capacitorCharge, capacitorEnergy))


def main():

    global resultsLabel

    content_frame = tk.Tk()
    content_frame.title("Calculadora de Capacitores")

    mainframe = ttk.Frame(content_frame)
    mainframe.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(mainframe)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(mainframe, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    content_frame = ttk.Frame(canvas)
    canvas.create_window((0,0), window=content_frame, anchor=tk.NW)

    # Centrar el título y hacerlo negrita
    ttk.Label(content_frame, text="Calculadora de Capacitores", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

    typeVar = ttk.Combobox(content_frame, values=["Parallel", "Spherical", "Cylindric"])
    typeVar.grid(row=1, column=1, pady=10)
    ttk.Label(content_frame, text="Tipo de capacitor:").grid(row=1, column=0, pady=10, sticky=tk.W)

    detailFrame = ttk.Frame(content_frame)
    detailFrame.grid(row=2, column=0, columnspan=2, pady=10)

    # Widgets para capacitor Parallel
    lengthLabel = ttk.Label(detailFrame, text="Largo de las placas (m):")
    lengthEntry = ttk.Entry(detailFrame)
    widthLabel = ttk.Label(detailFrame, text="Ancho de las placas (m):")
    widthEntry = ttk.Entry(detailFrame)
    platesDistanceLabel = ttk.Label(detailFrame, text="Distancia entre placas (m):")
    platesDistanceEntry = ttk.Entry(detailFrame)

    # Widgets para capacitor Spherical
    outerRadiusLabel = ttk.Label(detailFrame, text="Radio exterior (A) (m):")
    outerRadiusEntry = ttk.Entry(detailFrame)
    innerRadiusLabel = ttk.Label(detailFrame, text="Radio interior (B) (m):")
    innerRadiusEntry = ttk.Entry(detailFrame)

    # Widgets para capacitor Cylindric
    cylOuterRadiusLabel = ttk.Label(detailFrame, text="Radio exterior (A) (m):")
    cylOuterRadiusEntry = ttk.Entry(detailFrame)
    cylInnerRadiusLabel = ttk.Label(detailFrame, text="Radio interior (B) (m):")
    cylInnerRadiusEntry = ttk.Entry(detailFrame)
    cylLengthLabel = ttk.Label(detailFrame, text="Largo del cilindro (m):")
    cylLengthEntry = ttk.Entry(detailFrame)

    ttk.Label(content_frame, text="Voltaje a utilizar (V):").grid(row=3, column=0, pady=10, sticky=tk.W)
    voltageEntry = ttk.Entry(content_frame)
    voltageEntry.grid(row=3, column=1, pady=10)

    dielecVar = tk.BooleanVar()

    coverageLabel = ttk.Label(content_frame, text="Cobertura del dieléctrico:")
    coverageVar = ttk.Combobox(content_frame, values=["Full", "Half"])

    def mostrar_cobertura(*args):
        if dielecVar.get():
            coverageLabel.grid(row=5, column=0, pady=10, sticky=tk.W)
            coverageVar.grid(row=5, column=1, pady=10)
        else:
            coverageLabel.grid_forget()
            coverageVar.grid_forget()

    dielecVar.trace_add("write", mostrar_cobertura)
    ttk.Checkbutton(content_frame, text="¿Usar dieléctrico?", variable=dielecVar).grid(row=4, column=0, columnspan=2, pady=10)


    ttk.Label(content_frame, text="Resultados de propiedades físicas calculadas", font=("Arial", 9, "bold")).grid(row=7, column=0, columnspan=2, pady=10)
    resultsLabel = tk.Label(content_frame, wraplength=700)
    resultsLabel.grid(row=8, column=0, columnspan=2, pady=10)

    canvas = tk.Canvas(content_frame, width=700, height=700)
    canvas.grid(row=9, column=0, columnspan=2, pady=10)

    def combined_functions(event):
        updateInterface(typeVar, detailFrame, lengthLabel, lengthEntry, widthLabel, platesDistanceLabel, platesDistanceEntry, widthEntry, outerRadiusLabel, outerRadiusEntry, innerRadiusLabel, innerRadiusEntry, cylOuterRadiusLabel, cylOuterRadiusEntry, cylInnerRadiusLabel,  cylInnerRadiusEntry, cylLengthLabel,  cylLengthEntry)
        getData(typeVar, canvas, lengthEntry, widthEntry, outerRadiusEntry, platesDistanceEntry, innerRadiusEntry, cylOuterRadiusEntry,  cylInnerRadiusEntry,  cylLengthEntry, voltageEntry, dielecVar, coverageVar)
        
        if typeVar.get() == "Parallel":
            plateLength = float(lengthEntry.get()) if lengthEntry.get() else 0.0
            plateWidth = float(widthEntry.get()) if widthEntry.get() else 0.0
            platesD = float(platesDistanceEntry.get()) if platesDistanceEntry.get() else 0.0
            dielectricDist = "" if not dielecVar.get() else coverageVar.get()
            entVoltage = float(voltageEntry.get()) 
            calculateParallelPlates(plateLength, plateWidth, platesD, dielectricDist, entVoltage)
            drawCapacitor("Parallel", canvas, isDielectric=dielecVar.get(), coverage=coverageVar.get(), length=float(lengthEntry.get()), width=float(widthEntry.get()))

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

    ttk.Button(content_frame, text="Calcular", command=lambda: combined_functions(None)).grid(row=6, column=0, columnspan=2, pady=10)

    content_frame.mainloop()

if __name__ == "__main__":
    main()