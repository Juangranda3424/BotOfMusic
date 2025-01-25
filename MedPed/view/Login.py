import os
from customtkinter import *
from tkinter import PhotoImage
from PIL import Image

Myapp = CTk()


Myapp.title("MEDPED")

Myapp.resizable(0,0)

Myapp.geometry("600x700+450+50")

icon_path = os.path.join(os.path.dirname(__file__), "../img/logo.ico")
Myapp.iconbitmap(icon_path)


myFrame = CTkFrame(Myapp)

myFrame.configure(
    fg_color='transparent', 
    bg_color='transparent',
    width=450, 
    height=550, 
    corner_radius=100, 
    border_color="black", 
    border_width=2
)
myFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

myImg = PhotoImage(file=os.path.join(os.path.dirname(__file__), "../img/acceso.png"))

#Imagenes de fondo Gotas de agua

icon_font = os.path.join(os.path.dirname(__file__), "../img/fondo.png")

my_image = CTkImage(light_image=Image.open(icon_font),dark_image=Image.open(icon_font),size=(100, 100))

CTkLabel(
    myFrame, 
    image=my_image, 
    text=""
).place(relx=0.15, rely=0.25, anchor=CENTER)  

my_image2 = CTkImage(light_image=Image.open(icon_font),dark_image=Image.open(icon_font),size=(75, 75))


CTkLabel(
    myFrame, 
    image=my_image2, 
    text=""
).place(relx=0.8, rely=0.1, anchor=CENTER)  

my_image3 = CTkImage(light_image=Image.open(icon_font),dark_image=Image.open(icon_font),size=(60, 60))


CTkLabel(
    myFrame, 
    image=my_image3, 
    text=""
).place(relx=0.86, rely=0.4, anchor=CENTER) 

CTkLabel(
    myFrame,
    image=myImg, 
    text=None
).place(relx=0.5, rely=0.25, anchor=CENTER)


#Labels y Entry

CTkLabel(
    myFrame, 
    text="Usuario:", 
    font=("Arial", 20), 
    fg_color='transparent'
).place(relx=0.25, rely=0.5, anchor=CENTER)

CTkEntry(
    myFrame, 
    font=("Arial", 20), 
    width=300, 
    height=40
).place(relx=0.5, rely=0.58, anchor=CENTER)

CTkLabel(
    myFrame, 
    text="Contraseña:", 
    font=("Arial", 20)
).place(relx=0.29, rely=0.65, anchor=CENTER)

CTkEntry(
    myFrame, 
    font=("Arial", 20), 
    width=300, 
    height=40, 
    show="*"
).place(relx=0.5, rely=0.73, anchor=CENTER)


#Boton de Login toca hacer una funcion para que se pueda logear

CTkButton(
    myFrame, 
    text="LOGIN", 
    font=("Arial", 20), 
    height=40, 
    fg_color="#2DBAF0", 
    text_color="black",
    hover_color="#B8B8B8", 
    corner_radius=20 
).place(relx=0.68, rely=0.83, anchor=CENTER)


Myapp.mainloop()
