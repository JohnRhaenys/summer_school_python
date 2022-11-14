# Acessando valor dada a chave - mais recomendado

idades_pessoas = {'Harry': 1, 'Pedrinho': 2, 'Zezinho': 3, 'Maria': 4, 'Creuza': 5}

tamanho = len(idades_pessoas)

idade_harry = idades_pessoas.get('Harry')
idade_hermione = idades_pessoas.get('Hermione')

if idade_hermione is None:
    print('Pessoa nao existe')

print('Pessoas: ', idades_pessoas)
print('Tamanho: ', tamanho)
print('Idade Harry: ', idade_harry)
print('Idade Hermione: ', idade_hermione)


for key, value in idades_pessoas.items():
    print(f'A pessoa {key} tem idade {value}')
