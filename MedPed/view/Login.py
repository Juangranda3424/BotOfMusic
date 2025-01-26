import os
from customtkinter import *
from tkinter import PhotoImage
from PIL import Image
from model.User import User



class Login:
    def __init__(self):
        self.Myapp = CTk()
        self.Myapp.title("MEDPED")
        self.Myapp.resizable(0,0)
        self.Myapp.geometry("600x700+450+50")
        icon_path = os.path.join(os.path.dirname(__file__), "../img/logo.ico")
        self.Myapp.iconbitmap(icon_path)
        myFrame = CTkFrame(self.Myapp)

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

        fondo = os.path.join(os.path.dirname(__file__), "../img/fondo.png")

        Gota_1 = CTkImage(light_image=Image.open(fondo),dark_image=Image.open(fondo),size=(100, 100))

        CTkLabel(
            myFrame, 
            image=Gota_1, 
            text=""
        ).place(relx=0.15, rely=0.25, anchor=CENTER)  

        Gota_2 = CTkImage(light_image=Image.open(fondo),dark_image=Image.open(fondo),size=(75, 75))


        CTkLabel(
            myFrame, 
            image=Gota_2, 
            text=""
        ).place(relx=0.8, rely=0.1, anchor=CENTER)  

        Gota_3 = CTkImage(light_image=Image.open(fondo),dark_image=Image.open(fondo),size=(60, 60))


        CTkLabel(
            myFrame, 
            image=Gota_3, 
            text=""
        ).place(relx=0.86, rely=0.4, anchor=CENTER) 

        CTkLabel(
            myFrame,
            image=myImg, 
            text=None
        ).place(relx=0.5, rely=0.25, anchor=CENTER)


        # Labels y Entry
        CTkLabel(
            myFrame, 
            text="Usuario:", 
            font=("Arial", 20), 
            fg_color='transparent'
        ).place(relx=0.25, rely=0.5, anchor=CENTER)

        self.user_entry = CTkEntry(  # Cambia el nombre para guardar el objeto del Entry
            myFrame, 
            font=("Arial", 20), 
            width=300, 
            height=40
        )
        self.user_entry.place(relx=0.5, rely=0.58, anchor=CENTER)

        CTkLabel(
            myFrame, 
            text="Contraseña:", 
            font=("Arial", 20)
        ).place(relx=0.29, rely=0.65, anchor=CENTER)

        self.password_entry = CTkEntry(  # Cambia el nombre para guardar el objeto del Entry
            myFrame, 
            font=("Arial", 20), 
            width=300, 
            height=40, 
            show="•"
        )
        self.password_entry.place(relx=0.5, rely=0.73, anchor=CENTER)


        #Boton de Login toca hacer una funcion para que se pueda logear

        CTkButton(
            myFrame, 
            text="LOGIN", 
            font=("Arial", 20), 
            height=40, 
            fg_color="#2DBAF0", 
            text_color="black",
            hover_color="#B8B8B8", 
            corner_radius=20,
            command= lambda: self.verificate(self.user_entry.get(),self.password_entry.get())
        ).place(relx=0.68, rely=0.83, anchor=CENTER)

        self.Myapp.mainloop()
    
    def verificate(self, userInput,passwordInput):
        user = User()
        if userInput == user.get_user() and passwordInput == user.get_password():
            self.Myapp.destroy()
            from view.Inicio import windowInicio
            windowInicio()
        else:
            from view.windowAlert import mostrar_alerta
            mostrar_alerta("Credenciales incorrectas", "Error")


if __name__ == "__main__":
    login = Login()

        


    








