"""Listas en Python"""

"""Listas -> clear(): Limpia los elementos de una lista"""

var_1 =[60.8, 20.9, 140, False, "Miraflores"]

print("Los valores son: {}".format(var_1))

var_1.clear()
print("lista: {}".format(var_1))

# No se ha eliminado la lista, solo se ha limpiado
var_1.append("Perú")
print("lista: {}".format(var_1))
