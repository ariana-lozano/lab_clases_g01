"""Listas en Python"""

"""Listas -> sort(): Ordena los elementos de una lista"""

#Primero van las mayúsculas y luego por orden alfabético
var_1 = ["Camila", "Mariana", "Ariana", "Ana", "Zoe","ana"]

# Va de menor a mayor número
var_2 = [ 40, 2, 600, 36, 40.8, 2]


var_1.sort()
var_2.sort()

print(var_1)
print(var_2)

suma_lista = var_1 + var_2
print(suma_lista)

# No es permitido un orden de datos numéricos y strinrg cuando están dentro de una sola lista
