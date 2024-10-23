import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

class CuadroPuntoEquilibrioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Punto de Equilibrio")

        # Crear las entradas para los valores
        self.entradas = {}

        # Crear el layout del formulario
        self.create_form()

        # Botón para calcular y mostrar el cuadro
        self.calcular_btn = tk.Button(root, text="Calcular y Mostrar Cuadro", command=self.mostrar_cuadro)
        self.calcular_btn.grid(row=7, column=0, columnspan=6, pady=10)

    def create_form(self):
        conceptos = ["Ventas", "Costos variables", "Margen de Contribución", "Costos Fijos", "Utilidad o Pérdida"]
        unidades = ["2,000", "4,000", "6,000", "8,000", "10,000"]

        # Crear cabeceras
        tk.Label(self.root, text="Concepto").grid(row=0, column=0, padx=10, pady=10)
        for i, unidad in enumerate(unidades):
            tk.Label(self.root, text=unidad).grid(row=0, column=i+1)

        # Crear campos para ingresar datos
        for i, concepto in enumerate(conceptos):
            tk.Label(self.root, text=concepto).grid(row=i+1, column=0, padx=10, pady=5)
            self.entradas[concepto] = []
            for j in range(5):
                entry = tk.Entry(self.root)
                entry.grid(row=i+1, column=j+1, padx=5)
                self.entradas[concepto].append(entry)

        # Llenar Costos Fijos con valor predefinido
        for entry in self.entradas["Costos Fijos"]:
            entry.insert(0, "200,000")
            entry.config(state="disabled")  # Deshabilitar las entradas de Costos Fijos

    def mostrar_cuadro(self):
        # Extraer los valores de las entradas
        datos = {}
        try:
            for concepto in self.entradas:
                datos[concepto] = [float(entry.get().replace(',', '')) for entry in self.entradas[concepto]]
        except ValueError:
            messagebox.showerror("Error", "Asegúrese de ingresar solo valores numéricos")
            return

        # Crear el DataFrame con los datos
        data = {
            'Concepto': ["Ventas", "Costos variables", "Margen de Contribución", "Costos Fijos", "Utilidad o Pérdida"],
            '2,000': [datos["Ventas"][0], datos["Costos variables"][0], datos["Margen de Contribución"][0], datos["Costos Fijos"][0], datos["Utilidad o Pérdida"][0]],
            '4,000': [datos["Ventas"][1], datos["Costos variables"][1], datos["Margen de Contribución"][1], datos["Costos Fijos"][1], datos["Utilidad o Pérdida"][1]],
            '6,000': [datos["Ventas"][2], datos["Costos variables"][2], datos["Margen de Contribución"][2], datos["Costos Fijos"][2], datos["Utilidad o Pérdida"][2]],
            '8,000': [datos["Ventas"][3], datos["Costos variables"][3], datos["Margen de Contribución"][3], datos["Costos Fijos"][3], datos["Utilidad o Pérdida"][3]],
            '10,000': [datos["Ventas"][4], datos["Costos variables"][4], datos["Margen de Contribución"][4], datos["Costos Fijos"][4], datos["Utilidad o Pérdida"][4]],
        }
        
        df = pd.DataFrame(data)

        # Crear la tabla con los valores ingresados
        fig, ax = plt.subplots(figsize=(8, 4))
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        # Ajustar la tabla
        table.scale(1.5, 1.5)
        ax.axis('off')

        plt.show()

# Crear la aplicación
root = tk.Tk()
app = CuadroPuntoEquilibrioApp(root)
root.mainloop()
