import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Funciones para cálculos
def margen_contribucion(p, cv):
    return p - cv

def punto_equilibrio(cf, mc):
    return cf / mc if mc > 0 else float('inf')

def calcular_utilidad(x, p, cv, cf):
    return x * (p - cv) - cf

def calcular():
    try:
        # Obtener los valores ingresados
        cf = float(entry_cf.get())
        p = float(entry_p.get())
        cv = float(entry_cv.get())
        x = int(entry_x.get())

        # Validar que los valores sean positivos
        if cf < 0 or p <= 0 or cv < 0 or x < 0:
            raise ValueError("Los valores deben ser positivos y el precio mayor que los costos variables")

        # Calcular margen de contribución
        mc = margen_contribucion(p, cv)
        pe_unidades = punto_equilibrio(cf, mc)
        pe_quetzales = pe_unidades * p
        utilidad = calcular_utilidad(x, p, cv, cf)

        # Mostrar resultados en la tabla
        data = {
            'Concepto': ['Ventas', 'Costos Variables', 'Margen de Contribución', 'Costos Fijos', 'Utilidad/Pérdida'],
            'Monto': [x * p, x * cv, x * mc, cf, utilidad]
        }

        # Crear un DataFrame de pandas para mostrar el cuadro financiero
        cuadro_financiero = pd.DataFrame(data)
        print("\nCuadro Financiero:")
        print(cuadro_financiero)

        # Mostrar resultados en la interfaz gráfica
        label_mc.config(text=f"Margen de Contribución por unidad: Q{mc:.2f}")
        label_pe_unidades.config(text=f"Punto de Equilibrio (unidades): {pe_unidades:.2f}")
        label_pe_quetzales.config(text=f"Punto de Equilibrio (quetzales): Q{pe_quetzales:.2f}")
        label_utilidad.config(text=f"Utilidad / Pérdida (para {x} unidades): Q{utilidad:.2f}")

        # Gráfica de costos e ingresos
        generar_grafica(p, cv, cf, x, pe_unidades)

    except ValueError as e:
        label_mc.config(text=f"Error: {e}")
    except ZeroDivisionError:
        label_mc.config(text="Error: El precio debe ser mayor que los costos variables")

# Función para generar la gráfica
def generar_grafica(p, cv, cf, x, pe_unidades):
    # Datos para la gráfica
    unidades = np.linspace(0, pe_unidades * 1.5, 400)
    ingresos = p * unidades
    costos_totales = cf + cv * unidades
    utilidad = calcular_utilidad(unidades, p, cv, cf)

    # Crear gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(unidades, ingresos, label='Ingresos', color='blue')
    plt.plot(unidades, costos_totales, label='Costos Totales', color='red')
    plt.plot(unidades, utilidad, label='Utilidad/Pérdida', color='purple')
    plt.axvline(x=pe_unidades, color='green', linestyle='--', label='Punto de Equilibrio')
    plt.axhline(y=cf, color='gray', linestyle='--', label='Costos Fijos')
    plt.plot(pe_unidades, cf, 'go', label=f'PE: {pe_unidades:.2f} unidades')

    plt.title('Análisis del Punto de Equilibrio')
    plt.xlabel('Número de Unidades Vendidas')
    plt.ylabel('Cantidad de Dinero (Q)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Crear la interfaz de usuario
root = tk.Tk()
root.title("Análisis del Punto de Equilibrio")
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Etiquetas y campos de entrada
tk.Label(frame, text="Costos Fijos (Q)", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
entry_cf = tk.Entry(frame, font=("Arial", 12))
entry_cf.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Precio por Unidad (Q)", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
entry_p = tk.Entry(frame, font=("Arial", 12))
entry_p.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Costos Variables por Unidad (Q)", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
entry_cv = tk.Entry(frame, font=("Arial", 12))
entry_cv.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Número de Unidades Vendidas (X)", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
entry_x = tk.Entry(frame, font=("Arial", 12))
entry_x.grid(row=3, column=1, padx=5, pady=5)

# Botón para calcular
button_calcular = tk.Button(frame, text="Calcular", font=("Arial", 12, "bold"), command=calcular)
button_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Resultados
label_mc = tk.Label(frame, text="Margen de Contribución por unidad: ", font=("Arial", 12))
label_mc.grid(row=5, column=0, columnspan=2, pady=5)

label_pe_unidades = tk.Label(frame, text="Punto de Equilibrio (unidades): ", font=("Arial", 12))
label_pe_unidades.grid(row=6, column=0, columnspan=2, pady=5)

label_pe_quetzales = tk.Label(frame, text="Punto de Equilibrio (quetzales): ", font=("Arial", 12))
label_pe_quetzales.grid(row=7, column=0, columnspan=2, pady=5)

label_utilidad = tk.Label(frame, text="Utilidad / Pérdida: ", font=("Arial", 12))
label_utilidad.grid(row=8, column=0, columnspan=2, pady=5)

root.mainloop()
