import pandas as pd
import numpy as np

## Pandas tiene 4 formas de mostrar tiempo.
##1) Timestamp (marca de tiempo): representa un solo punto de tiempo. Es intercambiable con fecha usadas en python
print(pd.Timestamp('9/1/2016 10:05AM'))
print()
##2) Period: (lapso de tiempo)
print(pd.Period('1/2016')) ## Me dice que esto representa mes 'M'
print(pd.Period('3/5/2016')) ## Me dice que esto representa dias 'D'
print()
##3) Datetimeindex: Es el indice de un timestamp. En esta serie el timestamp se vuelve el index de la lista
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
print(t1)
print(type(t1.index))
print()
##4) Periodindex: EN esta serie el period se vuelve index
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
print(t2)

### Converting to datetime
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16'] # diferentes tipos de fechas en la lista
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab')) ## creamos un df con valores aleatorios entre 10 y 100 que ocupen una tabla de 4x2 donde las fechas sean el index y tenga 2 columnas llamadas "a" y "b"
print(ts3)
#Las fechas estan en distintos formatos, pero usando to_datetime, pandas convierte la lista a un solo formato
ts3.index = pd.to_datetime(ts3.index)
print(ts3)

## Timedeltas: son diferencias en tiempo
delta = pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')
print(delta) # obtenemos una diferencia de tiempo de 2 días
delta2 = pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H') # podemos saber cuando será si sumamos 2 fechas
print(delta2) # será 2016-09-14 11:10:00
print()

## Working with Dates in a Dataframe
#Supongamos que tener 9 mediciones cada 2 semanas tomadas cada domingo partiendo de octubre 2016. Usando date_range podemos hacer eso
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
print(dates)
## Ahora creemos un DF usando estos datos y llenemos 2 columnas con numeros aleatorios para ver que podemos hacer con ellos
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5,10,9).cumsum(), 'Count 2':120 + np.random.randint(-5,10,9)}, index=dates)
print(df)
# Podemos checkear en que día de la semana ocurrio cada dato
#print(df.index.weekday_name)
# Podemos encontrar el conteo promedio por cada mes en el DP
print(df.resample('M').mean())
# Podemos usar parte del index para buscar valores de un año en particular, o de un mes especifico
print(df['2017'])
print(df['2016-12'])
#Tambien podemos seleccionar fechas a partir de una en particulas hacia adelante
print(df['2016-12':])

## Otra funcion es cambiar la frecuencia de nuestros datos con asfreq. POr ejemplo si queremos cambiar la frecuencia de bi-semanal a semanal.
## Pare ellos usamos el metodo de forward fill para rellenar los espacios vacios que apareceran
print(df.asfreq('W', method='ffill'))

## Plots: podemos visualizar los datos usando lo siguiente
import matplotlib.pyplot as plt
%matplotlib inline

df.plot()
