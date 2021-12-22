#Ejercicio condicionales 1

''' 
Hacer un programa que pida tres número y determine cuál es el mayor
'''

num1 = int(input('ingrese primer número: '))
num2 = int(input('ingrese segundo número: '))
num3 = int(input('ingrese tercer número: '))

if num1>num2 and num1>num3:
    print(f'el mayor es {num1}')
elif num2>num1 and num2>num3:
    print(f'el mayor es {num2}')
else:
    print(f'el mayor es {num3}')

print('fin del programa')