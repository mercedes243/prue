import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

class BreakEvenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo del Punto de Equilibrio")
        self.root.geometry("700x500")

        # Pestañas
        self.tab_control = ttk.Notebook(self.root)

        self.tab_calculo = ttk.Frame(self.tab_control)
        self.tab_grafica = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_calculo, text='Cálculo')
        self.tab_control.add(self.tab_grafica, text='Gráfica')

        self.tab_control.pack(expand=1, fill='both')

        self.create_calculo_tab()
        self.create_grafica_tab()

    def create_calculo_tab(self):
        # Entradas de usuario
        ttk.Label(self.tab_calculo, text="Costos Fijos (Quetzales):").grid(column=0, row=0, padx=10, pady=5)
        self.fixed_costs = tk.DoubleVar()
        ttk.Entry(self.tab_calculo, textvariable=self.fixed_costs).grid(column=1, row=0)

        ttk.Label(self.tab_calculo, text="Precio de Venta (Quetzales):").grid(column=0, row=1, padx=10, pady=5)
        self.sale_price = tk.DoubleVar()
        ttk.Entry(self.tab_calculo, textvariable=self.sale_price).grid(column=1, row=1)

        ttk.Label(self.tab_calculo, text="Costo Variable por Unidad (Quetzales):").grid(column=0, row=2, padx=10, pady=5)
        self.variable_cost = tk.DoubleVar()
        ttk.Entry(self.tab_calculo, textvariable=self.variable_cost).grid(column=1, row=2)

        # Botón para calcular
        ttk.Button(self.tab_calculo, text="Calcular Punto de Equilibrio", command=self.calculate_breakeven).grid(column=0, row=3, columnspan=2, pady=10)

        # Botones para resultados
        self.create_results_buttons()

    def create_results_buttons(self):
        # Crear cuadro resumen tipo Excel
        self.results_frame = ttk.Frame(self.tab_calculo)
        self.results_frame.grid(column=0, row=4, columnspan=2, pady=10)

        self.costos_fijos_btn = ttk.Button(self.results_frame, text="Costos Fijos: 0", command=lambda: None)
        self.costos_fijos_btn.grid(row=0, column=0)

        self.ventas_btn = ttk.Button(self.results_frame, text="Ventas Totales: 0", command=lambda: None)
        self.ventas_btn.grid(row=1, column=0)

        self.margen_contribucion_btn = ttk.Button(self.results_frame, text="Margen de Contribución: 0", command=lambda: None)
        self.margen_contribucion_btn.grid(row=2, column=0)

        self.punto_equilibrio_btn = ttk.Button(self.results_frame, text="Punto de Equilibrio: 0", command=lambda: None)
        self.punto_equilibrio_btn.grid(row=3, column=0)

        self.utilidad_perdida_btn = ttk.Button(self.results_frame, text="Utilidad o Pérdida: 0", command=lambda: None)
        self.utilidad_perdida_btn.grid(row=4, column=0)

    def create_grafica_tab(self):
        ttk.Button(self.tab_grafica, text="Mostrar Gráfica", command=self.plot_breakeven).pack(pady=20)

    def calculate_breakeven(self):
        fixed_costs = self.fixed_costs.get()
        sale_price = self.sale_price.get()
        variable_cost = self.variable_cost.get()

        if sale_price <= variable_cost:
            self.update_result_buttons(0, 0, 0, 0, 0)
            self.punto_equilibrio_btn.config(text="Error: El precio de venta debe ser mayor que el costo variable.")
            return

        # Cálculo del punto de equilibrio en unidades y quetzales
        breakeven_units = fixed_costs / (sale_price - variable_cost)
        breakeven_quetzales = breakeven_units * sale_price

        # Cálculo del margen de contribución
        margin_per_unit = sale_price - variable_cost

        # Ingresos totales en el punto de equilibrio
        total_revenue = breakeven_units * sale_price

        # Ganancias o pérdidas
        utility_loss = total_revenue - fixed_costs

        # Actualización de los botones con resultados
        self.update_result_buttons(fixed_costs, total_revenue, margin_per_unit, breakeven_quetzales, utility_loss)

    def update_result_buttons(self, fixed_costs, total_revenue, margin_per_unit, breakeven, utility_loss):
        self.costos_fijos_btn.config(text=f"Costos Fijos: {fixed_costs:.2f}")
        self.ventas_btn.config(text=f"Ventas Totales: {total_revenue:.2f}")
        self.margen_contribucion_btn.config(text=f"Margen de Contribución por Unidad: {margin_per_unit:.2f}")
        self.punto_equilibrio_btn.config(text=f"Punto de Equilibrio en Quetzales: {breakeven:.2f}")
        self.utilidad_perdida_btn.config(text=f"Utilidad o Pérdida: {utility_loss:.2f}")

    def plot_breakeven(self):
        fixed_costs = self.fixed_costs.get()
        sale_price = self.sale_price.get()
        variable_cost = self.variable_cost.get()

        breakeven_units = fixed_costs / (sale_price - variable_cost)

        # Datos para la gráfica
        units = np.arange(0, breakeven_units * 2, 1)
        revenue = sale_price * units
        total_costs = fixed_costs + variable_cost * units
        variable_costs = variable_cost * units  
        fixed_costs_line = np.full_like(units, fixed_costs)

        # Gráfica del punto de equilibrio
        plt.figure(figsize=(10, 6))
        plt.plot(units, revenue, label='Ingresos Totales', color='green')
        plt.plot(units, total_costs, label='Costos Totales', color='red')
        plt.plot(units, variable_costs, label='Costos Variables', color='orange')
        plt.plot(units, fixed_costs_line, label='Costos Fijos', color='blue', linestyle='--')
        plt.axvline(x=breakeven_units, color='black', linestyle='--', label='Punto de Equilibrio')
        plt.title('Gráfica del Punto de Equilibrio')
        plt.xlabel('Unidades')
        plt.ylabel('Quetzales')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BreakEvenApp(root)
    root.mainloop()
