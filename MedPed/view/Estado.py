import os
from customtkinter import *
from PIL import Image
from datetime import datetime


def estado():
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
    ).place(relx = 0.8, rely = 0.05 , anchor = CENTER)


    #Fecha Actual


    fecha_actual = datetime.now().strftime(" %d / %m / %Y")  

    fecha_label = CTkLabel(
        myFrame, 
        text=fecha_actual,  
        font=("Arial", 30, "bold"), 
        fg_color='transparent',
    ).place(relx=0.5, rely=0.2, anchor=CENTER) 

    #Imagen Usuario

    usuario = os.path.join(os.path.dirname(__file__), "../img/usuario.png")

    my_image3 = CTkImage(light_image=Image.open(usuario),dark_image=Image.open(usuario),size=(200, 200))
    CTkLabel(
        myFrame, 
        image=my_image3, 
        text=""
    ).place(relx = 0.5, rely=0.4, anchor=CENTER) 

    #Nombre del trabajador Igual hay que colocar una funcion que me permita ver el nombre del trabajador

    numero_clientes = CTkLabel(
        myFrame, 
        text= "Juan",
        font=("Arial", 30 ,"bold"), 
        fg_color='transparent',
    ).place(relx=0.5, rely=0.6, anchor=CENTER) 

    #Clientes Faltantes implementar una funcion que me permita ver el numero de clientes que faltan por atender
    CTkLabel(
        myFrame, 
        text=200,
        font=("Arial", 80), 
        fg_color='transparent',
    ).place(relx=0.23, rely=0.72, anchor=CENTER) 


    CTkLabel(
        myFrame, 
        text= "CLIENTES \n FALTANTES",
        font=("Arial", 30 ,"bold"), 
        fg_color='transparent',
    ).place(relx=0.23, rely=0.9, anchor=CENTER) 


    #Clientes registrado implementar una funcion que me permita ver el numero de clientes registrados
    CTkLabel(
        myFrame, 
        text=100,
        font=("Arial", 80), 
        fg_color='transparent',
    ).place(relx=0.73, rely=0.72, anchor=CENTER) 

    CTkLabel(
        myFrame, 
        text= "CLIENTES \n REGISTRADOS",
        font=("Arial", 30 ,"bold"), 
        fg_color='transparent',
    ).place(relx=0.73, rely=0.9, anchor=CENTER) 



    Myinicio.mainloop()

def goInit():
    global Myinicio
    Myinicio.destroy()
    from view.Inicio import windowInicio  
    windowInicio()      



