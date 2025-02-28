#Importar la biblioteca pulp
from pulp import LpMaximize, LpProblem, lpSum, LpVariable

#Definir el problema de programación lineal
model = LpProblem(name="maximizar-beneficios", sense=LpMaximize)

#Definir las variables de decisión
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

#Definir la función objetivo
model += lpSum([2*x, 3*y])

#Definir las restricciones
model += (x + 2*y <= 4, "restriccion_1")
model += (2*x + y <= 3, "restriccion_2")

#Resolver el problema
status = model.solve()

#Imprimir la solución óptima
if status == 1:
    print("Solución óptima encontrada:")
    print(f"x = {x.varValue}")
    print(f"y = {y.varValue}")
    print(f"Beneficio máximo = {model.objective.value()}")
else:
    print("No se encontró una solución óptima")