import tkinter as tk
from tkinter import messagebox
import numpy as np

class CalculadoraMatricesVectores:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Matrices y Vectores")
        self.root.configure(bg='#2E3B4E')

        # Opción para elegir entre matrices o vectores
        self.tipo = tk.StringVar(value="Matriz")  # Por defecto es Matriz
        tk.Label(self.root, text="Selecciona tipo:", fg="white", bg='#2E3B4E').grid(row=0, column=0, padx=10, pady=10)
        tk.Radiobutton(self.root, text="Matriz", variable=self.tipo, value="Matriz", fg="white", bg='#2E3B4E', command=self.cambiar_tipo).grid(row=0, column=1)
        tk.Radiobutton(self.root, text="Vector", variable=self.tipo, value="Vector", fg="white", bg='#2E3B4E', command=self.cambiar_tipo).grid(row=0, column=2)

        # Entradas de Matrices o Vectores
        self.matriz_a_text = self.crear_texto()
        self.matriz_a_text.grid(row=1, column=0, padx=10, pady=10)

        self.matriz_b_text = self.crear_texto()
        self.matriz_b_text.grid(row=1, column=2, padx=10, pady=10)

        # Botones de Operaciones
        self.create_buttons()

        # Entrada para operaciones personalizadas
        tk.Label(self.root, text="Operación personalizada (ej. 2*A + B):", fg="white", bg='#2E3B4E').grid(row=6, column=0, columnspan=3, pady=(10, 0))
        self.operacion_text = tk.Entry(self.root, width=30)
        self.operacion_text.grid(row=7, column=0, columnspan=2, padx=10, pady=(5, 10))
        tk.Button(self.root, text="Calcular", width=10, command=self.calcular_operacion_personalizada).grid(row=7, column=2, padx=10, pady=(5, 10))

        # Resultado
        tk.Label(self.root, text="Resultado:", fg="white", bg='#2E3B4E').grid(row=8, column=0, columnspan=3)
        self.resultado_label = tk.Text(self.root, width=50, height=5, state='disabled')
        self.resultado_label.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    def crear_texto(self):
        return tk.Text(self.root, width=20, height=5)

    def create_buttons(self):
        # Botones de Operaciones para Matrices o Vectores

        # Botones para determinante
        self.boton_determinante_a = tk.Button(self.root, text="Determinante (A)", width=20, command=lambda: self.determinante('A'))
        self.boton_determinante_a.grid(row=2, column=0, padx=5, pady=5)
        self.boton_determinante_b = tk.Button(self.root, text="Determinante (B)", width=20, command=lambda: self.determinante('B'))
        self.boton_determinante_b.grid(row=2, column=2, padx=5, pady=5)

        # Botones para inversa
        self.boton_inversa_a = tk.Button(self.root, text="Inversa (A)", width=20, command=lambda: self.inversa('A'))
        self.boton_inversa_a.grid(row=3, column=0, padx=5, pady=5)
        self.boton_inversa_b = tk.Button(self.root, text="Inversa (B)", width=20, command=lambda: self.inversa('B'))
        self.boton_inversa_b.grid(row=3, column=2, padx=5, pady=5)

        # Botones para transpuesta
        self.boton_transpuesta_a = tk.Button(self.root, text="Transpuesta (A)", width=20, command=lambda: self.transpuesta('A'))
        self.boton_transpuesta_a.grid(row=4, column=0, padx=5, pady=5)
        self.boton_transpuesta_b = tk.Button(self.root, text="Transpuesta (B)", width=20, command=lambda: self.transpuesta('B'))
        self.boton_transpuesta_b.grid(row=4, column=2, padx=5, pady=5)

        # Botones para producto punto y producto cruz (vectores)
        self.boton_producto_punto = tk.Button(self.root, text="Producto Punto (A·B)", width=20, command=self.producto_punto)
        self.boton_producto_cruz = tk.Button(self.root, text="Producto Cruz (A×B)", width=20, command=self.producto_cruz)

        # Botones para magnitud (vectores)
        self.boton_magnitud_a = tk.Button(self.root, text="Magnitud (A)", width=20, command=lambda: self.magnitud_vector('A'))
        self.boton_magnitud_b = tk.Button(self.root, text="Magnitud (B)", width=20, command=lambda: self.magnitud_vector('B'))

    def cambiar_tipo(self):
        tipo = self.tipo.get()

        # Mostrar u ocultar los botones de operaciones según el tipo seleccionado
        if (tipo == "Matriz"):
            self.boton_determinante_a.grid(row=2, column=0, padx=5, pady=5)
            self.boton_inversa_a.grid(row=3, column=0, padx=5, pady=5)
            self.boton_transpuesta_a.grid(row=4, column=0, padx=5, pady=5)
            self.boton_determinante_b.grid(row=2, column=2, padx=5, pady=5)
            self.boton_inversa_b.grid(row=3, column=2, padx=5, pady=5)
            self.boton_transpuesta_b.grid(row=4, column=2, padx=5, pady=5)
            self.boton_producto_punto.grid_forget()
            self.boton_producto_cruz.grid_forget()
            self.boton_magnitud_a.grid_forget()
            self.boton_magnitud_b.grid_forget()
        elif (tipo == "Vector"):
            self.boton_determinante_a.grid_forget()
            self.boton_inversa_a.grid_forget()
            self.boton_transpuesta_a.grid_forget()
            self.boton_determinante_b.grid_forget()
            self.boton_inversa_b.grid_forget()
            self.boton_transpuesta_b.grid_forget()
            self.boton_producto_punto.grid(row=3, column=1, padx=5, pady=5)
            self.boton_producto_cruz.grid(row=4, column=1, padx=5, pady=5)
            self.boton_magnitud_a.grid(row=2, column=0, padx=5, pady=5)
            self.boton_magnitud_b.grid(row=2, column=2, padx=5, pady=5)

    def convertir_matriz(self, entrada):
        filas = entrada.split(';')
        matriz = [list(map(int, fila.split())) for fila in filas]
        return matriz

    def convertir_vector(self, entrada):
        vector = list(map(int, entrada.split()))
        return vector

    def obtener_matriz(self, texto):
        try:
            entrada = texto.get("1.0", tk.END).strip()
            matriz = np.array(self.convertir_matriz(entrada))
            return matriz
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener la matriz/vector: {e}")
            return None

    def obtener_vector(self, texto):
        try:
            entrada = texto.get("1.0", tk.END).strip()
            vector = np.array(self.convertir_vector(entrada))
            return vector
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener el vector: {e}")
            return None

    def calcular_operacion_personalizada(self):
        # Obtener las matrices A y B
        matriz_a = self.obtener_matriz(self.matriz_a_text)
        matriz_b = self.obtener_matriz(self.matriz_b_text)

        if matriz_a is None:
            return

        # Entorno para operaciones personalizadas
        entorno = {
            "A": matriz_a,
            "np": np 
        }
        
        if matriz_b is not None:
            entorno["B"] = matriz_b

        # Obtener la expresión de operación personalizada
        operacion = self.operacion_text.get().strip()
        try:
            resultado = eval(operacion, entorno)
            self.mostrar_resultado(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la operación personalizada: {e}")

    def producto_punto(self):
        vector_a = self.obtener_vector(self.matriz_a_text)
        vector_b = self.obtener_vector(self.matriz_b_text)
        if vector_a is not None and vector_b is not None:
            try:
                resultado = np.dot(vector_a, vector_b)
                self.mostrar_resultado(f"Producto Punto (A·B):\n{resultado}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al calcular el producto punto: {e}")

    def producto_cruz(self):
        vector_a = self.obtener_vector(self.matriz_a_text)
        vector_b = self.obtener_vector(self.matriz_b_text)
        if vector_a is not None and vector_b is not None:
            try:
                resultado = np.cross(vector_a, vector_b)
                self.mostrar_resultado(f"Producto Cruz (A×B):\n{resultado}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al calcular el producto cruz: {e}")

    def magnitud_vector(self, vector):
        vector_actual = self.obtener_vector(self.matriz_a_text if vector == 'A' else self.matriz_b_text)
        if vector_actual is not None:
            if vector_actual.ndim == 1:
                resultado = np.linalg.norm(vector_actual)
                self.mostrar_resultado(f"Magnitud de {vector}: {resultado:.2f}")
            else:
                messagebox.showerror("Error", "La entrada debe ser un vector para calcular la magnitud.")

    def determinante(self, matriz):
        matriz_actual = self.obtener_matriz(self.matriz_a_text if matriz == 'A' else self.matriz_b_text)
        if matriz_actual is not None:
            if matriz_actual.shape[0] == matriz_actual.shape[1]:
                try:
                    resultado = np.linalg.det(matriz_actual)
                    self.mostrar_resultado(f"Determinante de {matriz}: {resultado:.2f}")
                except np.linalg.LinAlgError:
                    messagebox.showerror("Error", "La matriz no es invertible.")
            else:
                messagebox.showerror("Error", "La matriz debe ser cuadrada para calcular el determinante.")

    def inversa(self, matriz):
        matriz_actual = self.obtener_matriz(self.matriz_a_text if matriz == 'A' else self.matriz_b_text)
        if matriz_actual is not None:
            if matriz_actual.shape[0] == matriz_actual.shape[1]:
                try:
                    resultado = np.linalg.inv(matriz_actual)
                    self.mostrar_resultado(f"Inversa de {matriz}:\n{resultado}")
                except np.linalg.LinAlgError:
                    messagebox.showerror("Error", "La matriz no es invertible.")
            else:
                messagebox.showerror("Error", "La matriz debe ser cuadrada para calcular la inversa.")

    def transpuesta(self, matriz):
        matriz_actual = self.obtener_matriz(self.matriz_a_text if matriz == 'A' else self.matriz_b_text)
        if matriz_actual is not None:
            resultado = matriz_actual.T
            self.mostrar_resultado(f"Transpuesta de {matriz}:\n{resultado}")

    def mostrar_resultado(self, resultado):
        if isinstance(resultado, (np.ndarray, list)):
            resultado = np.round(resultado, decimals=2)
            resultado_str = np.array2string(resultado, precision=2, separator=', ')
        elif isinstance(resultado, (int, float)):
            resultado = round(resultado, 2)
            resultado_str = f"{resultado:.2f}"
        else:
            resultado_str = str(resultado)
        
        self.resultado_label.config(state='normal')
        self.resultado_label.delete("1.0", tk.END)
        self.resultado_label.insert(tk.END, resultado_str)
        self.resultado_label.config(state='disabled')

# Inicializar la aplicación
root = tk.Tk()
app = CalculadoraMatricesVectores(root)
root.mainloop()
