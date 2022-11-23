import os
import shutil
import pandas as pd
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from PIL import Image

def convertir_imagen():
    img = Image.open('imagen.jpg')
    rgb_img = img.convert('RGB')
    rgb_img.save('imagen1.png')

def crear_archivo():
    docx_tpl = DocxTemplate("archivo.docx")
    imagen = "imagen.jpg"
    img = InlineImage(docx_tpl,imagen,height=Mm(120),width=Mm(170))

    contexto = {'id_caso': 'MTC-FT-001',
                'nombre_caso':'Caso 1',
                'descripcion_caso':'Descripcion del caso',
                'pasos':['paso1','paso2','paso3'],
                'resultados':['resultado1','resultado2','resultado3'],
                'imagen':img,
                }

    docx_tpl.render(contexto)
    docx_tpl.save('save.docx')

def ciclo():
    lista_i=[1,2,3,4,5,6]
    lista_a=['a','b','c','d','e','f']
    for i,a in zip(lista_i,lista_a):
        print(i)
        print(a)

#ciclo()

convertir_imagen()

