import pandas as pd
import numpy as np

df = pd.read_csv('/home/felipe/Dropbox/Python_class/Introductionn_to_data_science-Coursera/2nd_week/census.csv')
df = df[df['SUMLEV'] == 50]
print(df.head())

## Si quisieramos hacer un loop que iterara sobre todos los estados y genere una lista del promedio de poblacion, tenemos 2 formas para hacerlo:
# a) Hacemos un loop sobre los estados los cuales fueron seleccionados con la opcion unique
# b) Usamos la funcion gruop_by: Esta funcion toma una columna y las separa en pedazos basados en los nombres de las columnas, devolviendo un df agrupado por grupos.

# opcion a:
states = df['STNAME'].unique()
for state in states:
    ave = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    print('Counties in state '+ state + ' have an average population of '+ str(ave))

# mi opcion:
for state in states:
    cut = (df['STNAME'] == state)
    ave = np.average(df[cut]['CENSUS2010POP'])
    print('Counties in state '+ state + ' have an average population of '+ str(ave))

# opcion b: (mucho mas rapida)
for group, frame in df.groupby('STNAME'):
    ave = np.average(frame['CENSUS2010POP'])
    print('Counties in state '+ group + ' have an average population of '+ str(ave))

## La mayor parte del tiempo usaremos group_by en 1 o varias columnas para dividir el df, pero tambien podemos proporcionar una funcion para agrupar y segmentar los datos.
# Para usar este metodo debemos transformar en index la columna que queremos separar.
## por ejemplo:
df = df.set_index('STNAME')
def fun(item):
    if item[0] < 'M': #BOOLEAN
        return 0
    if item[0] < 'Q': #BOOLEAN
        return 1
    else:
        return 2

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group '+ str(group) +' for processing.')

## Un uso comun de la funcion group_by es que tu separas tus datos, aplicas alguna funcion y luego combinas el resultado. Esto se llama split apply combine pattern.
# esto se puede hacer a traves de la funcion agg de aggregate
df = pd.read_csv('/home/felipe/Dropbox/Python_class/Introductionn_to_data_science-Coursera/2nd_week/census.csv')
df = df[df['SUMLEV'] == 50]
print(df.groupby('STNAME').agg({'CENSUS2010POP': np.average}))

## Existe un pequeño detalle al usar la funcion agg. Por ejemplo
print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'])) #DF object
print(type(df.groupby(level=0)['POPESTIMATE2010'])) #Series object

#Estos 2 objetos se comportan de manera diferente al usar agg
#Por ejemplo: Tomemos el df census y creemos uns serie donde los estados sean el index y la unica columna sea el cencus2010pop. Luego usemos la funcion agg para calcular
# el promedio y la suma sobre los condados. Esto genera un output donde aparecen los estados junto a su respectiva suma y promedio
print(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum}))

## Si hacemos lo mismo pero ahora lo aplicamos a un df en vez de a una serie, donde el df tendrá como index los estados pero ahora tenemos 2 columnas (popestimate2010 y popestimate2011). Esto genera un df con los promedios y la suma de cada columna.
#df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'avg': np.average, 'sum': np.sum})

## EL problema aparece cuando queremos aplicar la cuncion a columnas diferentes del df. las funciones son aplicadas a cada columna, pero el output no muestra que funcion se aplico.
#print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))
