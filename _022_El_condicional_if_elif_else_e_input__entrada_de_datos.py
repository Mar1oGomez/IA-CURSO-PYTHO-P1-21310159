#El condicional if elif else e input, entrada de datos

edad= int(input('cual es tu edad\n'))
if edad <= 0:
    print('esta edad no existe.')
elif edad >= 1 and edad <18:
    print('estas chabo, mi chabo')
elif edad >18 and edad <=45:
    print('chavo ruco')
elif edad > 45 and edad <=100:
    print('pinche momia')
elif edad >100 and edad <= 120:
    print('nmms un dinosaurio')
else:
    print('no valido')