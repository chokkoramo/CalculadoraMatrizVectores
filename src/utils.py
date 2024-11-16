import numpy as np
import tkinter as tk
from tkinter import messagebox

def convertir_matriz(entrada):
    filas = entrada.split(';')
    matriz = [list(map(int, fila.split())) for fila in filas]
    return matriz

def convertir_vector(entrada):
    vector = list(map(int, entrada.split()))
    return vector

def obtener_matriz(texto):
    try:
        entrada = texto.get("1.0", tk.END).strip()
        matriz = np.array(convertir_matriz(entrada))
        return matriz
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener la matriz/vector: {e}")
        return None

def obtener_vector(texto):
    try:
        entrada = texto.get("1.0", tk.END).strip()
        vector = np.array(convertir_vector(entrada))
        return vector
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener el vector: {e}")
        return None