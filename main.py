## -- Calculadora de edad
'''
El objetivo es crear una pequeña aplicación que pida el año de nacimiento y, al hacer clic en un botón,
muestre la edad aproximada de la persona.
''' 

# Importar tkinter junto a otras funciones del mismo
import tkinter as tk
from datetime import datetime

# Función para calcular la edad
def calcular_edad():
    try:
        nacimiento = int(entry_edad.get())
        edad_actual = datetime.now().year
        edad = edad_actual - nacimiento
        if edad < 0:
            label_resultado.config(text="Eñ año de nacimiento no puede ser mayor que el año actual")
        elif edad == 2025:
            label_resultado.config(text=f"Tienes {edad} años de eda... ¿Jesús Joestar? ¿Eres tú??")
        elif edad > 1000:
            label_resultado.config(text=f"¿Acaso eres una criatura omnisciente??? Tienes {edad} años de antigüedad.")
        elif edad > 120:
            label_resultado.config(text=f"Probablemente seas un ser inmortal. En ese caso, tienes {edad} años de antigüedad.")
        else:
            label_resultado.config(text=f"Tienes aproximadamente {edad} años.")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un año válido")


# Crear la ventana principal junto al título
ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("340x200")
ventana.configure(bg="#f0f0f0")

# Etiqueta para el título
label_titulo = tk.Label(ventana, text="Calculadora de Edad")
label_titulo.grid(row=0, column=0, columnspan=2, pady=5)

# Etiqueta para el año de nacimiento
label_edad = tk.Label(ventana, text="Ingresa tu año de nacimiento:")
label_edad.grid(row=1, column=0, padx=10, pady=10)

# Entrada
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=10, pady=5)

# Botón para llamar función calcular la edad
boton_calcular = tk.Button(ventana, text="Calcular Edad", command=calcular_edad)
boton_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Loop principal de la aplicación
ventana.mainloop()