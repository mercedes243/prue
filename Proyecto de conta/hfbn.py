import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

class CuadroPuntoEquilibrioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Punto de Equilibrio")

        # Variables para las entradas de unidades vendidas, precio por unidad, costo fijo y costo variable
        self.unidades_entry = tk.Entry(root)
        self.precio_entry = tk.Entry(root)
        self.costo_fijo_entry = tk.Entry(root)
        self.costo_variable_entry = tk.Entry(root)

        self.entradas = {}

        # Crear el layout del formulario
        self.create_form()

        # Botones para calcular, borrar y graficar
        self.calcular_btn = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_btn.grid(row=7, column=6, padx=10, pady=10)

        self.borrar_btn = tk.Button(root, text="Borrar Datos", command=self.borrar_datos)
        self.borrar_btn.grid(row=8, column=6, padx=10, pady=10)

        self.graficar_btn = tk.Button(root, text="Graficar", command=self.mostrar_cuadro)
        self.graficar_btn.grid(row=9, column=6, padx=10, pady=10)

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
            entry.insert(0, "200000")
            entry.config(state="disabled")  # Deshabilitar las entradas de Costos Fijos

    def calcular(self):
        # Extraer valores del formulario
        try:
            ventas = [float(entry.get()) for entry in self.entradas["Ventas"]]
            costos_variables = [float(entry.get()) for entry in self.entradas["Costos variables"]]
            margen_contribucion = [float(entry.get()) for entry in self.entradas["Margen de Contribución"]]
            costos_fijos = 200000

            # Cálculos del punto de equilibrio
            margen_contribucion_unit = ventas[0] - costos_variables[0]  # Precio de venta - Costo variable por unidad
            punto_equilibrio_unidades = costos_fijos / margen_contribucion_unit
            punto_equilibrio_quetzales = punto_equilibrio_unidades * ventas[0]  # Unidades * Precio de venta

            # Mostrar resultado en un messagebox
            messagebox.showinfo("Cálculos",
                                f"Margen de contribución por unidad: Q{margen_contribucion_unit:.2f}\n"
                                f"Unidades para cubrir costos fijos: {punto_equilibrio_unidades:.2f} unidades\n"
                                f"Punto de equilibrio en ventas: Q{punto_equilibrio_quetzales:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Asegúrese de ingresar solo valores numéricos")

    def borrar_datos(self):
        # Borrar datos del formulario
        for concepto in self.entradas:
            for entry in self.entradas[concepto]:
                entry.delete(0, tk.END)

    def mostrar_cuadro(self):
        # Extraer los valores de las entradas
        datos = {}
        try:
            for concepto in self.entradas:
                datos[concepto] = [float(entry.get()) for entry in self.entradas[concepto]]
        except ValueError:
            messagebox.showerror("Error", "Asegúrese de ingresar solo valores numéricos")
            return

        # Crear el DataFrame con los datos
        data = {
            'Concepto': ["Ventas", "Costos variables", "Margen de Contribución", "Costos Fijos", "Utilidad o Pérdida"],
            '2,000': [datos["Ventas"][0], datos["Costos variables"][0], datos["Margen de Contribución"][0], 200000, datos["Utilidad o Pérdida"][0]],
            '4,000': [datos["Ventas"][1], datos["Costos variables"][1], datos["Margen de Contribución"][1], 200000, datos["Utilidad o Pérdida"][1]],
            '6,000': [datos["Ventas"][2], datos["Costos variables"][2], datos["Margen de Contribución"][2], 200000, datos["Utilidad o Pérdida"][2]],
            '8,000': [datos["Ventas"][3], datos["Costos variables"][3], datos["Margen de Contribución"][3], 200000, datos["Utilidad o Pérdida"][3]],
            '10,000': [datos["Ventas"][4], datos["Costos variables"][4], datos["Margen de Contribución"][4], 200000, datos["Utilidad o Pérdida"][4]],
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
