"""Listas en Python"""

"""Listas -> copy(): Copia """

var_1 = ["Camila", "Mariana", "Ariana", "Ana", "Zoe","ana"]
var_2 = var_1.copy()

print("Los valore de mi var_2 son : {}".format(var_2))

var_2.append("MaríaDB")
var_2.append("SQLite3")

print("Lista actualizada: {}".format(var_2))