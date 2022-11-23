#Creador: Roberto Alan Rodriguez Monroy
from tkinter import *
from tkinter import ttk,filedialog,messagebox
from tkinter.ttk import Combobox
from ttkthemes import ThemedTk
import json
from api_manage_data import Manage
from operator import itemgetter
import os
#from buscar_info import Buscar

class Login:
    def __init__(self, window, title):
        self.fondo = 'black'; self.letra = 'white' ; self.color_check = 'black'      
        self.window = window
        self.window.title(title)
        self.window.resizable(False,False)
        #self.window.geometry("916x300")
        self.window.configure(background = self.fondo)
        #self.window.state("zoomed")
        self.window.wm_attributes("-transparentcolor","#60b26c")#60b26c
        self.window.wm_attributes("-alpha",.85)
        self.menu()
        self.control_mostrar_pasos = False
        self.window.bind("<Control-g>",self.reacomodar)
        self.window.bind("<Alt-e>",self.editar_casos)
        self.ARCHIVO_NUEVO = False

    def abrir_matriz(self):
        ruta_programa = os.getcwd()
        self.archivo_json = filedialog.askopenfilename(title="Abrir", initialdir = ruta_programa,filetypes = [("Archivo json","*.json")])
        llamar_manage = Manage()
        llamar_manage.memoria_guardar_archivo_json(self.archivo_json)
        self.insertar_valores_tabla()

    # VERIFICAR SI HAY UN ARCHIVO ABIERTO ANTERIORMENTE #
    def verificar_archivo_configuracion(self):
        llamar_manage = Manage() 
        try:
            self.archivo_json = llamar_manage.memoria_archivo_json()
            self.insertar_valores_tabla()
        except Exception as e:
            print(f"Aviso: no existe ningun archivo en el historial para abrir.")

    # FUNCION COMPLEMENTO DE 'CREAR_MATRIZ' PARA MANDAR EL NOMBRE DEL ARCHIVO #
    def mandar_archivo(self,event):
        if self.nombre_matriz.get() == '':
            messagebox.showinfo('Error','Registrar un nombre para la matriz')
        else:
            llamar_manage = Manage()
            llamar_manage.crear_json_matriz(self.nombre_matriz.get()) #Crear el json de la matriz
            llamar_manage.memoria_guardar_archivo_json(f'matrices/{self.nombre_matriz.get()}.json') #Guardar la ruta en la
            self.top_crear_matriz.destroy() #Destruir la interfaz para registrar nombre
            self.insertar_valores_tabla() #Actualizar tabla
            self.ARCHIVO_NUEVO = True
            self.crear_casos()

    # FUNCION PARA CREAR INTERFAZ PARA CREAR MATRIZ #
    def crear_matriz(self):
        self.top_crear_matriz=Toplevel()
        self.top_crear_matriz.title("Nueva matriz de prueba")
        self.top_crear_matriz.grab_set()
        self.top_crear_matriz.transient(master=None)
        self.top_crear_matriz.resizable(False, False)
        self.top_crear_matriz.configure(bg = "white")#ffffff
        #self.window.wm_attributes("-transparentcolor","#60b26c")#60b26c
        self.top_crear_matriz.wm_attributes("-alpha",.95)

        registros = Label(self.top_crear_matriz,text="Nombre de la matriz: ",bg="white",font=("Arial",12))
        registros.grid(row=0,column=0,sticky="e")
        self.nombre_matriz = Entry(self.top_crear_matriz,width=20,justify=CENTER,font=("Arial",12))
        self.nombre_matriz.grid(row=0,column=1,pady=5,padx=5,sticky="w")
        self.nombre_matriz.bind('<Return>',self.mandar_archivo)

        
    def menu(self):
        style = ttk.Style()
        style.configure("Treeview")
        style.map("Treeview", background=[("selected","#38022D")])

        #__________________________________Barra menu___________________________________
        barramenu=Menu(self.window) 
        self.window.config(menu=barramenu)
        Archivo=Menu(barramenu,tearoff=0)
        Ayuda=Menu(barramenu,tearoff=0)
        barramenu.add_cascade(label="Abrir matriz",menu=Archivo)
        barramenu.add_cascade(label="Ayuda",menu=Ayuda)
        #Submenus
        Archivo.add_command(label="Abrir matriz",command=self.abrir_matriz)
        Archivo.add_command(label="Crear nueva matriz",command=self.crear_matriz)

        registros = Label(self.window,text="Casos de prueba: ",fg=self.letra,bg=self.fondo,font=("Arial",12))
        registros.grid(row=0,column=0,sticky="e")
        self.cantidad_registros = Entry(self.window,width=10,justify=CENTER,font=("Arial",12))
        self.cantidad_registros.grid(row=0,column=1,pady=5,sticky="w")

        label_busqueda = Label(self.window,text="Busqueda por: ",fg=self.letra,bg=self.fondo,font=("Arial",12))
        label_busqueda.grid(row=1,column=0,sticky="e",pady=10)
        self.buscador = ttk.Entry(self.window, font=("Arial",12),width=20)
        self.buscador.grid(row=1,column=1, pady=10,sticky="w")
        self.buscador.bind("<KeyRelease>",self.buscar)

        self.tabla = ttk.Treeview(self.window)
        self.tabla["columns"] = ("ID","Nombre","Descripción")
        self.tabla.column("#0",width=0,stretch=NO)
        self.tabla.column("ID",anchor=CENTER,width=60)
        self.tabla.column("Nombre",anchor=CENTER,width=300)
        self.tabla.column("Descripción",anchor=CENTER,width=500)

        self.tabla.heading("#0",text="",anchor=CENTER)
        self.tabla.heading("ID",text="ID",anchor=CENTER)
        self.tabla.heading("Nombre",text="Nombre",anchor=CENTER)
        self.tabla.heading("Descripción",text="Descripción",anchor=CENTER)

        self.tabla.grid(row=2,column=0,sticky="nw",columnspan=2)
        #self.window.bind('<Control-Up>', self.mover)      # forward-slash
        self.window.bind('<Control-w>', self.mover) 
        self.window.bind('<Control-s>', self.mover)  # backslash
        #self.tabla.place(x=0,y=0)
        self.scrollvert=Scrollbar(self.window,command=self.tabla.yview)
        self.scrollvert.place(in_=self.tabla,relx=1, relheight=1, bordermode="outside")
        self.tabla.config(yscrollcommand=self.scrollvert.set)

        frame_debajo_scroll = Frame(self.window,width=17)
        frame_debajo_scroll.grid(row=2,column=2,sticky="s")

        def pop_menu(event):
            menu.tk_popup(event.x_root,event.y_root)

        menu = Menu(self.tabla, tearoff=0, bg="black", fg="white")
        menu.add_command(label="Agregar caso de prueba", command=self.crear_casos)
        menu.add_command(label="Editar", command=self.editar_casos)
        menu.add_command(label="Eliminar", command=self.eliminar)
        menu.add_command(label="Guardar tabla (Control + G)", command=self.reacomodar)
        menu.add_command(label="Mostrar/ocultar pasos", command=self.mostrar_pasos)
        menu.add_separator()
        menu.add_command(label="Exportar a excel...", command=self.exportar_excel)
        menu.add_command(label="Ayuda")
        self.tabla.bind("<Button-3>", pop_menu)
        self.tabla.bind("<Up>", self.insertar_pasos)
        self.tabla.bind("<Down>", self.insertar_pasos)
        self.tabla.bind("<Double-Button-1>", self.insertar_pasos)
        self.tabla.bind("<Control-e>", self.editar_casos)

        creador = Label(self.window,text="Creado por Roberto Alan Rodriguez Monroy",fg=self.letra,bg=self.fondo,font=("Arial",8))
        creador.grid(row=3,column=0,padx=10,columnspan=2)

        self.verificar_archivo_configuracion()

    def buscar(self, event): #Buscador de elementos en la DB
        llamar_manage=Manage()
        self.tabla.delete(*self.tabla.get_children())
        data = llamar_manage.buscar(self.buscador.get())

        # Registrar la cantidad de registros en un entry #
        self.CANTIDAD_REGISTROS_0=len(data)
        self.cantidad_registros.configure(state="normal")
        self.cantidad_registros.delete(0, END)
        self.cantidad_registros.insert(0,self.CANTIDAD_REGISTROS_0)
        self.cantidad_registros.configure(state="disabled")
        self.diccionario_informacion = data

        # INSERTAR LOS DATOS EN LA TABLA #
        for i in data:
            self.tabla.insert(parent="",index="end",text="",values=(i['id'],i['NOMBRE'],i['DESCRIPCION']))
    
    # MOSTRAR E INSERTAR PASOS #
    def insertar_pasos(self, event=str()):
        if self.control_mostrar_pasos == True:
            seleccion = self.tabla.focus()
            values = self.tabla.item(seleccion,"values")
            if values == "":
                pass
            else:
                if event.keysym == "Up" or event.keysym == "Down":
                    ENCONTRAR = False
                    datos = self.tabla.get_children()
                    lista_valores = list()
                    valor_final = tuple()
                    for dato in datos:
                        values0 = self.tabla.item(dato,"values")
                        lista_valores.append(values0)
                        if ENCONTRAR:
                            valor_final = values0
                            break
                        if values0[0] == values[0]:
                            posicion = lista_valores.index(values0)
                            if event.keysym == "Up":
                                valor_final = lista_valores[posicion - 1]
                            elif event.keysym == "Down":
                                ENCONTRAR = True
                                pass
                    if not valor_final:
                        valor_final = lista_valores.pop()
                elif event.num == 1:
                    valor_final = values

                self.text_mostrar_pasos.configure(state="normal")
                self.text_mostrar_pasos.delete(1.0, END)
                llamar_manage = Manage()
                diccionario = llamar_manage.buscar_dato_json(valor_final[0])
                for i in diccionario['PASOS']:
                    self.text_mostrar_pasos.insert(END, i + '\n')
                self.text_mostrar_pasos.configure(state="disabled")

    def mostrar_pasos(self):
        if not self.control_mostrar_pasos:
            self.control_mostrar_pasos = True
            self.text_mostrar_pasos = Text(self.window,width=40,height=12,border=2,wrap="word",font=("Times New Roman", 12))
            self.text_mostrar_pasos.grid(row=2,column=3,padx=20,pady=10,sticky="n")

            self.scrollvert_0=Scrollbar(self.window,command=self.text_mostrar_pasos.yview)
            self.scrollvert_0.place(in_=self.text_mostrar_pasos,relx=1, relheight=1, bordermode="inside")
            self.text_mostrar_pasos.config(yscrollcommand=self.scrollvert_0.set)
            self.insertar_pasos()
        else:
            self.control_mostrar_pasos = False
            self.text_mostrar_pasos.destroy()
            self.scrollvert_0.destroy()

    def crear_casos(self):          #Interfaz para realizar registros de casos
        self.top=Toplevel()
        self.top.title("Registro caso de prueba")
        self.top.grab_set()
        self.top.transient(master=None)
        self.top.resizable(False, False)
        self.top.configure(bg = "white")#ffffff
        #self.window.wm_attributes("-transparentcolor","#60b26c")#60b26c
        self.top.wm_attributes("-alpha",.95)
        self.top.bind("<Control-g>",self.guardar_datos)

        registros = Label(self.top,text="Número de registro: ",bg="white",font=("Arial",12))
        registros.grid(row=0,column=0,sticky="e")
        self.numero_registro = Entry(self.top,width=10,justify=CENTER,font=("Arial",12))
        self.numero_registro.grid(row=0,column=1,pady=5,sticky="w")
        if self.ARCHIVO_NUEVO:
            numero_registro = 1
            self.ARCHIVO_NUEVO = False
        else:
            numero_registro = self.CANTIDAD_REGISTROS_0 + 1
        self.numero_registro.insert(END,numero_registro)
        self.numero_registro.configure(state="disabled")
        
        self.registrar_nombre = ttk.Entry(self.top,width=40,font=("Times New Roman", 12))
        self.registrar_nombre.grid(row=1,column=0,padx=10,pady=5,columnspan=2)
        #self.registrar_nombre.bind("<Key>",self.mover_registro)

        self.registrar_descripcion = Text(self.top,width=50,height=5,border=2,wrap="word",font=("Times New Roman", 12))
        self.registrar_descripcion.grid(row=2,column=0,padx=20,pady=5)
        self.scrollvert0=Scrollbar(self.top,command=self.registrar_descripcion.yview)
        self.scrollvert0.place(in_=self.registrar_descripcion,relx=1, relheight=1, bordermode="inside")
        self.registrar_descripcion.config(yscrollcommand=self.scrollvert0.set)

        self.registrar_resultado_general = Text(self.top,width=50,height=5,border=2,wrap="word",font=("Times New Roman", 12))
        self.registrar_resultado_general.grid(row=2,column=1,padx=20,pady=5)
        #self.registrar_descripcion.bind("<Key>",self.mover_registro)

        self.scrollvert0_1=Scrollbar(self.top,command=self.registrar_resultado_general.yview)
        self.scrollvert0_1.place(in_=self.registrar_resultado_general,relx=1, relheight=1, bordermode="inside")
        self.registrar_resultado_general.config(yscrollcommand=self.scrollvert0_1.set)

        self.registrar_pasos = Text(self.top,width=50,height=5,border=2,wrap="word",font=("Times New Roman", 12))
        self.registrar_pasos.grid(row=3,column=0,padx=20,pady=5)
        #self.registrar_pasos.bind("<Key>",self.mover_registro)

        self.scrollvert1=Scrollbar(self.top,command=self.registrar_pasos.yview)
        self.scrollvert1.place(in_=self.registrar_pasos,relx=1, relheight=1, bordermode="inside")
        self.registrar_pasos.config(yscrollcommand=self.scrollvert1.set)

        self.registrar_resultado = Text(self.top,width=50,height=5,border=2,wrap="word",font=("Times New Roman", 12))
        self.registrar_resultado.grid(row=3,column=1,padx=20,pady=5)

        self.scrollvert2=Scrollbar(self.top,command=self.registrar_resultado.yview)
        self.scrollvert2.place(in_=self.registrar_resultado,relx=1, relheight=1, bordermode="inside")
        self.registrar_resultado.config(yscrollcommand=self.scrollvert2.set)

        #estilo = ttk.Style()
        #estilo.configure("W.TButton", font = ('Arial', 10, 'bold'),foreground = 'black',background="white")
        #estilo.map('TButton', foreground = [('active', '!disabled', '#38022D')],background = [('active', '#38022D')])
        
        button_editar = ttk.Button(self.top,style='W.TButton',text="Guardar",cursor="hand2",command=self.guardar_datos)
        #button_editar.place(x=200,y=250)
        button_editar.grid(row=4,column=0,pady=5,columnspan=2)

    def mover_registro(self, event):    #Moverte con las flechas del teclado dentro de los campos de registro
        widgets=[self.registrar_nombre,self.registrar_descripcion,self.registrar_pasos]
        if event.keysym == "Down":
            try:
                x=widgets.index(event.widget)
                c=widgets[x+1]
                c.focus()
            except IndexError:
                pass
        elif event.keysym == "Up":
            try:
                x=widgets.index(event.widget)
                c=widgets[x-1]
                c.focus()
            except IndexError:
                pass

    def mover(self,event):              #Mover los registros dentro de la tabla
        if event.keysym == "w":
            rows= self.tabla.selection()
            for row in rows:
                self.tabla.move(row,self.tabla.parent(row),self.tabla.index(row)-1)
        elif event.keysym == "s":
            rows= self.tabla.selection()
            for row in reversed(rows):
                self.tabla.move(row,self.tabla.parent(row),self.tabla.index(row)+1)             

    def reacomodar(self,event=0):               #Reorganizar la tabla despues de mover datos "Control-g"
        datos = self.tabla.get_children()
        lista_nueva = list()
        numero_inicio = 0
        for numero,i in enumerate(datos,start=numero_inicio):
            values = self.tabla.item(i,"values")
            for vacio in self.diccionario_informacion:
                if int(values[0]) == vacio["id"]:
                    vacio["id"] = numero + 1
                    self.diccionario_informacion.remove(vacio)
                    lista_nueva.append(vacio)

        #sorted_diccionario = sorted(self.diccionario_informacion, key=itemgetter("id"))
        llamar_manage = Manage()
        llamar_manage.guardar_reacomodo(lista_nueva)
        self.insertar_valores_tabla()

    def editar_casos(self,event=0):                 #Interfaz grafica para editar casos de prueba
        seleccion = self.tabla.focus()
        values = self.tabla.item(seleccion,"values")

        if values =="":
            messagebox.showinfo("Error","No ha seleccionado un registro")
        else:
            self.top=Toplevel()
            self.top.title("Editar caso de prueba")
            self.top.grab_set()
            self.top.transient(master=None)
            self.top.resizable(False, True)
            self.top.configure(bg = "#ffffff")
            self.top.bind("<Control-g>",self.actualizar_datos)

            self.texto_nombre = StringVar()
            self.texto_nombre.set("Nombre del caso de prueba")
            self.editar_nombre = ttk.Entry(self.top,width=40,textvariable=self.texto_nombre,font=("Times New Roman", 12))
            self.editar_nombre.grid(row=1,column=0,padx=10,pady=5,columnspan=2)
            #self.editar_nombre.bind("<Key>",self.mover)
            self.texto_descripcion = StringVar()
            self.texto_descripcion.set("Descripción del caso de prueba")

            self.editar_descripcion = Text(self.top,width=50,height=5,border=2, wrap="word",font=("Times New Roman", 12))
            self.editar_descripcion.grid(row=2,column=0,padx=20,pady=5)
            self.scrollvert0=Scrollbar(self.top,command=self.editar_descripcion.yview)
            self.scrollvert0.place(in_=self.editar_descripcion,relx=1, relheight=1, bordermode="outside")
            self.editar_descripcion.config(yscrollcommand=self.scrollvert0.set)

            self.editar_resultado_general = Text(self.top,width=50,height=5,border=2, wrap="word",font=("Times New Roman", 12))
            self.editar_resultado_general.grid(row=2,column=1,padx=20,pady=5)
            self.scrollvert0_1=Scrollbar(self.top,command=self.editar_resultado_general.yview)
            self.scrollvert0_1.place(in_=self.editar_resultado_general,relx=1, relheight=1, bordermode="outside")
            self.editar_resultado_general.config(yscrollcommand=self.scrollvert0_1.set)

            self.editar_pasos = Text(self.top,width=50,height=5,border=2,wrap="word",font=("Times New Roman", 12))
            self.editar_pasos.grid(row=3,column=0,padx=20,pady=5)
            self.scrollvert1=Scrollbar(self.top,command=self.editar_pasos.yview)
            self.scrollvert1.place(in_=self.editar_pasos,relx=1, relheight=1, bordermode="outside")
            self.editar_pasos.config(yscrollcommand=self.scrollvert1.set)

            self.editar_resultados = Text(self.top,width=50,height=5,border=2,wrap="word",font=("Times New Roman", 12))
            self.editar_resultados.grid(row=3,column=1,padx=20,pady=5)
            self.scrollvert2=Scrollbar(self.top,command=self.editar_resultados.yview)
            self.scrollvert2.place(in_=self.editar_resultados,relx=1, relheight=1, bordermode="outside")
            self.editar_resultados.config(yscrollcommand=self.scrollvert2.set)

            self.insertar_valores_casos(values)
            estilo = ttk.Style()
            """
            estilo.configure("W.TButton", font = ('Arial', 10, 'bold'),
                foreground = 'black',background="white")
            estilo.map('TButton', foreground = [('active', '!disabled', '#38022D')],
                     background = [('active', '#38022D')])"""
            button_editar = ttk.Button(self.top,style='W.TButton',text="Guardar",cursor="hand2",command=self.actualizar_datos)
            button_editar.grid(row=4,column=0)          #Ventana grafica para editar los casos

            button_documentacion = ttk.Button(self.top,style='W.TButton',text="Crear documentación",cursor="hand2",command=self.crear_word)
            button_documentacion.grid(row=4,column=1)          #Ventana grafica para editar los casos

    def guardar_datos(self, event=0):
        if self.registrar_nombre.get() == "":
            messagebox.showinfo("Error","El registro debe tener como minimo nombre")
        else:
            diccionario = {'nombre':self.registrar_nombre.get(),
                        'descripcion':self.registrar_descripcion.get(1.0,END),
                        'resultado_general':self.registrar_resultado_general.get(1.0,END),
                        'pasos':self.registrar_pasos.get(1.0,END),
                        'resultado':self.registrar_resultado.get(1.0,END)}
            llamar_manage = Manage()
            llamar_manage.guardar_datos_json(diccionario)
            messagebox.showinfo('Completado','Registro completado')

            self.insertar_valores_tabla()
            self.numero_registro.configure(state="normal")
            self.numero_registro.delete(0,END)
            numero_registro = self.CANTIDAD_REGISTROS_0 + 1
            self.numero_registro.insert(END,numero_registro)
            self.numero_registro.configure(state="disabled")
            self.registrar_nombre.delete(0, END)
            self.registrar_descripcion.delete(1.0, END)
            self.registrar_resultado_general.delete(1.0, END)
            self.registrar_pasos.delete(1.0, END)
            self.registrar_resultado.delete(1.0, END)
    
    def actualizar_datos(self,event=0):
        diccionario = {'identificador':self._valor_id,
                    'nombre':self.editar_nombre.get(),
                    'descripcion':self.editar_descripcion.get(1.0,END),
                    'resultado_general':self.editar_resultado_general.get(1.0,END),
                    'pasos':self.editar_pasos.get(1.0,END),
                    'resultado':self.editar_resultados.get(1.0,END)}
        llamar_manage = Manage()
        llamar_manage.actualizar_datos_json(diccionario)
        messagebox.showinfo("Completado","Caso actualizado.")
        self.top.destroy()
        self.insertar_valores_tabla()

    def insertar_valores_casos(self,values):
        self._valor_id=values[0]  #Aqui guarda el valor del ID para futuras operaciones
        self.editar_nombre.delete(0, END)
        self.editar_nombre.insert(END,values[1])  #Se introducen toodos los valores de la tabla a los Entry's
        self.editar_descripcion.insert(END,values[2])
        llamar_manage = Manage()
        diccionario = llamar_manage.buscar_dato_json(self._valor_id)
        try:
            self.editar_resultado_general.insert(END,diccionario['RESULTADO_GENERAL'])
        except Exception as e:
            print(e)
        try:
            for i in diccionario['PASOS']:
                self.editar_pasos.insert(END, i + '\n')
        except Exception as e:
            print(e)

        try:
            for i in diccionario['RESULTADO']:
                self.editar_resultados.insert(END, i + '\n')
        except Exception as e:
            print(e)

    def insertar_valores_tabla(self):
        self.tabla.delete(*self.tabla.get_children())                   #Eliminar valores actuales de la tabla
        llamar_manage = Manage()                                        
        data=llamar_manage.get_info_json()                              #Llamar funcion para recuperar los datos del json

        # Registrar la cantidad de registros en un entry #
        try:
            self.CANTIDAD_REGISTROS_0=len(data)
        except Exception as e:
            self.CANTIDAD_REGISTROS_0 = 0
        self.cantidad_registros.configure(state="normal")
        self.cantidad_registros.delete(0, END)
        self.cantidad_registros.insert(0,self.CANTIDAD_REGISTROS_0)
        self.cantidad_registros.configure(state="disabled")
        self.diccionario_informacion = data

        # INSERTAR LOS DATOS EN LA TABLA #
        try:
            for i in data:
                self.tabla.insert(parent="",index="end",text="",values=(i['id'],i['NOMBRE'],i['DESCRIPCION']))
        except Exception as e:
            print('No hay datos en la matriz')

    def eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showinfo("Error","No ha seleccionado un registro")
        else:
            decision2=messagebox.askquestion("Confirmar","¿Seguro que quieres eliminar el registro?")
            if decision2 == "yes":
                llamar_manage=Manage()
                for valor_eliminar in seleccion:
                    values = self.tabla.item(valor_eliminar,"values")
                    llamar_manage.eliminar_dato(int(values[0]))
                messagebox.showinfo("Completado","Registro eliminado.")
                self.insertar_valores_tabla()

    def exportar_excel(self):
        llamar_manage = Manage()
        llamar_manage.exportar_excel()

    def crear_word(self):
        llamar_manage = Manage()
        llamar_manage.crear_word(self._valor_id)

if __name__ =="__main__":   
    window=ThemedTk(theme="adapta")
    iniciar_sesion=Login(window,"Administrar casos")
    window.mainloop()