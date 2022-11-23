from tkinter import *
from tkinter import messagebox

class Login:
    def __init__(self, window, title):      
        self.window = window
        self.window.title(title)
        self.window.resizable(False,False)
        #self.window.geometry("916x300")
        self.window.configure(background = 'black')
        #self.window.state("zoomed")
        self.window.wm_attributes("-transparentcolor","#60b26c")#60b26c
        self.window.wm_attributes("-alpha",.85)

        label_usuario = Label(self.window,text="Usuario:",bg='black',fg='white')
        label_usuario.grid(row=0,column=0,padx=(10,1),pady=10)

        self.usuario = Entry(self.window,width=20)
        self.usuario.grid(row=0,column=1,padx=10,pady=10)

        label_password = Label(self.window,text="Contraseña:",bg='black',fg='white')
        label_password.grid(row=1,column=0,padx=(10,1),pady=10)

        self.password = Entry(self.window,width=20)
        self.password.grid(row=1,column=1,padx=10,pady=10)

        self.boton_login = Button(self.window,text="Iniciar sesión",command=self.iniciar_usuario,cursor="hand2")
        self.boton_login.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

    def iniciar_usuario(self):
    	SESION_INICIADA = False
    	admin_user = 'admin'
    	admin_password = 'admin'

    	usuarios = [{'user':'usuario1','password':'2021'},
    				{'user':'usuario2','password':'2022'},
    				{'user':'usuario3','password':'2023'},
    				{'user':'usuario4','password':'2024'}]

    	if self.usuario.get() == admin_user and self.password.get() == admin_password:
    		messagebox.showinfo("Login",f"Bienvenido {admin_user}")
    		SESION_INICIADA = True
    		self.window.destroy()
    		self.interfaz_admin()
    	else:
    		for usuario in usuarios:
    			if self.usuario.get() == usuario['user'] and self.password.get() == usuario['password']:
    				messagebox.showinfo('Login',f'Bienvenido usuario {self.usuario.get()}')
    				SESION_INICIADA = True
    				self.window.destroy()
		    		self.interfaz_usuario()
		    		break
    	if not SESION_INICIADA:
    		messagebox.showinfo('Login',f'Usuario y/o contraseña invalidos.')

    def interfaz_admin(self):
    	self.window = Tk()
    	self.window.title('Interfaz admin')
    	self.window.resizable(False,False)
    	self.window.geometry("600x300")
    	self.window.configure(background = 'green')
    	#self.window.state("zoomed")
    	self.window.wm_attributes("-transparentcolor","#60b26c")#60b26c
    	self.window.wm_attributes("-alpha",.85)
    	self.window.mainloop()

    def interfaz_usuario(self):
    	self.window = Tk()
    	self.window.title('Interfaz usuario')
    	self.window.resizable(False,False)
    	self.window.geometry("600x300")
    	self.window.configure(background = 'blue')
    	#self.window.state("zoomed")
    	self.window.wm_attributes("-transparentcolor","#60b26c")#60b26c
    	self.window.wm_attributes("-alpha",.85)
    	self.window.mainloop()

if __name__ =="__main__":   
    window=Tk()
    iniciar_sesion=Login(window,"Login")
    window.mainloop()