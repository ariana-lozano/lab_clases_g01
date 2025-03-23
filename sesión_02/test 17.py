"""Listas en Python"""
from numpy.ma.core import append

"""Listas len(): Obtener el tamaño de la lista en Python """

paises = []

print("El tamaño de mi lista es : {}".format(len(paises)))

"""Agrengando datos a mi lista: append()"""

paises.append("Perú")
paises.append("Colombia")
paises.append("Francia")
paises.append("España")

print("El nuevo tamaño de mi lista es: {}".format(len(paises)))
print("Los valores de mi lista: {}".format(paises))