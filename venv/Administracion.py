import customtkinter
import tkinter as tk
from tkinter import ttk

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

# Crear ventana principal
root = customtkinter.CTk()
root.title("Ventana de Administración")
root.geometry("800x600")

# Función para aplicar filtros (agregar lógica después)
def aplicar_filtros():
    # Supongamos que los resultados se almacenan en una lista llamada "resultados"
    resultados = [
        ("Usuario1", "2023-01-01", "08:00:00", "16:00:00"),
        ("Usuario2", "2023-01-02", "09:00:00", "17:00:00"),
        # Agrega más resultados según tus necesidades
    ]

    # Limpia la tabla antes de mostrar nuevos resultados
    for i in tabla.get_children():
        tabla.delete(i)

    # Agrega los resultados a la tabla
    for resultado in resultados:
        tabla.insert("", "end", values=resultado)

# Función para cerrar la ventana de administración
def cerrar_ventana():
    ventana_administracion.destroy()

# Crear un marco (frame) para organizar los elementos
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Etiqueta de título
label = customtkinter.CTkLabel(master=frame, text="Ventana de Administración")
label.pack(pady=12, padx=10)

# Campos para filtrar
filtro_huella_dactilar_label = customtkinter.CTkLabel(master=frame, text="Filtrar por Huella Dactilar:")
filtro_huella_dactilar_label.pack()
filtro_huella_dactilar_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Huella Dactilar")
filtro_huella_dactilar_entry.pack(pady=6, padx=10)

filtro_fecha_label = customtkinter.CTkLabel(master=frame, text="Filtrar por Fecha:")
filtro_fecha_label.pack()
filtro_fecha_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Fecha (YYYY-MM-DD)")
filtro_fecha_entry.pack(pady=6, padx=10)

filtro_hora_entrada_label = customtkinter.CTkLabel(master=frame, text="Filtrar por Hora de Entrada:")
filtro_hora_entrada_label.pack()
filtro_hora_entrada_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Hora de Entrada (HH:MM:SS)")
filtro_hora_entrada_entry.pack(pady=6, padx=10)

filtro_hora_salida_label = customtkinter.CTkLabel(master=frame, text="Filtrar por Hora de Salida:")
filtro_hora_salida_label.pack()
filtro_hora_salida_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Hora de Salida (HH:MM:SS)")
filtro_hora_salida_entry.pack(pady=6, padx=10)

# Botón para aplicar filtros
aplicar_filtros_button = customtkinter.CTkButton(master=frame, text="Aplicar Filtros", command=aplicar_filtros)
aplicar_filtros_button.pack(pady=12, padx=10)

# Crear la tabla para mostrar resultados
tabla_frame = customtkinter.CTkFrame(master=frame)
tabla_frame.pack(pady=20, padx=10, fill="both", expand=True)

# Configurar la tabla
#*tabla = customtkinter.CTkTreeview(tabla_frame, columns=("Usuario", "Fecha", "Hora Entrada", "Hora Salida"))
# tabla.heading("#1", text="Usuario")
# tabla.heading("#2", text="Fecha")
# tabla.heading("#3", text="Hora Entrada")
# tabla.heading("#4", text="Hora Salida")

tabla = ttk.Treeview(tabla_frame, columns=("Usuario", "Fecha", "Hora Entrada", "Hora Salida"))
tabla.heading("#1", text="Usuario")
tabla.heading("#2", text="Fecha")
tabla.heading("#3", text="Hora Entrada")
tabla.heading("#4", text="Hora Salida")

# Agregar scrollbar
#scrollbar = customtkinter.CTkScrollbar(tabla_frame, orient="vertical", command=tabla.yview)
#tabla.configure(yscroll=scrollbar.set)

#tabla.pack(fill="both", expand=True)
#scrollbar.pack(side="right", fill="y")

# Iniciar la interfaz gráfica
root.mainloop()