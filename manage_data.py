import json
import pandas as pd
from tkinter import filedialog,messagebox
import openpyxl
from openpyxl.styles import Alignment

class Manage:
	def set_json(self):
		data = list()
		data.append({"id": 1,
		"NOMBRE": "Obtener selloxxo pagando con dinero 'coalición'",
		"DESCRIPCION": "Realizar las compras de productos para obtener selloxxo pagando con dinero 'coalición'",
		"PASOS": ["PASO1.1","PASO1.2","PASO1.3"]}
		)

		data.append({"id": 2,
		"NOMBRE": "Obtener selloxxo pagando con efectivo",
		"DESCRIPCION": "Realizar las compras de productos para obtener selloxxo pagando en efectivo",
		"PASOS": ["PASO2.1","PASO2.2","PASO2.3"]}
		)

		data.append({"id": 3,
		"NOMBRE": "Obtener selloxxo pagando con tarjeta debito",
		"DESCRIPCION": "Realizar las compras de productos para obtener selloxxo pagando con tarjeta de debito",
		"PASOS": ["PASO3.1","PASO3.2","PASO3.3"]}
		)
		
		with open("data.json","w", encoding="UTF-8") as file:
			json.dump(data,file, indent=7)

	def get_info_json(self):
		try:
			with open('data.json','r',encoding="UTF-8") as archivo:
				data = json.load(archivo)
				return data
		except Exception as e:
			print(e)
			return False

	def buscar_dato_json(self,identificador):
		try:
			with open('data.json','r',encoding="UTF-8") as archivo:
				data = json.load(archivo)
			
			for i in data:
				if i['id'] == int(identificador):
					return i
		except Exception as e:
			print(e)
			return False

	def guardar_datos_json(self,diccionario):
		try:
			with open('data.json','r',encoding="UTF-8") as archivo:
				data = json.load(archivo)
			nueva_info = list()
			identificador = 0

			for i in data:
				nueva_info.append(i)
				identificador = i['id']

			descripcion = diccionario['descripcion'].replace('\n','')
			paso = list() ; lista_pasos = list()
			for x in diccionario['pasos']:
				if x == '\n':
					agregar="".join(paso)
					if agregar != "":
						lista_pasos.append(agregar)
					paso.clear()
				else:
					paso.append(x)

			identificador += 1
			nueva_info.append({"id": identificador ,
				"NOMBRE": diccionario['nombre'],
				"DESCRIPCION": descripcion,
				"PASOS": lista_pasos})

			with open("data.json","w", encoding="UTF-8") as file:
				json.dump(nueva_info,file, indent=7)

		except Exception as e:
			print(e)
			return False

	def actualizar_datos_json(self,diccionario):
		try:
			with open('data.json','r',encoding="UTF-8") as archivo:
				data = json.load(archivo)
			nueva_info = list()

			for i in data:
				if i['id'] != int(diccionario['identificador']):
					nueva_info.append(i)
				else:
					descripcion = diccionario['descripcion'].replace('\n','')
					#pasos_unidos = diccionario['pasos'].replace('\n','')
					paso = list() ; lista_pasos = list()
					for x in diccionario['pasos']:
						if x == '\n':
							agregar="".join(paso)
							if agregar != "":
								lista_pasos.append(agregar)
							paso.clear()
						else:
							paso.append(x)

					nueva_info.append({"id": int(diccionario['identificador']),
						"NOMBRE": diccionario['nombre'],
						"DESCRIPCION": descripcion,
						"PASOS": lista_pasos})

			with open("data.json","w", encoding="UTF-8") as file:
				json.dump(nueva_info,file, indent=7)

		except Exception as e:
			print(e)
			return False

	def eliminar_dato(self, identificador):
		try:
			with open('data.json','r',encoding="UTF-8") as archivo:
				data = json.load(archivo)
			nueva_info = list()

			for i in data:
				if i['id'] != identificador:	# Mientras sea diferente al valor buscado o seguira agregando, si es diferente simplemente no lo agregara (eliminacion) 
					nueva_info.append(i)

			with open("data.json","w", encoding="UTF-8") as file:
				json.dump(nueva_info,file, indent=7)

		except Exception as e:
			print(e)
			return False

	def exportar_excel(self):
		data_null={}
		df_null = pd.DataFrame(data_null)
		a = filedialog.asksaveasfilename(title="Abrir", initialdir = "C:/",filetypes = [("Archivo excel","*.xlsx")])

		if a != "":
			df_vacio = pd.DataFrame(columns=["Id caso de prueba","Caso de prueba","Descripción","Pre-requisitos","Datos de prueba","No.paso","Descripción del paso"])
			try:
				with open('data.json','r',encoding="UTF-8") as archivo:
					data = json.load(archivo)
			except Exception as e:
				print(e)
				return False

			for i in data:
				validar_primer_paso = 0
				#FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
				for x in i['PASOS']:
					if validar_primer_paso == 0:
						validar_primer_paso += 1
						#FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.df_vacio = df_vacio.append({"Id caso de prueba": "" ,
						df_vacio = df_vacio.append({"Id caso de prueba": "CP"+ str(i['id']),
										"Caso de prueba":i['NOMBRE'],
										"Descripción": i['DESCRIPCION'],
										"Pre-requisitos": "",
										"Datos de prueba": "",
										"No.paso": validar_primer_paso,
										"Descripción del paso": x,}, ignore_index=True)
					else:
						validar_primer_paso += 1
						df_vacio = df_vacio.append({"Id caso de prueba": "" ,
										"Caso de prueba": "",
										"Descripción": "" ,
										"Pre-requisitos": "" ,
										"Datos de prueba": "" ,
										"No.paso": validar_primer_paso,
										"Descripción del paso": x,}, ignore_index=True)

			df_vacio.to_excel(f"{a}.xlsx",index=False)

			#Darle formato al excel
			wb = openpyxl.load_workbook(f"{a}.xlsx") 
			sheet = wb.active 
			#Tamaño a las columnas
			sheet.column_dimensions['A'].width = 20
			sheet.column_dimensions['B'].width = 50
			sheet.column_dimensions['C'].width = 50
			sheet.column_dimensions['D'].width = 20
			sheet.column_dimensions['G'].width = 50
			for row in sheet:
			  for cell in row:
			    cell.alignment = Alignment(wrapText=True,horizontal='center')	#Ajusta el texto y lo centra
			wb.save(f"{a}.xlsx") 
			messagebox.showinfo("Completado","Excel creado.")

	def guardar_reacomodo(self,datos):
		with open("data.json","w", encoding="UTF-8") as file:
			json.dump(datos,file, indent=7)

	def buscar(self, valor_busqueda):
		try:
			with open('data.json','r',encoding="UTF-8") as archivo:
				info = json.load(archivo)

			info1=[]
			valor_busqueda1=valor_busqueda.lower()

			if valor_busqueda =="":
				return info

			for i in info:
				cadena_nombre = i["NOMBRE"].split(" ")
				cadena_descripcion = i["DESCRIPCION"].split(" ")

				string_cadena_nombre = " ".join(cadena_nombre)	#Convertir la lista de palabras en una sola cadena
				string_cadena_descripcion = " ".join(cadena_descripcion)
				lista = [string_cadena_nombre,string_cadena_descripcion] #Colocarlos en una lista para recorrer
				for a1 in lista:					
					b1=str(a1) ; c1=b1.lower()		#Transforma en texto y minusculas
					objeto1=c1.find(valor_busqueda1) 	#Checar si la palabra de busqueda esta
					if objeto1 != -1 and i not in info1:						#Si es diferente de False y no esta en la lista
						info1.append(i)
				"""		
				for leer_cadena in lista:
					for a1 in leer_cadena:
						b1=str(a1) ; c1=a1.lower()		#Transforma en texto y minusculas
						print(c1[:len(valor_busqueda1)],valor_busqueda1)
						objeto1=c1[:len(valor_busqueda1)].find(valor_busqueda1) 	#Checar si la palabra de busqueda esta
						if objeto1 != -1 and i not in info1:						#Si es diferente de False y no esta en la lista
							#print("Agregar con metodo 2",i["id"])
							info1.append(i)
							break"""			
			return info1
		except Exception as e:
			print(e)
			return False

if __name__ == '__main__':
	llamar_manage = Manage()
	#x=llamar_manage.set_json()
	#e=llamar_manage.buscar_dato_json(1)
	#print(e)
	#y=llamar_manage.get_info_json()
	#print(y)
	#llamar_manage.eliminar_dato(3)
