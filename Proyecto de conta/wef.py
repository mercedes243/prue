import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

def calcular_punto_equilibrio():
    try:
        p = float(entry_precio.get())
        cv = float(entry_costo_variable.get())
        cf = float(entry_costo_fijo.get())
        x = cf / (p - cv)
        ventas_totales = x * p
        costos_variables_totales = x * cv
        margen_contribucion_total = ventas_totales - costos_variables_totales
        utilidad_perdida = margen_contribucion_total - cf

        resultado.set(f"Unidades para cubrir gastos fijos: {x:.2f}\n"
                      f"Ventas totales para punto de equilibrio: Q{ventas_totales:.2f}")

        # Actualizar tabla
        tabla.delete(*tabla.get_children())
        tabla.insert("", "end", values=("Ventas totales", f"Q{ventas_totales:.2f}"))
        tabla.insert("", "end", values=("Costos variables totales", f"Q{costos_variables_totales:.2f}"))
        tabla.insert("", "end", values=("Margen de contribución total", f"Q{margen_contribucion_total:.2f}"))
        tabla.insert("", "end", values=("Costos fijos", f"Q{cf:.2f}"))
        tabla.insert("", "end", values=("Utilidad o pérdida", f"Q{utilidad_perdida:.2f}"))

        # Graficar
        graficar(p, cv, cf, x)
    except ValueError:
        resultado.set("Por favor, ingrese valores numéricos válidos.")

def graficar(p, cv, cf, x):
    unidades = np.arange(0, x*2, 1)
    ingresos = unidades * p
    costos_totales = cf + (unidades * cv)
    utilidad = ingresos - costos_totales

    plt.figure(figsize=(10, 6))
    plt.plot(unidades, ingresos, label='Ingresos')
    plt.plot(unidades, costos_totales, label='Costos Totales')
    plt.plot(unidades, utilidad, label='Utilidad')
    plt.axvline(x=x, color='r', linestyle='--', label='Punto de Equilibrio')
    plt.xlabel('Unidades Vendidas')
    plt.ylabel('Quetzales')
    plt.title('Análisis del Punto de Equilibrio')
    plt.legend()
    plt.grid(True)
    plt.show()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Análisis del Punto de Equilibrio")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Precio por unidad (p):").grid(column=1, row=1, sticky=tk.W)
entry_precio = ttk.Entry(frame)
entry_precio.grid(column=2, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Costo variable por unidad (cv):").grid(column=1, row=2, sticky=tk.W)
entry_costo_variable = ttk.Entry(frame)
entry_costo_variable.grid(column=2, row=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Costos fijos (cf):").grid(column=1, row=3, sticky=tk.W)
entry_costo_fijo = ttk.Entry(frame)
entry_costo_fijo.grid(column=2, row=3, sticky=(tk.W, tk.E))

ttk.Button(frame, text="Calcular Punto de Equilibrio", command=calcular_punto_equilibrio).grid(column=2, row=4, sticky=tk.W)

resultado = tk.StringVar()
ttk.Label(frame, textvariable=resultado).grid(column=1, row=5, columnspan=2, sticky=(tk.W, tk.E))

# Tabla de resultados
columns = ("Concepto", "Valor")
tabla = ttk.Treeview(frame, columns=columns, show='headings')
tabla.heading("Concepto", text="Concepto")
tabla.heading("Valor", text="Valor")
tabla.grid(column=1, row=6, columnspan=2, sticky=(tk.W, tk.E))

root.mainloop()
