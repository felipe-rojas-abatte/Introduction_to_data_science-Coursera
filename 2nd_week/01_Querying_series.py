import pandas as pd
import numpy as np
import timeit
## podemos buscar valores de la lista ya sea por la posicion de intex o por le etiqueta del index
#Series = {index : valor}
#por ejemplo:
sports = {'Archery':'Bhutan','Golf':'Scotland','Sumo':'Japan','Takewondo':'South Korea'}
c = pd.Series(sports)

#si queremos conocer el 4to pais de la serie sports podemos usar el atributo iloc
print(c.iloc[3])
# si queremos saber que pais tiene como deporte nacional el golf, usamos el atributo loc
print(c.loc['Golf'])
## iloc y loc no son metodos, son atributos, entonces debemos usar [] para ejecutarlos

print(c[3], c['Golf'])

# Para realizar operaciones en la lista podríamos iterar sobre todos los valores de la lista por ejemplo usando un for
s = pd.Series([100.00, 120.00, 101.00, 3.00])
total = 0
for item in s:
   total += item
print(total)

## Pandas tiene la capacidad de ejecutar operaciones mathematicas simultaneamente usando el metodo vectorizacion
total = np.sum(s)
print(total)
# Ambas formas realizan la misma funcion, pero la segunda es mucho mas eficiente en cuanto a tiempo
# Para ver que tan rápido es la segunda opcion sobre la primera creemos una lista de 10000 numeros aleatoreos entre 0 y 1000
s = pd.Series(np.random.randint(0,1000,10000))
print(s.head()) ## Metodo head muestra los 5 primeros valores de la lista
print(len(s)) ## muestra el numero de elementos de la lista

## Usaremos la funcion timeit para ver cuanto nos demoramos al ejecutar los 2 metodos. Podemos decirle el numero de loops que nos gustaría correr. Por defecto usa 1000 loops pero ahora usaremos 100. El resultado muestra que el segundo metodo es mucho mas rapido que el primero

## Podemos usar los metodos de pandas para incrementar la velocidad del programa. Por ejemplo podríamos aumentar en 2 cada valor de la serie 
print(s.head(5))
s += 2
print(s.head(5))

## Usando la primera forma tendríamos que hacer un loop sobre todos los valores de la serie e incrementar cada valor en 2

## Al hacer esta operacion no se esta guardando el nuevo valor de value
for value in s:
   value = value + 2
print(s.head(5))

## Para eso tenemos que hacer el loop de la siguiente forma
for label, value in s.iteritems():
#    print(label,value)	
    s.loc[label] = value + 2
print(s.head(5))

for i, value in enumerate(s):
#    print(label,value)	
    s.loc[i] = value + 2
print(s.head(5))


### El atributo loc no solo te permite modificar datos, sino que tambien agregar nuevos datos 
s = pd.Series([1,2,3])
s.loc['Animal'] = 'Bears'
print(s)

## Hasta ahora hemos visto series donde el index es unico, pero podemos ver un ejemplo donde eso no ocurre y el valor de idex es no unico
original_sports = {'Archery':'Bhutan','Golf':'Scotland','Sumo':'Japan','Takewondo':'South Korea'}
original_sports = pd.Series(original_sports)
cricket_loving_countries = pd.Series(['Australia','Barbados','Pakistan','England'], index=['Cricket','Cricket','Cricket','Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
print(all_countries)
print(original_sports) ## La serie original no cambio y sigue manteniendo los mismos datos
