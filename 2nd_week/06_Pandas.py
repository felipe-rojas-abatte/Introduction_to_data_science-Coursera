## Trabajan con Series. Una serie es una mezcla entre una lista y un diccionario.
import pandas as pd
import numpy as np

#Creamos una lista con animales
animals = ['Tiger', 'Bear', 'Moose']
print(pd.Series(animals)) # Al usar Series con strings este devuelve que son objetos

numbers = [1,2,3]
print(pd.Series(numbers)) # Al usar Series con numeros este devuelve que son int64

animals = ['Tiger', 'Bear', None] # Al usar None dentro de la serie, pandas lo incorpora dentro de los valores de la lista como un objeto
print(pd.Series(animals))

numbers = [1, 2, None] # Al usar None junto con numeros, pandas convierte el valor None en un float designandoilo como NaN (Not a number)
print(pd.Series(numbers))

# Usando numpy, np.nan es similar a None pero entrega un valor numerico, y es tratado de manera diferente por razones de eficiencia. Si hacemos el test de igualdad:
print(np.nan == None) # esto da Falso
# Para hacer el testeo de forma correcta debemos usar funciones especiales
print(np.isnan(np.nan))

# Una serie puede ser creada a partir de un diccionario. Al hacer esto el indice es automaticamente asignado a la llave del diccionario
# diccionario = {llave : valor} ->  Series = {index : valor}
sports = {'Archery':'Bhutan','Golf':'Scotland','Sumo':'Japan','Takewondo':'South Korea'}
a = pd.Series(sports)
print(a)
print(a.index) ## Se puede acceder al index de la Serie

## Tambien se puede asignar de forma separada el indice escribiendolo explicitamente en la Serie
b = pd.Series(['Tiger','Bear','Moose'],index=['India','America','Canada'])
print(b)
print(b.index)

# ¿Que pasa cuando la lista de valores en el index no está alineada con la llave del diccionario?
# pandas solo deja pasar los velores de index que tu proporcionas, ignorando los que no estan en la lista de index pero si aparecen en el diccionario
# Los valores de index que no estan en el diccionario seran rellenados con NaN
sports = {'Archery':'Bhutan','Golf':'Scotland','Sumo':'Japan','Takewondo':'South Korea'}
c = pd.Series(sports, index = ['Golf','Sumo','Hockey'])
print(c)
