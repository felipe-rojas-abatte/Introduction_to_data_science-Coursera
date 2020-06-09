import pandas as pd

purchase_1 = pd.Series({'Name':'Chris','Item Purchased':'Dog Food', 'Cost':22.50})
purchase_2 = pd.Series({'Name':'Kevin','Item Purchased':'Kitty Litter', 'Cost':2.50})
purchase_3 = pd.Series({'Name':'VInod','Item Purchased':'Beard Seed', 'Cost':5.00})

df = pd.DataFrame([purchase_1,purchase_2,purchase_3], index = ['Store 1','Store 1','Store 2'])

## Hay que tener cuidado al manipular datos en pandas ya que cualquier maniplacion podría tener un impacto en los datos originales.
#Por ejemplo

costs = df['Cost']
print(costs)
costs += 2 ## Al realizar esta operacion estamos cambiando el valor original de la columna costs
print(costs)
print(df) ## Esto se ve reflejado en el df original. Por lo que es mejor llamar el metodo copy para asegurarnos de no modificar los datos originales

print('\n ############################### \n')
## La idea de usar pandas es tomar datos externos almacenados en archivos que podemos importar usando python para luego crear un dataframe con esos datos y trabajar sobre el df

## Importamos el archivo olympic.cvs
df = pd.read_csv('olympics.csv')
print(df.head())
## Al ver lo que contiene el archivo podemos darnos cuenta de que la primera columna de datos contiene nombres de paises y la primera fila de datos contiene el nombre de cada columna. La casilla 0,0 contiene el valor NaN= Not a Number. Podemos indicarle a pandas que columna debe ser asignada como index y que fila debe ser asignada como nombres de columnas.
# Para eso importamos nuevamente el archivo agragando lo siguiente
df = pd.read_csv('olympics.csv', index_col=0, skiprows = 1) # Con este le decimos a pandas que la columna de paises sea ahora el index y que no tome en cuenta la primera fila
print(df.head())
## Ahora que hemos arreglado el index podemos darnos cuenta que los nombres de las columnas no son del todo claras. El df original usa los nombres 01! 02! y 03! en vez de usar oro, plata, cobre para los ganadores de medallas. Podemos modificar los nombres para que quede mas claro a que se refieren
print(df.columns) #Muestra el nombre origila de cada columna

# Iteramos sobre cada columna
for col in df.columns:
	#print(col)
	#print(col[:2]) ## Escojo los 2 primeros caracteres del nombre de cada columna
	#print()
	if(col[:2] == '01'): df.rename(columns={col:'Gold'+col[4:]}, inplace=True) #si se cumple if, entonces reemplazamos el nombre por 'gold'+todo desde el caracter 4 hacia adelante. inplace hace que pandas remplace los cambios directamente en df
	if(col[:2] == '02'): df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
	if(col[:2] == '03'): df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
	if(col[:2] == '#'): df.rename(columns={col:'#'+col[4:]}, inplace=True)

print(df.head())

## Boolean masking: corazon del proceso de busqueda en numpy.
## Es un arreglo que puede ser 1d (serie) o 2d (data frame) dode cada valor de la matriz puede ser verdadero o falso. Este arreglo está incrustado por sobre los datos. Cada celda alineada con el valor True será admitida en el rasultado final y cada celda con el valor False no será admitida.
## Por ejemplo: Usando la informacion de los juegos olimpicos podríamos estar interesados solo en los paises que han ganado medallas de oro en los juegos de verano. Para construir un boolean mask hacemos lo siguiente
print(df['Gold']>0) ## Esto entregara una lista de verdaderos y falsos que cumplan con la condicion
# Para aplicar esta condicion el el df original y así construir un nuevo df con los datos que queremos seleccionar usamos la funcion where
only_gold = df.where(df['Gold']>0)
print(only_gold.head(3))
# Al hacer eso, todos los paises que cumplen la condicion son mostrados, y aquellos que no la cumplen pararecen como NaN
#Si quisieramos saber cuantos paises han cumplido esta condicion hacemos
print(only_gold['Gold'].count()) ## solo 100 paises han cumplido esta condicion
print(df['Gold'].count()) ## Si hacemos lo mismo en el df original veremos que son 147 los paises en totalself.

## Si queremos ahora eliminar los datos que no cumplen con la condicion usamos la funcion dropna
only_gold = only_gold.dropna()
print(only_gold.head())

##Otra opcion, sin usar la opcion dropna:
gold_cut = (df['Gold']>0)
only_gold2 = df[gold_cut]
print(only_gold2.head())
print(only_gold2['Gold'].count())

## El resultado final de 2 boolean masks siendo comparada con operadores logicos es otro boolean mask. Podemos realizar operaciones logicas (and, or, etc) con diferentes cortes en el data DataFrame
# por ejemplo:
## Creemos una mascara con todos los paises que recibieron una medalla de oro en los juegos de verano "o" crear una mascara con todos los paises que recibieron una medalla de oro en los juegos de invierno
only_gold_summer = (df['Gold']>0)
only_gold_winter = (df['Gold.1']>0)
print(len(df[only_gold_summer | only_gold_winter]))
print('\n ############################### \n')
##¿Cuantos paises han ganado una medalla de oro en los juegos de invierno y nunca en los juegos de verano?
only_gold_winter = (df['Gold.1']>0)
never_gold_summer = (df['Gold']==0)
print(df[never_gold_summer & only_gold_winter])

print('\n ############################### \n')
### Que pasa si queremos indexar nuestro df no por la lista de paises sino que por el numero de medallas que fueron ganadas en los juegos de verano
#a) Primero debemos conservar la informacion de los paises en una nueva columna
df['country'] = df.index
#b) Luego usando la funcion set_index le decimos que columna queremos usar como index
df = df.set_index('Gold')
print(df.head())
## Ahora la columna gold paso a ser index y una nueva columna apareción con la informacion de los paises
## Sin embargo, el nombre de la columna quedó en la posicion 0 del index.
## Tambien podemos resetear el index con la funcion reset_index() para crear una nueva columna con numeros desde eo 0 hasta N como index
df = df.reset_index()
print(df.head())


### Ejercicio:
#Reindex the purchase records DataFrame to be indexed hierarchically, first by store, then by person. Name these indexes 'Location' and 'Name'. Then add a new entry to it with the value of:
#Name: 'Kevyn', Item Purchased: 'Kitty Food', Cost: 3.00 Location: 'Store 2'.

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

##### Mi solucion
# 1st: we store the information of the index in a new column
df['Location'] = df.index
# 2nd: we set the new index using 2 columns
df = df.set_index(['Location','Name'])
print(df)
# 3rd: create the new entry
purchase_4 = pd.Series({'Name':'Kevyn','Item Purchased': 'Kitty Food','Cost': 3.00})
# 4th: do the same with new entry
df2 = pd.DataFrame([purchase_4], index=['Store 2'])
df2['Location'] = df2.index
df2 = df2.set_index(['Location','Name'])
# 5th: Append the new entry to the existing df
df=df.append(df2)
print(df)


### Solucion del curso
df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
print(df)
