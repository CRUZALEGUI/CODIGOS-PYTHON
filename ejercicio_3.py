''' 
Ejercicio 3
Hacer un programa para ingresar el radio de un circulo y se reporte su área y
la longitud de la circunferencia
''' 

import math

radio = float(input('radio -> '))
area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f'el área es {area:.2f} y la longitud es {longitud}') 
#'2f' indica que después del punto decimal solo se mostrará dos decimales