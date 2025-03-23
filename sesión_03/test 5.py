"""Listas en Python"""

"""Listas -> count(): Contar cuantas veces se repite algo"""

var_1 = ["Python", "JAVA", "php", "Javascrib", "Typescript"]

var_1.append("Python")
var_1.append("Python")
var_1.append("Python")
var_1.append("Python")
var_1.append("NodeJS")

print("Mi lista var_1: {}".format(var_1))

print("La cantidad de veces que se repite 'Python es: {}".format(var_1.count("Python")))
