import tkinter as tk
from tkinter import messagebox
import requests

def calcular_suma():
    numero1 = float(entrada_numero1.get())
    numero2 = float(entrada_numero2.get())

    api_url = "http://localhost/php_api/api2.php"
    parametros = {"numero1": numero1, "numero2": numero2}

    try:
        response = requests.post(api_url, data=parametros)
        response_data = response.json()

        if response.status_code == 200:
            resultado = response_data["resultado"]
            resultado_label.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Error", f"Error: {response_data['error']}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error al conectar con el API: {e}")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Suma")

# Etiquetas y campos de entrada
etiqueta_numero1 = tk.Label(ventana, text="Número 1:")
etiqueta_numero1.pack()
entrada_numero1 = tk.Entry(ventana)
entrada_numero1.pack()

etiqueta_numero2 = tk.Label(ventana, text="Número 2:")
etiqueta_numero2.pack()
entrada_numero2 = tk.Entry(ventana)
entrada_numero2.pack()

# Botón para calcular la suma
calcular_button = tk.Button(ventana, text="Calcular Suma", command=calcular_suma)
calcular_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Iniciar la aplicación
ventana.mainloop()
