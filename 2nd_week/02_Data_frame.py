## Dataframe es basicamente una serie de 2 dimendiones.
## Se puede usar de varias formas:
## a) Puede ser usado como un grupo de series de 1d, donde cada serie representa una fila de tus datos
## b) Puedes usar un grupo de diccionarios, donde cada diccionario representa una fila de tus datos
## Ejemplo:
import pandas as pd

purchase_1 = pd.Series({'Name':'Chris','Item Purchased':'Dog Food', 'Cost':22.50})
purchase_2 = pd.Series({'Name':'Kevin','Item Purchased':'Kitty Litter', 'Cost':2.50})
purchase_3 = pd.Series({'Name':'VInod','Item Purchased':'Beard Seed', 'Cost':5.00})

df = pd.DataFrame([purchase_1,purchase_2,purchase_3], index = ['Store 1','Store 1','Store 2'])
print(df.head())

## Si queremos seleccionar datos de la tabla usamos loc. Esto selecciona toda la file de Store 2
print(df.loc['Store 2'])
## Podemos ver que el nombre de la serie es la indix del df, mientras que las columnas del df pasan a ser el index de la serie.
## Podemos verificar el tipo de output de la serie
print(type(df.loc['Store 2']))

## Si queremos seleccionar una columna entera simplemente hacemos
print(df['Item Purchased'])
## O podemos transponer la matrix cambiando filas por columnas con df.T para luego seleccionad la fila con loc
print(df.T)
print(df.T.loc['Item Purchased'])

## SI queremos acceder a un solo cuadro de la matriz usamos loc incorporando 2 indices
print(df.loc['Store 2','Cost'])
## Con esto tambien podemos hacer slicing. Por ejemplo, si quisieramos seleccionar todas las filas podemos usar una columna para indicar una tajada desde comienzo a fin, y luego agregar una columna como segundo parametro como una string
print(df.loc[:,['Name','Cost']])


## Finalmente podemos juntar operaciones en df. Por ejemplo
print(df.loc['Store 1']['Cost'])
## Hay que tener cuidado al usar eso, ya que aquí lo que hacemos es crear un nuevo df con los datos seleccionados en vez de mirar los datos seleccionados


### Veamos como eliminar data
## Para ello podemos usar la funcion drop que admite 1 parametro
print(df.drop('Store 1')) ## Con esto eliminamos toda la informacion concerniente a Store 1. Pero hace una copia del df original. Si vemos la informacion contenida en df original esta estará intacta

# podemos hacer una copia del df original y usar la funcion drop para que quede guardado el cambio 
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print(copy_df)

## La funcion drop tiene dos opciones:
## a) in place: Si in place = True entonces el df sera actualizado en vez de hacer una copia
## b) axes: si axes = 0 entonces se elimina una fila, si axes = 1 se elimina una columna. POr defecto axes es 0

## Existe una segunda opcion si se quiere eliminar una columna. Esto se hace usando del
del copy_df['Name']
print(copy_df)

## Ademas podemos agragar una nueva columna al df. Por ejemplo si queremos agragar la columna Location, hacemos
df['Location'] = None ## Agrega una nueva columna con valor None
print(df)

print('#############')

## Ejercicio. Como podemos actualizar el df aplicando un descuento de un 20% a todos los valores de cost

print(df)
New_cost_df = df['Cost']*0.8
del df['Cost']
df['Cost'] = New_cost_df
print(df)

## Mas facil
df['Cost'] *= 0.8
print(df)

