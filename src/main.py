import tkinter as tk
from src.Calculadora import CalculadoraMatricesVectores

def main():
    root = tk.Tk()
    app = CalculadoraMatricesVectores(root)
    root.mainloop()

if __name__ == "__main__":
    main()