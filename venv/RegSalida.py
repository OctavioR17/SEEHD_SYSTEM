import customtkinter

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue")

# Crear ventana principal
root = customtkinter.CTk()
root.title("Registro de Salida")
root.geometry("500x350")

# Función para registrar la salida (agregar lógica después)
def registrar_salida():
    pass

# Función para cerrar la ventana de registro de salida
def cerrar_ventana():
    ventana_registro_salida.destroy()

# Crear un marco (frame) para organizar los elementos
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Etiqueta de título
label = customtkinter.CTkLabel(master=frame, text="Registro de Salida")
label.pack(pady=12, padx=10)

# Campo para ingresar número de cuenta
numero_cuenta_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Número de Cuenta")
numero_cuenta_entry.pack(pady=12, padx=10)

# Campo para ingresar huella dactilar (puedes mostrar una indicación)
huella_dactilar_label = customtkinter.CTkLabel(master=frame, text="Huella Dactilar:")
huella_dactilar_label.pack()

# Botón para registrar salida
registrar_salida_button = customtkinter.CTkButton(master=frame, text="Registrar Salida", command=registrar_salida)
registrar_salida_button.pack(pady=12, padx=10)

# Iniciar la interfaz gráfica
root.mainloop()