
"""Listas en Python"""

"""
Requisitos:

- Crear dos lista de personas vacías
- Agregar los datos de nombre, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edad // por índica
- Sumar ambas listas y mostrar el resultado en la terminal
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas
- Mostrar la lista vacía de la segunda persona aplicando el método respectivamente

"""

# Crear de lista vacía
persona_01 =[]
persona_02 =[]
print("persona 1: {}".format(persona_01))
print("persona 2: {}".format(persona_02))

# Agregar datos
persona_01.append("Camila")
persona_01.append(17)
persona_01.append("Ingeniería")

persona_02.append("Ale")
persona_02.append(18)
persona_02.append("Química")

print("persona 1: {}".format(persona_01))
print("persona 2: {}".format(persona_02))

# Suma de listas
suma = persona_01 + persona_02
print("Suma: {}".format(suma))

# Mostrar inversa
suma.reverse()
print("Reversa: {}".format(suma))

# Eliminar edades
suma.remove(18)
suma.remove(17)
print("Lista actualizada: {}".format(suma))

#Lista vacía persona 2
persona_02.clear()
print("Lista de persona 2: {}".format(persona_02))
