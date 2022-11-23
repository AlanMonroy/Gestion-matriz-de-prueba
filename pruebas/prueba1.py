import tkinter as tk
import random

#Creador: Roberto Alan Rodriguez Monroy
from tkinter import *
from tkinter import ttk,filedialog,messagebox
from tkinter.ttk import Combobox
from ttkthemes import ThemedTk
import json
from operator import itemgetter

class Aplicacion:
    def __init__(self,window,nombre):
        self.fondo = 'black'; self.letra = 'white' ; self.color_check = 'black'      
        self.window = window
        #self.window.title(title)
        self.window.resizable(False,False)
        #self.window.geometry("916x300")
        self.window.configure(background = self.fondo)
        #self.window.state("zoomed")
        self.window.wm_attributes("-transparentcolor","#60b26c")#60b26c
        self.window.wm_attributes("-alpha",.85)

        #self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.window, width=900, height=500, background="black")
        self.canvas1.grid(column=0, row=0)

        for x in range(101):
            x1=random.randint(1,900)
            y1=random.randint(1,500)
            self.cuadrado=self.canvas1.create_rectangle(x1, y1, x1+20, y1+20, fill="red", outline="red", tags="movil")
        
        ñself.canvas1.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
        self.canvas1.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.carta_seleccionada = None
        #self.ventana1.mainloop()

    def presion_boton(self, evento):
        carta = self.canvas1.find_withtag(tk.CURRENT)
        self.carta_seleccionada = (carta, evento.x, evento.y)

    def mover(self, evento):
        x, y = evento.x, evento.y
        carta, x1, y1 = self.carta_seleccionada
        self.canvas1.move(carta, x - x1, y - y1)
        self.carta_seleccionada = (carta, x, y)    

#aplicacion1=Aplicacion()

if __name__ =="__main__":   
    window=ThemedTk(theme="adapta")
    iniciar_sesion=Aplicacion(window,"Administrar casos")
    window.mainloop()