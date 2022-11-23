import numpy as np

matriz_cero = np.array(42)
matriz_unidimensional = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
matriz_bidimensional = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
matriz_tridimensional = np.array([ 
								[[1,2,3],[4,5,6]], 
								[[7,8,9],[10,11,12]] 
								])

def ciclo(lista,conteo):
	if conteo != len(lista):
		print(lista[conteo])
		conteo += 1
		ciclo(lista,conteo)

def ciclo2(lista):
	for i in lista:
		print(i)

ciclo(matriz_unidimensional,0)
ciclo2(matriz_unidimensional)