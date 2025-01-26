import os
from customtkinter import *
from PIL import Image


def verRegistro():
    global Myinicio

    Myinicio = CTk()

    Myinicio.title("MEDPED")


    Myinicio.geometry("600x700+450+50")

    icon_path = os.path.join(os.path.dirname(__file__), "../img/logo.ico")
    Myinicio.iconbitmap(icon_path)

    myFrame = CTkFrame(Myinicio, width=600, height=700, fg_color='transparent').place( anchor=CENTER)

    #Boton de Inicio

    icon_path = os.path.join(os.path.dirname(__file__), "../img/casa.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="INICIO", 
        width=120, 
        height= 50,
        font=("Arial", 16), 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon, 
        hover_color="black",
        command=goInit
    ).place(relx = 0.17, rely = 0.05 , anchor = CENTER)

    #Boton de Estado Resgistro

    icon_path = os.path.join(os.path.dirname(__file__), "../img/ojo.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="ESTADO DE REGISTRO",
        font=("Arial", 16), 
        width=240, 
        height= 50, 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon,
        hover_color="black",
        command=gostate
    ).place(relx = 0.74, rely = 0.05 , anchor = CENTER)

    #Registros

    CTkLabel(
        myFrame, 
        text="Registros",
        font=("Arial", 40, "bold"), 
        fg_color='transparent',
    ).place(relx=0.5, rely=0.16, anchor=CENTER) 


    #Busqueda implementar una barra de busqueda
    CTkEntry(
        myFrame, 
        font=("Arial", 20), 
        width=400, 
        height=40
    ).place(relx=0.4, rely=0.24, anchor=CENTER)


    icon_path = os.path.join(os.path.dirname(__file__), "../img/lupa.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="Buscar",
        font=("Arial", 16), 
        width=100, 
        height= 40, 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon,
        hover_color="black"
    ).place(relx = 0.85, rely = 0.24 , anchor = CENTER)



    #Subir a la Nube implementar subir a la nube

    icon_path = os.path.join(os.path.dirname(__file__), "../img/nube.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="SUBIR A LA NUBE", 
        width=250, 
        height= 50,
        font=("Arial", 16), 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon, 
        hover_color="black"
    ).place(relx = 0.28, rely = 0.9 , anchor = CENTER)

    #Boton de Ver Registro

    icon_path = os.path.join(os.path.dirname(__file__), "../img/lapiz.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="EDITAR", 
        width=250, 
        height= 50,
        font=("Arial", 16), 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon, 
        hover_color="black"
    ).place(relx = 0.72, rely = 0.9, anchor = CENTER)



    Myinicio.mainloop()


def goInit():
    global Myinicio
    Myinicio.destroy()
    from view.Inicio import windowInicio  
    windowInicio()      


def gostate():
    global Myinicio
    Myinicio.destroy()
    from view.Estado import estado
    estado()



