

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

# Crear ventana principal
root = customtkinter.CTk()
root.title("Registro de Usuarios")
root.geometry("680x450")

# Función para registrar usuario
def registrar_usuario():
    # Agrega aquí la lógica para registrar al usuario en la base de datos
    pass

# Función para cerrar la aplicación
def cerrar_aplicacion():
    root.destroy()

# Crear un marco (frame) para organizar los elementos
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Etiqueta de título
label = customtkinter.CTkLabel(master=frame, text="Registro de Usuarios")
label.pack(pady=12, padx=10)

# Campos para ingresar datos
nombre_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Nombre")
nombre_entry.pack(pady=12, padx=10)

apellido_paterno_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Apellido Paterno")
apellido_paterno_entry.pack(pady=12, padx=10)

apellido_materno_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Apellido Materno")
apellido_materno_entry.pack(pady=12, padx=10)

numero_cuenta_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Número de Cuenta")
numero_cuenta_entry.pack(pady=12, padx=10)

carrera_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Carrera/Licenciatura")
carrera_entry.pack(pady=12, padx=10)

huella_dactilar_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Huella Dactilar")
huella_dactilar_entry.pack(pady=12, padx=10)

# Botón para registrar usuario
registrar_button = customtkinter.CTkButton(master=frame, text="Registrar Usuario", command=registrar_usuario)
registrar_button.pack(pady=12, padx=10)

# Configurar el cierre de la aplicación al cerrar la ventana principal
root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

# Iniciar la interfaz gráfica
root.mainloop()