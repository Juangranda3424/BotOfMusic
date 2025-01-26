import os
from customtkinter import *
from PIL import Image
from datetime import datetime

def windowInicio():

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
        hover_color="black"
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

    #Imagen Usuario

    usuario = os.path.join(os.path.dirname(__file__), "../img/usuario.png")

    my_image3 = CTkImage(light_image=Image.open(usuario),dark_image=Image.open(usuario),size=(200, 200))
    CTkLabel(
        myFrame, 
        image=my_image3, 
        text=""
    ).place(relx = 0.27, rely=0.35, anchor=CENTER) 


    #Fecha Actual


    fecha_actual = datetime.now().strftime(" %d / %m / %Y")  

    CTkLabel(
        myFrame, 
        text=fecha_actual,  
        font=("Arial", 30), 
        fg_color='transparent',
    ).place(relx=0.73, rely=0.25, anchor=CENTER) 


    #Numero de clientes
    # Hay que colocar una funcion que me permita ver el numero de clientes que se han registrado

    CTkLabel(
        myFrame, 
        text="Clientes Totales",
        font=("Arial", 30), 
        fg_color='transparent',
    ).place(relx=0.73, rely=0.32, anchor=CENTER) 




    CTkLabel(
        myFrame, 
        text=300,
        font=("Arial", 90), 
        fg_color='transparent',
    ).place(relx=0.73, rely=0.42, anchor=CENTER) 

    #Nombre del trabajador Igual hay que colocar una funcion que me permita ver el nombre del trabajador

    CTkLabel(
        myFrame, 
        text= "Juan",
        font=("Arial", 30), 
        fg_color='transparent',
    ).place(relx=0.27, rely=0.54, anchor=CENTER) 

    #Boton de Iniciar Registro

    icon_path = os.path.join(os.path.dirname(__file__), "../img/mas.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame,
        text="INICIAR REGISTRO", 
        width=290, 
        height= 60,
        font=("Arial", 16), 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon, 
        hover_color="black",
        command=goRegister
    ).place(relx = 0.25, rely = 0.7 , anchor = CENTER)


    #Boton de Ver Registro

    icon_path = os.path.join(os.path.dirname(__file__), "../img/lapiz.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="VER REGISTROS", 
        width=290, 
        height= 60,
        font=("Arial", 16), 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon, 
        hover_color="black",
        command=goViewRegister
    ).place(relx = 0.75, rely = 0.7, anchor = CENTER)


    #Boton de Clientes

    icon_path = os.path.join(os.path.dirname(__file__), "../img/avatar.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(20, 20))

    CTkButton(
        myFrame, 
        text="CLIENTES",
        width=290, 
        height= 60,
        font=("Arial", 16), 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon, 
        hover_color="black"
    ).place(relx = 0.25, rely = 0.8 , anchor = CENTER)


    #Continuar Registros

    icon_path = os.path.join(os.path.dirname(__file__), "../img/formulario-de-contacto.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="CONTINUAR REGISTRO", 
        width=290, 
        height= 60,
        font=("Arial", 16), 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon, 
        hover_color="black",
        command=goRegister
    ).place(relx = 0.75, rely = 0.8 , anchor = CENTER)


    #Subir a la Nube implementar subir a la nube

    icon_path = os.path.join(os.path.dirname(__file__), "../img/nube.png")

    icon_image = Image.open(icon_path)

    my_icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(16, 16))

    CTkButton(
        myFrame, 
        text="SUBIR A LA NUBE", 
        width=290, 
        height= 50,
        font=("Arial", 16), 
        corner_radius=3, 
        text_color="white", 
        fg_color="#2DBAF0",
        image=my_icon, 
        hover_color="black"
    ).place(relx = 0.5, rely = 0.9 , anchor = CENTER)



    Myinicio.mainloop()


def gostate():
    global Myinicio
    Myinicio.destroy()
    from view.Estado import estado
    estado()


def goRegister():
    global Myinicio
    Myinicio.destroy()
    from view.Registro import Registro
    Registro()    

def goViewRegister():
    global Myinicio
    Myinicio.destroy()
    from view.VerRegistros import verRegistro
    verRegistro()        