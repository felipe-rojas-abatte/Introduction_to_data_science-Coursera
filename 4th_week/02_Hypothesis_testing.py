# Test de Hipotesis: (A/B testing)
#Hipotesis: es una declaracion que podemos poner a prueba.
#Por ejemplo: Digamos que lanzamos un curso online, y queremos verificar so los estudiantes que se inscriben inmediatamente al curso se desempeñaran de mejor manera sobre aquellos estudiantes que se inscribieron mas tarde en el curso.
# En ete ejemplo tenemos 2 grupos diferentes que queremos comparar, los primeros en inscribirse y los que se inscriben mas tarde.
# Bajo este concepo generamos una hipotesis: Existe una diferencia entre los grupos de estuiantes.
# Pero ademas creamos uns segunda hipotesis llamada hipotesis nula: Ques la opcion contraria a la hipotesis inicial, es decir, no hay diferencia entre grupos.
# Si al final de testear el experimento nos damos cuenta que existe una diferencia entre los grupos, entonces estamos capacitados para decir que encontramos evidencia en contra de la hipotesis nula, por lo que estamos mas confiados con nuestra hipotesis inicial.
import pandas as pd

df = pd.read_csv('grades.csv')
print(df.head())
#En el archivo de datos tenemos estudiantes con su respectivo id, notas finales de cursos y cuando se inscribieron a esos cursos.
print(len(df))
#Separemos estos estudiantes en 2 grupos. Aquellos que se inscribieron antes del 31-dic-2015 y los que se inscribieron luego de eso.
condition_early = (df['assignment1_submission'] <= '2015-12-31')
condition_late = (df['assignment1_submission'] > '2015-12-31')
early = df[condition_early]
late = df[condition_late]
## Si miramos los valores promedios de las notas veremos que existen pequeñas diferencias, menores al 2% entre los grupos. SI quisieramos tomar una decision sobre que hipotesis nomar, debemos tener un criterio de selección.
print(early.mean())
print(late.mean())
print(100*(early.mean() - late.mean())/early.mean())
# Para ello necesitamos definir un nivel de significancia como umbral para saber cuanto estamos dispuesto a considerar como diferencia y poder tomar una decision. Este nivel de significancia se llama alfa.
# Valores tipicos para alfa en ciencias sociales varian de entre 0.1, 0.05
# En fisica, donde los experimentos son mas controlados se espera usar valores del orden de 10e-5 o mayores.

#En python hay una libreria de tests estadisticos
from scipy import stats
#Por ejemplo el T-test es una forma de comparar los promedios de 2 poblaciones diferentes.
# Es bueno primero investigar que tipo de distribucion subjacente esya presente en los datos antes de aplicar alguno de estos test.
# Para usar el T-test ingresamos los dos grupos dentro de la funcion
T_test = stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
print(T_test)
# EL resultado es una 2pla con el test statistic y el p-value. El p-value es mayor que el umbral de 0.05, por lo que no podemos rechazar la hipotesis nula. Esto nos dice que las 2 poblaciones son iguales. Podemos decir que no existe diferencia estadistica en estas 2 muestras.
# Veamos si pasa lo mismo con las notas del curso 2
T_test = stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])
print(T_test)
# El resultado del p-value es incluso mayor que el anterior.
#Veamos las notas 3
T_test = stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade'])
print(T_test)
# Es mas cercano al valor umbral, pero aun es mayor.
# Aqui hay que parar para entender lo que esta pasando. Si seguimos buscando algun curso en donde haya u  p-value menor que el valor umbral lo que estamos haciendo se llama P-hacking or Dredging. Esto es, estamos forzando nuestra muestra para intentar validar nuestra hipotesis. AL hacer muchos test hasta que alguno muestre lo que queremos no es una forma buena de trabajar con esto.
# Pare evitar caer en esto podemos usar los siguientes metodos.
#a) Usando el nivel de confianza (p-value) = 0.05 podriamos encontrar 1 valor positivo si hacemos 20 test, pero necesitamos corregir este valor umbral. Para ellos podemos multiplicar el p-value por 1/20 y así corregir nuestro p.value haciendo mas confiable el test de hipotesis. (Bonferroni correction)
# b) Podemos tomar parte de los datos para ser testeados y ver que tan genericos son los resultados. Podemos tomar la mitad de los datos en cada muestra y hacer el t-test. COn estos resultados podemos formular una hipotesis bien especifica y luego correr el t-test muy limitado basado en esta hipotesis.
# c) EL tercer metodo es que bosquejes lo que esperas obtener, y describas un test que apoye positivamente esta idea.
