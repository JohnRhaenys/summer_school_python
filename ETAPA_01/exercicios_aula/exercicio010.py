"""
Fazer um programa com um método capaz de lidar com dados com
valores em cadeias de
caracteres (String). Separar os símbolos alfanuméricos
 (letras e algarismos) em cada cadeia.
"""

string = 'ABC123XYZ'

# letras = ''
# algarismos = ''
# for caractere in string:
#     if ord(caractere) >= 65 and ord(caractere) <= 90:
#         letras = letras + caractere
#     elif ord(caractere) >= 48 and ord(caractere) <= 57:
#         algarismos = algarismos + caractere
#
# print(letras)
# print(algarismos)


# CODIGO_ASCII_LETRA_A = 65
# CODIGO_ASCII_LETRA_Z = 90
#
# letras = ''
# algarismos = ''
# for caractere in string:
#     if CODIGO_ASCII_LETRA_A <= ord(caractere) <= CODIGO_ASCII_LETRA_Z:
#         letras = letras + caractere
#     elif 48 <= ord(caractere) <= 57:
#         algarismos = algarismos + caractere


# letras = ''
# algarismos = ''
# for caractere in string:
#     if caractere.isnumeric():
#         algarismos += caractere
#     elif caractere.isalpha():
#         letras += caractere
#
# print(letras)
# print(algarismos)


# letras = ''.join(list(filter(lambda c: c.isalpha(), string)))
# algarismos = ''.join(list(filter(lambda c: c.isnumeric(), string)))
# print(letras)
# print(algarismos)

