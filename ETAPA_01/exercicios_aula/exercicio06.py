"""
Ler dois caracteres e escreve-los em ordem alfabética
"""
primeiro_caractere = input('Insira um caractere: ')
segundo_caractere = input('Insira outro caractere: ')

if primeiro_caractere < segundo_caractere:
    print(primeiro_caractere, segundo_caractere)
else:
    print(segundo_caractere, primeiro_caractere)