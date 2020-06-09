## Definimos la funciones sumar 2 numeros
def add_numbers(x,y):
    result = x + y
    return result

print(add_numbers(1,2))

## Definimos la funcion sumar 2 o 3 numeros
def add_numbers(x,y,z=None):
    if(z==None): return x + y
    else: return x + y + z

print(add_numbers(1,2))
print(add_numbers(1,2,3))

## Definimos la función sumar 2 o 3 numeros mas un flag
def add_numbers(x,y,z=None, flag=False):
    if(flag): print('Flag is true!')
    if(z==None): return x + y
    else: return x + y + z
print(add_numbers(1,2,flag=True))

## type retorna que tipo de variable es
print(type('Esto es una cadena'))
print(type(None))
print(type(1.0))
print(type(1))
print(type(add_numbers))


## Existen 3 tipos de colecciones de datos: tuplas, listas y diccionarios
#a) Tuplas: lista de variables que no se pueden modificar. Se crean usando parentesis.
x = (1,'a',2,'b')
print(x, type(x))
#b) Listas: es una lista de variables que se puede modificar. Se crean usando []
x = [1,'a',2,'b']
print(x, type(x))
## Podemos usar la funcion append para incorporar nuevos elementos a la Tuplas
x.append(3.3)
print(x)

## Podemos recorrer cada elemento de la lista con un for.
for i in x:
    print(i)

## Podemos hacer lo mismo usando while
i=0
while(i != len(x)):
    print(x[i])
    i = i+1

## Podemos concatenar 2 listas sumandolas
print([1,2] + [3,4])

## Podemos ver si existe algun elemento dentro de la lista usando in
print(1 in [1,2,3,4])

## Podemos seleccionar caracteres especificos en una lista
x = 'This is a string'
print(x[0]) ## Imprime el 1er caracter
print(x[0:1]) ## Improme todos los caracteres entre 0 y 1
print(x[0:2]) ## Improme todos los caracteres entre 0 y 2
print(x[-1]) ## Improme ultimo caracter
print(x[-4:-2])
print(x[:3]) ## Imprime desde el comienzo hasta el 3er caracter

firstname = 'Christopher'
lastname = 'Brooks'

print(firstname+' '+lastname) ## Imprime nombre mas apellido separado por un espacio
print(firstname*3) ## Imprime 3 veces el nombre
print('Chris' in firstname) ## Imprime True si esa secuencia se encuentra en el nombre

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] ## Separa cada palabra separada por espacio y selecciona el 1er elemento
print(firstname)
firstname = 'Christopher Arthur Hansen Brooks'.split(' ') ## Separa cada palabra separada por espacio y selecciona el 1er elemento
print(firstname)
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] ## Separa cada palabra separada por espacio y selecciona el ultimo elemento
print(lastname)

#c) Diccionarios: Son similares a listas o tuplas pero no tienen un orden. Esto significa que por cada valor tu insertas en el diccionario, debes tambien dar una llave para obtener el valor

##     llave  :  valor
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
print(x['Christopher Brooks'])

##Podemos agragar un nuevo elemento agregando un nuevo indice
x['Kevin Collins-Thompson'] = None

## Puedes recorre todas las llaves en el diccionario x
for name in x:
    print(name, x[name])
## Recorre todos los valores en el diccionario x
for email in x.values():
    print(email)
## Recorre todos las llaves y valores en el diccionario x
for n,e in x.items():
    print(n,e)

## Se puede asignar variables a diferentes elementos del diccionario
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x
print(fname, lname, email)

## Formato para imprimir valores de forma mas optima
sales_record = {'price': 3.24,'num_items': 4,'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))




