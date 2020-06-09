## Trabajar con valores que faltan en un data set es importante a la hora de hacer data analisis
## Hasta ahora hemos visto como pandas rellena los espacios vacios usando None y Numpy usa NaN.
## Existen algunas opciones que podemos usar como flags cuando leemos archivos csv en python
## a) na_value: puede indicar otros string como mising values
## b) na_filter: no toma en cuenta espacios vacios de la lista

## Ademas existen otras funciones como:
# a) fillna(): que llena espacios vacios usando un metodo especifico. (‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None})
# Los metodos mas usados son ffill y bfill.
# ffill: es forward filling. Actualiza un espacio vacio con el valor de la fila anterior. Para esto es necesario que los datos esten ordenados.
# Podemos ordenar los datos ya sea por index o por valores. Si definimos alguna columna como index, entonces usando df.sort_index() podemos ordenarla numericamente.
# En caso que en la columna idex aparezcan valores repetidos, podemos indexar una segunda columna para evitar el dobre conteo.
# df = df.set_index(['columna1','columna2'])

## SI queremos reemplazar celdas que tnenen ... por np.nan usamos
#replace('...', np.nan))
