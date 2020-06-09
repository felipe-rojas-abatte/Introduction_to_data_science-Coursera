## Clases
class Person:
    department = 'School of Information' #a class variable

    def set_name(self, new_name): #definimos un metodo
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

#######################################

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary): ## primer metodo que se llama class constructor
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

#creamos primera entrada de la clase
print('This would create first object of Employee class')
emp1 = Employee("Zara", 2000)
print('This would create second object of Employee class')
emp2 = Employee("Manni", 5000)

## Podemos acceder a los objetos
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

###################
##Mapeo: devuelve in iterador que aplica una funciones a cada item 
#Ejemplo: map(funcion, variables a iterar)
## Como encontrar el valor minimo entre 2 listas comparando los elementos de la misma posicion
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest

for item in cheapest:
    print(item)
