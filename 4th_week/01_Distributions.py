#Distribution: Un conjunto de todas las posibilidades que una variable aleatoria puede tomar.
#Existen muchas distribuciones como por ejemplo la distribucion binomial. Esta distribucion nos permite por ejemplo
#estudiar la probabilidad de obtener cara o sello cuando lanzamos una moneda.
#Algunos ejemplos donde podemos usar la distribucion binomial son:
#a) Lanzamiento de una moneda. Acá tenemos solo 2 posibilidades: cara o sello. Por lo que cae en la categoría de distribucion discreta, A o B, en vez de numeros reales..
#   Cada posibilidad tiene la misma probabilidad de salir (equiprobable)
#b) Eventos donde aparece un tornado. Acá tambien solo tenemos 1 posibilidades: aparece o no aparece. Sin embargo la probabilidad de que aparezca un tornado es muy baja por lo que la distribucion no es equiprobable.

# numpy tiene en su base de datos distribuciones para poder trabajar  generar eventos aleatorios. Por ejemplo:
import pandas as pd
import numpy as np

#BINOMIAL: dispone de 3 parametros binomial(n,p,size), donde n=numero de intentos, p=probabilidad de exito, size=numero de veces que repetimos el experimento.
# El primer parametro es el numero de veces que queremos correr la funcion y el segundo es la probabilidad de cada evento. En este caso, lo usaremos para representar "cara" en el lanzamiento de una moneda.
# Lo que nos retorna la funcion es 0 o 1
coin1 = np.random.binomial(1, 0.5)
print(coin1)
# Si repetimos este experimento unas 1000 veces obtendremos la suma de todos los casos donde so obtuvo 1. SI ese numero lo dividmos por el total de casos usados, obtendremos la probabilidad de que en un experimento donde se lanzó 1000 veces una moneda obtengamos cara.
coin1k = np.random.binomial(1000, 0.5)
print(coin1k/1000)

#Suppose we want to simulate the probability of flipping a fair coin 20 times, and getting a number greater than or equal to 15. Use np.random.binomial(n, p, size) to do 10000 simulations of flipping a fair coin 20 times, then see what proportion of the simulations are 15 or greater.
# Mi solucion
n_sim = 10000
simulations = np.random.binomial(20, 0.5, n_sim)
cond = 0
for s in simulations:
  if(s>=15): cond += 1
  else: continue
print('proportion = {:.4f}'.format(float(cond)/n_sim))

#coursera solucion
x = np.random.binomial(20, .5, 10000)
print((x>=15).mean())

## Podemos decirle a la distribucion sobre probabilidades no equiprobables usando el ejemplo del tornado.
chance_of_tornado = 0.01/100
x = np.random.binomial(100000, chance_of_tornado)
print(x)

## Tomemos otro ejemplo. Digamos que la posibilidad de que aparezca un tornado es de 1%, en cualquier día del año.
## Cual es la probabilidad de que aparezca un tornado 2 días seguidos?
chance_of_tornado = 0.01
number_of_days = 1000000
tornado_event = np.random.binomial(1, chance_of_tornado, number_of_days)
two_days_in_a_row = 0
for j in range(1,len(tornado_event)):
    if(tornado_event[j] == 1 and tornado_event[j-1] == 1):
        two_days_in_a_row += 1
print('{} tornadoes back to back in {} years'.format(two_days_in_a_row,number_of_days/365))

### Distribucion uniforme:
#Es la distribucion más sencilla de todas. Si graficamos en el eje x el valor observado y en el eje y la probabilidad de observar ese valor, lo que deberíamos obtener es una distribución constante (plana).
# uniform(low,high, size), donde low=valor minimo, high=valor maximo, size=veces que repetimos el experimento.
#Esta distribucion entrega numeros aleatorios entre low y high con igual probabilidad
unif = np.random.uniform(0,10,1)
print('uniforme = ',unif)

### Distribucion normal (gausiana): Distribucion con forma de campana, simetrica en torno al valor central.
#normal(loc,scale,size), donde loc= valor central, scale=desviacion estandard (defaulf = 1.0), size=veces que se repite el experimento
gaus = np.random.normal(0.75)
print('normal = ',gaus)

#Propiedades de las distribuciones
# Valor esperado: representa el valor medio de una distribucion
# Varianza: medida de cuan distribuidos los datos de una muestra estan en torno al valor medio
# Medidas de tendencias centrales: Media, mediana, moda.
# Medidas de variabilidad: deaviacion estandar, rango intercuartil.

#Ejemplo:
distribution = np.random.normal(0.75, 2, size=1000) # generamos un arreglo con 1000 numeros distribuidos de forman normal al rededor del valor 0.75
# Ahora podemos calcular la desviación estandard.
#primero calculamos el valor medio
medio = np.mean(distribution)
sd = np.sqrt(np.sum((medio - distribution)**2)/len(distribution))
sd_py = np.std(distribution) #python tiene una funcion que calcula la desviacion estandar
print('valor medio = {}, desviacion estandar = {}  python std = {}'.format(medio,sd,sd_py))
#Obtenemos valores similares a los incorporados como loc y scale al comienzo

## Indice de curtosis: es una medida que determina el grado de condenración que presentan los valores de una variable alrededor de la zona central de la distribucion.
# un valor negativo indica que la distribución es mas plana que la distribucion normal. POr el contrario un valor positivo indica que la distribucion es mas angosta que la distribucion normal.
 #curtosis k>0 : mas puntiaguda que gausiana
 #         k<0 : mas ancha que gausiana

import scipy.stats as stats
kurt = stats.kurtosis(distribution)
print('curtosis = {} '.format(kurt))

## Indice de asimetria (skew): es una medida que determina que tan asimetrica la distribucion es.
asim = stats.skew(distribution)
print('asimetria = {}'.format(asim)) # podemos ver que este indicador es muy pequeño en la distribucion normal, que es por definicion simetrica.
#Pero veamos cuando nos da este indicador de asimetria en otro tipo de distribucion como Chi⁻2

## Distribucion Chi-2
## Esta distribucion tiene solo 1 parametro llamado grados de libertad.
# Los grados de lobertad estan relacionados con el numero de muestras que tomas de una poblacion normal.
#chisquare(n,size) donde n=numero de grados de libertad, size?veces que repetimos el experimento
chi_squared_df2 = np.random.chisquare(2,size=10000)
asim = stats.skew(chi_squared_df2)
print('asimetria chi2 (2)= {}'.format(asim))

chi_squared_df5 = np.random.chisquare(5,size=10000)
asim = stats.skew(chi_squared_df5)
print('asimetria chi2 (5)= {}'.format(asim))

## Distribuciones bimodales: Tipos de distribuciones que presentan 2 valores centrales y las colas de ellas se traslapan entre si.
