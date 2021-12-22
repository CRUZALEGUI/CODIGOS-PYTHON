#Ejercicio condicionales 2
'''
Hacer un programa que pida un caracter e indique si es una vocal o no
'''

letra = input('ingrese un caracter: ')

if len(letra)==1:
    if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        print(f'"{letra}" es una vocal')
    else:
        print(f'"{letra}" no es una vocal')
else:
    print('Dato incorrecto')