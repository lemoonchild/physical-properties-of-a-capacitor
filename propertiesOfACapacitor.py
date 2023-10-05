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
import tkinter as tk  # Biblioteca estándar para crear interfaces gráficas en Python
from tkinter import ttk  # Módulo que proporciona acceso a widgets adicionales de tkinter
import numpy as np  # Biblioteca para operaciones matemáticas y manipulación de arrays
import matplotlib.pyplot as plt  # Biblioteca para crear gráficos y visualizaciones
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Permite embeber gráficos de Matplotlib en una aplicación tkinter
# ---------------------------------------------------------------------------