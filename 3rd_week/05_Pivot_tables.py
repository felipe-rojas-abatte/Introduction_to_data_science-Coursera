## Pivot table es una forma de resumir los datos para algun proposito que el usuario estime.
## Un pivot table es en si mismo un DataFrame donde las filas representan una variable (la que el usuario estime), las columnas representan otras variable y las celdas algun valor agregado.
## Un pivot table tambien tiende a mostrar valores marginas, que perminte visualizar relaciones entre variable.
## Abramos un nuevo cvs file
import pandas as pd
import numpy as np
df = pd.read_csv('cars.csv') ## Eficiencia de diferentes marcas de autos
print(df.head())
## Digamos que queremos comparar las marcas de autos electricos vs el año y queremos hacer esta comparación en términos de capacidad de batería.
table = df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
print(table)
## Esta tabla nos indica que practicamente todas las marcas no han tenido cambios a los largo de los años en cuanto a capacidad de batería, con excepcion de TESLA, que ha ido aimentando con los años.
## SI queremos agregar 2 valores escribimos values=['col1','col2']

### Pivot table permite realizar varias funciones a la vez creando una tabla con columnas de manera jerarquica como resultado
table2 = df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)
print(table2)
