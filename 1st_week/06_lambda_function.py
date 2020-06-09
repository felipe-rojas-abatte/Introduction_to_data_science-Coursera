## funcion lambda: estas son formas que tiene python para crear cunciones anonimas. Son lo mismo que una funcion, pero no tienen nombre.

#esta funcion toma 3 valores numericos y suma los 2 primeros
my_function = lambda a, b, c : a + b
print(my_function(1, 2, 3))

## funcion que itera desde 0 a 999 y devuelve los numeros pares
my_list = []
for n in range(0,10,1):
    if(n % 2 == 0): my_list.append(n)
    else: continue

print(my_list)

#usando lambda function

num_pares = [n for n in range(0,10,1) if n % 2==0]
print(num_pares)


## ejemplo de list comprehension
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

print(times_tables())

print(times_tables() == [i*j for i in range(0,10,1) for j in range(0,10,1)])


## escribir todas las posibles combinaciones usando la notacion 'aa43' 

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [l1+l2+n1+n2 for l1 in lowercase for l2 in lowercase for n1 in digits for n2 in digits]


