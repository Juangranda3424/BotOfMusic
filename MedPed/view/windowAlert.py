from customtkinter import *


def mostrar_alerta(mensaje="¡Este es un mensaje de alerta!", titulo="Alerta"):
    alerta = CTkToplevel()  # Crear la ventana emergente
    alerta.title(titulo)


    alerta.geometry("300x150+550+100")
    alerta.resizable(0, 0)

    # Asegurar que la ventana de alerta siempre esté encima
    alerta.lift()  # Elevar la ventana para que esté encima de otras
    alerta.attributes("-topmost", 1)  # Mantener la ventana siempre en la parte superior
    alerta.focus_force()  # Asegurar que la ventana de alerta esté activa

    label_mensaje = CTkLabel(alerta, text=mensaje, font=("Arial", 20))
    label_mensaje.pack(pady=20)

    boton_cerrar = CTkButton(alerta, text="Cerrar", command=alerta.destroy)
    boton_cerrar.pack(pady=10)

    alerta.mainloop()  

