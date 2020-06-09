### Method chaining
import pandas as pd
df = pd.read_csv('/home/felipe/Dropbox/Python_class/Introductionn_to_data_science-Coursera/2nd_week/census.csv')
print(df.head())
# La idea general detras de method chaining es que cada metodo en un objeto devuelve una referencia de ese objeto. Eso significa que podemos condensar muchas operaciones en un DF.
# Por ejemplo, podemos reducir las lineas de codigo de la siguiente forma, haciendo el codigo mas "pandorable"
df = (df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))
# Realizamos varias acciones dentro de la misma linea de codigo
print(df.head())

# Al hacerlo de la forma antigua el codigo no queda tan pandorable
#df = df[df['SUMLEV']==50]
#df.set_index(['STNAME','CTYNAME'], inplace=True)
#df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})

## Otro ejemplo usando el set de datos del censo.
## En el archivo tenemos 5 columnas para poblacion estimada para cada año entre 2010 y 2015. Si quisieramos crear una nueva columna con valores maximos o minimos. Para esto podemos aplicar una funcion que hata este trabajo
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})
## Ahora que tenemos creada la funcion tenemos que aplicarla al DF. Para eso usamos la funcion apply
print(df.apply(min_max, axis=1)) # en este caso el parametro axis se refiere al indice a usar. Para aplicar a todas la filas usamos 1

# Tambien podemos agragar estas columnas al mismo df usando esta funcion
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row

print(df.apply(min_max, axis=1).head())
#print(df.head())

## Una tercera opcion para hacer lo mismo es usanfo las funciones lambdas
rows = [['POPESTIMATE2010',
         'POPESTIMATE2011',
         'POPESTIMATE2012',
         'POPESTIMATE2013',
         'POPESTIMATE2014',
         'POPESTIMATE2015']]
df.apply(lambda x: np.max(x[rows]), axis=1)
