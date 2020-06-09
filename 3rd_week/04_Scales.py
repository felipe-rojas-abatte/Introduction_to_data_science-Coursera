## Tipos de escalas usadas en data science:
#a) Ratio scale: Las unidades estan equidistantes unas de otras y se pueden aplicar operaciones matematicas como +-*/. Ej: peso, altura
#b) Interval scale: LAs unidades estan igualmente estaciadas, pero no hay un cero verdadero. NO se puede * o /. Ej: Temperatura
#c) Ordinary scales: El orden es importante, pero no el espacio entre ellas. Ej: Notas con letras (A+,A,B+,B, etc)
#d) Nominal scale: datos en categorias. No hay orden entre si. Ej: Paises, Equipos deportivos, etc

## Pandas tiene muchas funciones que ayudan a trabajar con estos diferentes tipos de escalas.
##Veamos un ejemplo con notas en escala de letra. Aqui podemos usar la funcion astype para asignar categorías a datos ordinales
import pandas as pd
import numpy as np
##astype
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
print(df)
print()
print(df['Grades'].astype('category').head(11)) # Nos dice que existen 11 categorias para grados. Ahora podemos asignarle prioridad a cada categoría indicando cual es mayor que la otra.

grades = df['Grades'].astype('category',
                             categories = ['D','D+','C-','C','C+','B-','B','B+','A-','A','A+'],
                             ordered = True)
print(grades.head()) #Ahora las categorías tienen una jearquía. POr lo que podemos aplicar operadores como <, >, == .
print(grades > 'C')

##Con tados numericos podemos crear categorías (cangos de datos) con la funcion cut, para reducir la dimensionalidad de los datos.
## cut
df = pd.read_csv('/home/felipe/Dropbox/Python_class/Introductionn_to_data_science-Coursera/2nd_week/census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
## Agrupamos los datos del censo por nombre de estado y calculamos el promedio de poblacion estimada 2010 para cada estado.
## con la funcion cut aplicada a la columna promedio (avg) podemos escoger cuantas categorías crear, o crear n separaciones para ranguear los estados
print(pd.cut(df['avg'],10))
