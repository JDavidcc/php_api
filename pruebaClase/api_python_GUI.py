import tkinter as tk
from tkinter import ttk
import requests

# Función para cargar las colonias desde el API y cargarlas en el ComboBox
def cargar_colonias():
    codigo_postal = codigo_postal_entry.get()

    # Realizar una solicitud GET al API con el código postal
    api_url = f"http://localhost/PHP_API/pruebaClase/api_mysql.Php?cp={codigo_postal}"
    response = requests.get(api_url)

    if response.status_code == 200:
        colonias = response.json()

        # Limpiar el ComboBox antes de cargar las nuevas colonias
        colonias_combo["values"] = ()

        if colonias:
            colonias_combo["values"] = colonias
        else:
            colonias_combo["values"] = ("No se encontraron colonias",)
    else:
        colonias_combo["values"] = ("Error al cargar las colonias",)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Búsqueda de Colonias por Código Postal")

# Etiqueta y campo de entrada para el código postal
codigo_postal_label = tk.Label(ventana, text="Código Postal:")
codigo_postal_label.grid(row=0, column=0, padx=10, pady=10)
codigo_postal_entry = tk.Entry(ventana)
codigo_postal_entry.grid(row=0, column=1, padx=10, pady=10)

# Botón para cargar las colonias
cargar_button = tk.Button(ventana, text="Cargar Colonias", command=cargar_colonias)
cargar_button.grid(row=0, column=2, padx=10, pady=10)

# ComboBox para mostrar las colonias
colonias_combo = ttk.Combobox(ventana)
colonias_combo.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
colonias_combo["values"] = ("Selecciona un código postal",)

# Iniciar la aplicación
ventana.mainloop()
