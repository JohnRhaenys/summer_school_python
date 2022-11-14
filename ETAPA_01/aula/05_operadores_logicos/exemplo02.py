altura_minima_cm = 100
altura_maxima_cm = 200

altura = int(input('Entre com a sua altura: '))

if altura < altura_minima_cm or altura > altura_maxima_cm:
    print('Sua altura nao e permitida')
else:
    print('Altura permitida')
