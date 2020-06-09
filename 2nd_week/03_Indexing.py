import pandas as pd

## Importamos el archivo census.cvs
df = pd.read_csv('census.csv')
print(df.head(10))

## Este archivo contiene informacion sobre la poblacion a nivel de condado de US. Repartidos en 100 columnas.
## En este data set hay 3 tipos de informacion contenida: Una que contiene informacion a nivel pais o otra que contiene informacion a nivel por cada estado y una ultima que contiene informacion por cada condado
# Podemos ver que en la columna SUMLEV hay solo 2 posibles valores 45 y 50. Esto lo hacemos con la funcion unique()
print(df['SUMLEV'].unique())
#print(df['DIVISION'].unique())
#print(df['STATE'].unique())
#print(df['COUNTY'].unique())
print(df.columns)
## Por ahora solo vamos a trabajar con algunas de las columnas para ir reduciendo el numero de datos.
## Solo vamos a trabajar con las columnas de nombre de estado y ciudad que diga condado (sumlev=50), poblacion total estimada por año y el n° total de nacimientos por año. Para eso quisieramos:
columns_to_keep = ['STNAME','CTYNAME','BIRTHS2010','BIRTHS2011','BIRTHS2012','BIRTHS2013','BIRTHS2014','BIRTHS2015','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
city_name_county = (df['SUMLEV'] == 50)
df = df[columns_to_keep]
df = df[city_name_county]
print(df.head())

##Ahora podemos asociar al index 2 columnas: STNAME y CTYNAME
df = df.set_index(['STNAME','CTYNAME'])
print(df.head(20))

## Ahora que tenemos in index con 2 columnas, si queremos buscar ciertas filas debemos incorporar 2 indices dependiendo de lo que queramos buscar.
## Si queremos saber todas las ciudades dentro de 1 estado (Alabama) usamos 1 indices
print(df.loc['Alabama'])
## Si queremos saber la informacion de un county en particular, debemos ingresar el estado y luego el county
print(df.loc['Alabama','Autauga County'])
## Si queremos comparar 2 condados del mismo estado debemos usar la siguiente notacion
print(df.loc[ [('Michigan','Washtenaw County'),('Michigan','Wayne County')] ])
