def pedir_datos():
	try:
		x = float(input("Dame un valor: "))
		y = float(input("Dame un valor: "))
		z = float(input("Dame un valor: "))

		mayor = max(x,y,z)
		print("El número mayor es: ",mayor)
	except Exception as e:
		print("Datos equivocados, se volveran a solicitar")
		pedir_datos()

pedir_datos()