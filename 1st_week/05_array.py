import numpy as np
## creamos una lista y lo convertimos en arreglo
mylist = [1, 2, 3]
x = np.array(mylist)
print(x)

m = np.array([[7, 8, 9], [10, 11, 12]])
print(m)

# la funcion shape muestra la dimension del arreglo
print(m.shape)

# crea un arreglo de numeros entre 0 y 30 de 2 en 2
n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
# reordena el areglo con una nueva forma
n = n.reshape(3, 5) # reshape array to be 3x5
# crea un arreglo de 9 numeros entre 0 y 4
o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
# retorna un arreglo lleno de 1 con las dimensiones mensionadas
np.ones((3, 2))
# retorna un arreglo lleno de ceros con las dimensiones mensionadas
np.zeros((2, 3))
# retorna una matriz unidad de dimension mensionada
y = np.eye(3)
# extrae la diagonal de una matriz o crea una matriz diagonal
print(np.diag(y))
# crea un arreglo usando la misma fila 3 veces creando una fila mas larga
print(np.array([1, 2, 3] * 3))
# crea un arreglo usando la misma fila repetidas veces
print(np.repeat([1, 2, 3], 3))
#
p = np.ones([2, 3], int)
print(p)
print(np.vstack([p, 2*p]))

##### Operaciones
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y) # suma elemento por elemento
print(x-y) # resta elemento por elemento
print(x*y) # multiplica elemento por elemento
print(x/y) # divide elemento por elemento
print(x**2) # cuadrado de cada elemento
print(x.dot(y)) # producto punto
z = np.array([x, y])
print(z)
print(len(z)) # numero de filas en la matriz
print(z.T) #Transpuesta de una matriz
print(z.dtype) # Tipo de datos del arreglo

###### Funciones matematicas
a = np.array([-4, -2, 1, 3, 5])
print(a.sum()) # suma todos los elementos
print(a.max()) # encuentra el valor maximo
print(a.min()) # encuentra el valor minimo
print(a.mean()) # encuentra el promedio
print(a.std()) # encuentra la desviacion estandar
print(a.argmax()) # devuelve el lugar del valor maximo
print(a.argmin()) # devuelve el lugar del valor minimo
print(a[0])

r = np.arange(36) ## crea un arreglo desde 0 a 36 con saltos de 1
r1 = r.reshape(6,6) ## # reordena el areglo con una nueva forma
print(r1)
print(r1[2,2]) # imprime valor de (fila, columna)
print(r1[3,3:6]) # irmprime file 3 entre columnas 3 y 6
print(r1[r1>30]) # imprime valores mayores a 30
r1[r1>30]=30 #asigna el valor 30 a todos los elementos mayores de 30
print(r1)

r2 = r1[:3,:3] # selecciona las primeras 3 filas y primeras 3 columnas
print(r2)

r_copy = r1.copy() # copiamos el arreglo r1 sin afectar el arreglo r1 en caso de modificar r
print(r_copy)
r_copy[:] = 10
print(r_copy, '\n')
print(r1)
