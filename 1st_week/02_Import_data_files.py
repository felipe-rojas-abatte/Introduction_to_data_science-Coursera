
##Importamos archivos cvs para ser leidos
import csv
with open('COVID19_open_line_list.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))  ## DictReader lee cada fila como un diccionario.

print(mpg[:1]) # Imprime las primeras  linas de la lista
print(len(mpg)) ## Imprime el numero de elementos de la lista

print(mpg[0].keys()) ## Muestra el nombre de las columnas de nuestro cvs

#sum(float(d['cty']) for d in mpg) / len(mpg) ## Sacamos promedio de cty
#cylinders = set(d['cyl'] for d in mpg)  ## La funcion set devuelve el univo valor cuando hay valores repetidos en la lista

## Pequreño codigo para agrupar autos por numero de cilindros y encontrar el promesio de cty para cada grupo

CtyMpgByCyl = [] # Creamos arreglo para almacenar datos
cylinders = set(d['cyl'] for d in mpg) ## encuentra todos los valores para los cilindros
for c in cylinders: # itera sobre todos los posibles valores de cilindros
    summpg = 0 ## contador para sumar cty
    cyltypecount = 0 ## contador
    for d in mpg: # itera sobre todos el diccionario
        if d['cyl'] == c: # selecciona la fila si cyl es = al numero de cilindros
            summpg += float(d['cty']) # suma el cty en cada file seleccionada
            cyltypecount += 1 # contador para este numero de cilindro
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0]) ## sort: ordena el arreglo en orden ascendente
CtyMpgByCyl
