import tkinter as tk
from tkinter import messagebox
import numpy as np
import re

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
        self.boton_determinante_a = tk.Button(self.root, text="Determinante (A)", width=20, command=lambda: self.determinante('A'))
        self.boton_determinante_a.grid(row=2, column=0, padx=5, pady=5)

        self.boton_inversa_a = tk.Button(self.root, text="Inversa (A)", width=20, command=lambda: self.inversa('A'))
        self.boton_inversa_a.grid(row=3, column=0, padx=5, pady=5)

        self.boton_transpuesta_a = tk.Button(self.root, text="Transpuesta (A)", width=20, command=lambda: self.transpuesta('A'))
        self.boton_transpuesta_a.grid(row=4, column=0, padx=5, pady=5)

        self.boton_subespacio_a = tk.Button(self.root, text="Verificar Subespacio (A)", width=20, command=lambda: self.verificar_subespacio('A'))
        self.boton_subespacio_a.grid(row=5, column=0, padx=5, pady=5)

        self.boton_determinante_b = tk.Button(self.root, text="Determinante (B)", width=20, command=lambda: self.determinante('B'))
        self.boton_determinante_b.grid(row=2, column=2, padx=5, pady=5)

        self.boton_inversa_b = tk.Button(self.root, text="Inversa (B)", width=20, command=lambda: self.inversa('B'))
        self.boton_inversa_b.grid(row=3, column=2, padx=5, pady=5)

        self.boton_transpuesta_b = tk.Button(self.root, text="Transpuesta (B)", width=20, command=lambda: self.transpuesta('B'))
        self.boton_transpuesta_b.grid(row=4, column=2, padx=5, pady=5)

        self.boton_subespacio_b = tk.Button(self.root, text="Verificar Subespacio (B)", width=20, command=lambda: self.verificar_subespacio('B'))
        self.boton_subespacio_b.grid(row=5, column=2, padx=5, pady=5)

    def cambiar_tipo(self):
        tipo = self.tipo.get()

        # Mostrar u ocultar los botones de operaciones según el tipo seleccionado
        if tipo == "Matriz":
            self.boton_determinante_a.grid(row=2, column=0, padx=5, pady=5)
            self.boton_inversa_a.grid(row=3, column=0, padx=5, pady=5)
            self.boton_transpuesta_a.grid(row=4, column=0, padx=5, pady=5)
            self.boton_subespacio_a.grid(row=5, column=0, padx=5, pady=5)
            self.boton_determinante_b.grid(row=2, column=2, padx=5, pady=5)
            self.boton_inversa_b.grid(row=3, column=2, padx=5, pady=5)
            self.boton_transpuesta_b.grid(row=4, column=2, padx=5, pady=5)
            self.boton_subespacio_b.grid(row=5, column=2, padx=5, pady=5)
        else:
            self.boton_determinante_a.grid_forget()
            self.boton_inversa_a.grid_forget()
            self.boton_transpuesta_a.grid_forget()
            self.boton_determinante_b.grid_forget()
            self.boton_inversa_b.grid_forget()
            self.boton_transpuesta_b.grid_forget()


    def obtener_matriz(self, texto):
        try:
            contenido = texto.get("1.0", tk.END).strip()
            if not contenido:
                return None  # No hacer nada si el texto está vacío
            matriz = np.array(eval(contenido))
            return matriz
        except Exception as e:
            messagebox.showerror("Error", f"Formato de matriz incorrecto: {e}. Usa [[1, 2], [3, 4]]")
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
            "np": np  # Para usar funciones de numpy
        }
        
        # Solo agrega B si ha sido ingresada
        if matriz_b is not None:
            entorno["B"] = matriz_b

        # Obtener la expresión de operación personalizada
        operacion = self.operacion_text.get()

        # Paso 1: Detectar multiplicación por un escalar, por ejemplo "2A" -> "2 * A"
        operacion = re.sub(r'(\d+)(A|B)', r'\1*\2', operacion)  # Detecta 2A, 3B, etc. y los convierte en 2*A, 3*B

        # Paso 2: Ajustar la operación para potencia de matrices con "^", como A^2 -> np.linalg.matrix_power(A, 2)
        operacion = re.sub(r'([A|B])\^(\d+)', r'np.linalg.matrix_power(\1, \2)', operacion)

        # Paso 3: Ajustar la operación para multiplicación de matrices, permitiendo multiplicación por escalar
        # Cambiar solo cuando ambos lados del * son A o B
        operacion = re.sub(r'(?<!\w)(A|B)\s*\*\s*(A|B)(?!\w)', r'np.matmul(\1, \2)', operacion)

        # Paso 4: Reemplazar "^" con el operador de potencia cuando no se utiliza para matrices, solo como potencia de números
        operacion = operacion.replace("^", "**")  # Cambiar ^ a ** para operaciones estándar de Python

        try:
            # Evaluar la operación en el entorno definido
            resultado = eval(operacion, {"__builtins__": None}, entorno)
            self.mostrar_resultado(f"Resultado de '{self.operacion_text.get()}':\n{resultado}")
        except Exception as e:
            messagebox.showerror("Error", f"Operación inválida: {e}")


    def determinante(self, matriz):
        matriz_actual = self.obtener_matriz(self.matriz_a_text if matriz == 'A' else self.matriz_b_text)
        if matriz_actual is not None:
            if matriz_actual.shape[0] == matriz_actual.shape[1]:
                resultado = np.linalg.det(matriz_actual)
                self.mostrar_resultado(f"Determinante de {matriz}: {resultado}")
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

    def verificar_subespacio(self, matriz):
        matriz_actual = self.obtener_matriz(self.matriz_a_text if matriz == 'A' else self.matriz_b_text)
        if matriz_actual is not None:
            # Verificar que la matriz contiene el vector cero
            if not np.any(matriz_actual == 0):
                messagebox.showerror("Error", f"La matriz {matriz} no contiene el vector cero.\n"
                                             "Contraejemplo: Resta de la matriz consigo misma.\n"
                                             f"{matriz_actual} - {matriz_actual} = {np.subtract(matriz_actual, matriz_actual)}")
                return

            # Verificar cerradura bajo adición
            suma = np.add(matriz_actual, matriz_actual)
            if not np.array_equal(suma, matriz_actual):
                messagebox.showerror("Error", f"La matriz {matriz} no es cerrada bajo adición.\n"
                                             f"Contraejemplo: Suma de la matriz consigo misma.\n"
                                             f"{matriz_actual} + {matriz_actual} = {suma}")
                return

            # Verificar cerradura bajo multiplicación por escalar
            escalar = 2
            multiplicado = np.multiply(matriz_actual, escalar)
            if not np.array_equal(multiplicado, matriz_actual):
                messagebox.showerror("Error", f"La matriz {matriz} no es cerrada bajo multiplicación por escalar.\n"
                                             f"Contraejemplo: Multiplicación por el escalar {escalar}.\n"
                                             f"{matriz_actual} * {escalar} = {multiplicado}")
                return

            # Si todas las propiedades se cumplen
            self.mostrar_resultado(f"La matriz {matriz} es un subespacio vectorial.")

    def mostrar_resultado(self, resultado):
        self.resultado_label.config(state='normal')
        self.resultado_label.delete("1.0", tk.END)
        self.resultado_label.insert(tk.END, str(resultado))
        self.resultado_label.config(state='disabled')

# Inicializar la aplicación
root = tk.Tk()
app = CalculadoraMatricesVectores(root)
root.mainloop()
