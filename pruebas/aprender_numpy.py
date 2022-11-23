import numpy as np

matriz_cero = np.array(42)
matriz_unidimensional = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
matriz_bidimensional = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
matriz_tridimensional = np.array([ 
								[[1,2,3],[4,5,6]], 
								[[7,8,9],[10,11,12]] 
								])

#Preguntar la dimension de la matriz
'''
print(matriz_cero.ndim)
print(matriz_unidimensional.ndim)
print(matriz_bidimensional.ndim)
print(matriz_tridimensional.ndim)
'''

#Acceder a datos dentro de matriz
'''
print(matriz_unidimensional[0])
print(matriz_bidimensional[3,0])
print(matriz_tridimensional[1,0,0])
print(matriz_tridimensional[1,0,-1])	#Uso de numeros negativos para leer en reversa
'''
#Acceder
#print(matriz_unidimensional[1:4])
#print(matriz_unidimensional[:])
#print(matriz_bidimensional[1,0:2])
#print(matriz_bidimensional[0:5, 0:4]) #Primer parte es la 'lista general', la segunda parte aplica a todos de la primera parte
#----------------------------------------------
# COPIAR MATRIZ #
matriz_flotante = np.array([1.2,2.1,3.3])
nueva_matriz = matriz_flotante.astype(int) # COPIAR MATRIZ CAMBIANDO FORMATO DE VARIABLE #
#print(nueva_matriz)

matriz_copy = matriz_flotante.copy()	#Copiar la matriz
matriz_flotante[0] = 11.11

print(matriz_flotante)
print(matriz_copy)
#------------------------------------------------------------------------
arr = np.array([1, 2, 3, 4], ndmin=5)	#Con ndim podemos asignar una cantidad de dimensiones

print(arr)
print('shape of array :', arr.shape)	#Con shape podemos preguntar la cantidad de dimensiones


