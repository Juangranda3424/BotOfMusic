import os
from customtkinter import *
from tkinter import PhotoImage
from PIL import Image
from datetime import datetime

def Registro():
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

    #Datos

    CTkLabel(
        myFrame, 
        text="Datos",
        font=("Arial", 40, "bold"), 
        fg_color='transparent',
    ).place(relx=0.5, rely=0.16, anchor=CENTER) 


    #Colocar una funcion que me de el numero del medidor
    CTkLabel(
        myFrame, 
        text="MED-1011",
        font=("Arial", 20), 
        fg_color='transparent',
        width=160,
        height=50
    ).place(relx=0.73, rely=0.26, anchor=CENTER) 


    CTkLabel(
        myFrame, 
        text="Numero de medidor: ",
        font=("Arial", 20, "bold"), 
        bg_color='transparent'
    ).place(relx=0.25, rely=0.26, anchor=CENTER) 


    #Colocar una funcion que me de el codigo de propiedad


    CTkLabel(
        myFrame, 
        text="COD-1011",
        font=("Arial", 20), 
        fg_color='transparent',
        width=160,
        height=50
    ).place(relx=0.73, rely=0.32, anchor=CENTER) 


    CTkLabel(
        myFrame, 
        text="Codigo de propiedad: ",
        font=("Arial", 20, "bold"), 
        bg_color='transparent'
    ).place(relx=0.24, rely=0.32, anchor=CENTER) 



    #Colocar una funcion que me de el condominio

    CTkLabel(
        myFrame, 
        text="PORTOBELO PRIMERA ETAPA",
        font=("Arial", 20), 
        fg_color='transparent',
        width=160,
        height=50
    ).place(relx=0.73, rely=0.39, anchor=CENTER) 


    CTkLabel(
        myFrame, 
        text=" Condominio: ",
        font=("Arial", 20, "bold"), 
        bg_color='transparent'
    ).place(relx=0.308, rely=0.39, anchor=CENTER) 


    #Colocar una funcion que me de la lectura anterior

    CTkLabel(
        myFrame, 
        text="123",
        font=("Arial", 20), 
        fg_color='transparent',
        width=160,
        height=50
    ).place(relx=0.73, rely=0.46, anchor=CENTER) 


    CTkLabel(
        myFrame, 
        text="Lectura anterior: ",
        font=("Arial", 20, "bold"), 
        bg_color='transparent'
    ).place(relx=0.28, rely=0.46, anchor=CENTER) 



    #Colocar una funcion que me ingrese la lectura actual

    CTkLabel(
        myFrame, 
        text="Lectura actual ",
        font=("Arial", 20, "bold"), 
        bg_color='transparent'
    ).place(relx=0.5, rely=0.52, anchor=CENTER) 

    CTkEntry(
        myFrame, 
        font=("Arial", 20), 
        width=300, 
        height=40, 
        show="*",
        border_color="black"
    ).place(relx=0.5, rely=0.60, anchor=CENTER)

    #Boton de la Foto implementar una funcion que me permita tomar la foto

    icon_path = os.path.join(os.path.dirname(__file__), "../img/camara.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="FOTO",
        font=("Arial", 16), 
        width=150, 
        height= 50, 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon,
        hover_color="black"
    ).place(relx = 0.5, rely = 0.7 , anchor = CENTER)


    #Boton de la Registrar implementar una funcion que me permita REGISTRAR

    icon_path = os.path.join(os.path.dirname(__file__), "../img/mas.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="REGISTRAR",
        font=("Arial", 16), 
        width=150, 
        height= 50, 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon,
        hover_color="black"
    ).place(relx = 0.2, rely = 0.8 , anchor = CENTER)

    #Boton de la Resetear implementar una funcion que me permita Resetear

    icon_path = os.path.join(os.path.dirname(__file__), "../img/menos.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="RESETEAR",
        font=("Arial", 16), 
        width=150, 
        height= 50, 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon,
        hover_color="black"
    ).place(relx = 0.8, rely = 0.8 , anchor = CENTER)

    #Boton de la Siguiente implementar una funcion que me permita Siguiente

    icon_path = os.path.join(os.path.dirname(__file__), "../img/flecha.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(20, 20))

    CTkButton(
        myFrame, 
        text="SIGUIENTE",
        font=("Arial", 16), 
        width=150, 
        height= 50, 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon,
        hover_color="black",
        compound="right"
    ).place(relx = 0.86, rely = 0.9 , anchor = CENTER)



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
