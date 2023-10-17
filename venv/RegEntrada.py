

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

# Crear ventana principal
root = customtkinter.CTk()
root.title("Registro de Entrada")
root.geometry("500x350")

# Función para registrar la entrada (agregar lógica después)
def registrar_entrada():
    pass

# Función para cerrar la ventana de registro de entrada
def cerrar_ventana():
    ventana_registro_entrada.destroy()

# Crear un marco (frame) para organizar los elementos
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Etiqueta de título
label = customtkinter.CTkLabel(master=frame, text="Registro de Entrada")
label.pack(pady=12, padx=10)

# Campo para ingresar número de cuenta
numero_cuenta_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Número de Cuenta")
numero_cuenta_entry.pack(pady=12, padx=10)

# Campo para ingresar huella dactilar (puedes mostrar una indicación)
huella_dactilar_label = customtkinter.CTkLabel(master=frame, text="Huella Dactilar:")
huella_dactilar_label.pack()

# Botón para registrar entrada
registrar_entrada_button = customtkinter.CTkButton(master=frame, text="Registrar Entrada", command=registrar_entrada)
registrar_entrada_button.pack(pady=12, padx=10)

# Iniciar la interfaz gráfica
root.mainloop()