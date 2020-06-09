#### Resumen de lo que hemos visto:
# Hay 2 tipos de estructuras de datos que son muy similares:
# a) Series: objetos de 1d
# b) Data Frames: objetos de 2d
# Para realizar busquedas en estas bases de datos podemos usar los atributos iloc y loc si queremos buscar por fila, o usar los parentesis [] para buscar por columna.
# Tambien vimos que los DF y S pueden ser reducidos a traves de un boolean masking.

import pandas as pd
purchase_1 = pd.Series({'Name':'Chris','Item Purchased':'Dog Food', 'Cost':22.50})
purchase_2 = pd.Series({'Name':'Kevin','Item Purchased':'Kitty Litter', 'Cost':2.50})
purchase_3 = pd.Series({'Name':'VInod','Item Purchased':'Beard Seed', 'Cost':5.00})
df = pd.DataFrame([purchase_1,purchase_2,purchase_3], index = ['Store 1','Store 1','Store 2'])
#print(df.head())

### Algunas cosas útiles
# Si queremos agregar una nueva columna con informacion, por ejemplo la fecha de la compra, solo escribimos
df['Date'] = ['Dicember 1','January 1','mid-May']
#print(df)
# Si queremos agregar una columna con informacion de si se realizó la entrega, podemos escribir
df['Delivery'] = True
#print(df)
# ¿Que ocurre si tenemos que agregar solo algunos datos en una columna, Por ejemplo feedback, en donde solo tenemos la informacion de 2 filas. Por lo que tenemos que llenar con None en los lugares que no tenemos la información.
# Esto es un problema si estamos trabajando con una lista larga de datos.
df['Feedback'] = ['Positive', None, 'Negative']
print(df)
# Si cada fila tuvo un indice unico, entonces podríamos simplemente asignar este identificardor a la serie para llenar los espacios con informacion. Por ejemplo, si reseteamos el index en este ejemplo tendremos un nuevo index que va desde 0 a 2. Así podemos asignarle a la columna que queramos el valor correspondiente.
# Con este método podemos ignorar las celdas que no conocemos la informacion
adf = df.reset_index()
adf['Date'] = pd.Series({0: 'Dicember 1', 2: 'mid-May'})
print(adf)

### Como fusionar DFs
# Primero debemos tomar en cuenta algunas cosas antes de fusionar DF. Pensemos que tenemos 2 conjuntos de datos:
# a) El conjunto A son solo estudiantes de una universidad
# b) El conjunto B son solo staff de la universidad.
# Si queremos fusionar estos dos conjuntos de datos tenemos que tomar en cuenta elementos de la teoría de conjuntos.
# Por ejemplo si queremos visualizar un df con toda la gente ligada a la universidad sin importar que funcion desempeñan, esto es lo mismo que considerar la union (Full outer join) de los conjuntos. Por otro lado tambien podríamso considerar los casos donde tomaramos encuenta solo a las personas que son alumnos y funcionarios a la vez. Esto es lo mismo que la interseccion (Inner join).
# ejemplo
# Creamos 2 DF, staff y estudiantes
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())
# En este ejemplo tenemos 2 estudiantes que estan en ambos df (Sally y James)
# Si quisieramos la union de estos 2 df usamos la funcion merge
# los flags: how:(outer=union)) left_index and right_index: queremos usar las columnas de la iz y der para fusionarlos
print('##### Union #####')
union = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
print(union)
print('##### Interseccion #####')
interseccion = pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
print(interseccion)
## Set addition
# Si ahora quisieramos listar a todos staff sin importar si son estudantes o no, pero si lo fueran nos gustaría tener tambien esa informacion.
print('##### Set addition 1 #####')
set_addition1 = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
print(set_addition1)
# Si ahora quisieramos listar a todos estudiantes sin importar si son staff o no, pero si lo fueran nos gustaría tener tambien esa informacion.
print('##### Set addition 2 #####')
set_addition2 = pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
print(set_addition2)

### Otras opciones. No es necesario usar index para fisionar los DFs, tambien puedes usar columnas.
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
option1 = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
print(option1)

## Que ocurre cuando tenemos conflictos en el df.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
option2 = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
## En este caso, tenemos que la dirección de un estudiantes es su casa, pero la dirección de la misma persona como staff es la universidad. Pandas conserva esta informacion, pero agrega un sub indice al nombre de la columna
## en este caso el subindice _x siempre hace referencia al df izquierdo, y el subindice _y hace referencia al df derecho
print(option2)

## Multi-indexing and multiple columns.
# Es posible que el primer nombre de un estudiante se traslape con el de un staff, pero el apellido sea diferente en ambos casos. Por ejemplo
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
print(staff_df)
print(student_df)
## Para evitar eso, podemos usar en la opcion left_on 2 columnas al igual que en la opcion right_on
interseccion = pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])
print(interseccion)
# En este caso, solo la persona kelly aparecía igual en ambas listas, por lo tanto es la unica que caen el pa interseccion
