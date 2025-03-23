"""""
Requisitos

1. Crear 2 variables enteras. 2 variables flotantes, 1 variable string ( solo caracteres), 1 variable string con contenido solamente numérido, 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica (realizar conversiones si es necesario)
3. Obtener y mostrar la suma de las 2 variables enteras mñas la variable string numérica y la variable flotante 
4. Obtener y mostrar el módulo de las dos variables enteras: %
5. Obtener y mostrar el resultado entero o parte entera de las 2 variables int: //
6. Obtener la potencia usando una de las variables flotante como base y la variable como potencia

"""""
var_int_1 = 54
var_int_2 = 67
var_float_1 = 12.5
var_float_2 = 6.7
var_str = "Sofia"
var_str_num = "2025"
var_bool = False
suma_1 = var_int_1 + int(var_str_num)
print ("La suma de un núnero entero con un número str es {}".format(suma_1))
suma_2 = var_int_1 + var_int_2 + int(var_str_num) + var_float_1
print("La suma de dos núnmeros enteros, un número en str y un flotante es {} ".format(suma_2))
modu = var_int_1 % var_int_2
print("El módulo de dos variables enteras es: {}".format (modu))
resul_int = var_int_2 //var_int_1
print("El resultado de una división entera es: {}". format(resul_int))
resul_potencia = pow(var_float_2,var_int_1)
print ("El resultado de una potencia de base flotante y exponente entero es : {}".format(resul_potencia))