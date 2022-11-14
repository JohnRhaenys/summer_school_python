# Acessando valor dada a chave

idades_pessoas = {'Harry': 13, 'Pedrinho': 24, 'Zezinho': 3, 'Maria': 4, 'Creuza': 5}

tamanho = len(idades_pessoas)

idade_harry = idades_pessoas['Harry']

# Quando eu tento buscar um valor a partir de uma chave inexistente, o Python
# me da um KeyError, que eh uma excecao que deve ser tratada pelo programador
idade_hermione = idades_pessoas['Hermione']


print('Pessoas: ', idades_pessoas)
print('Tamanho: ', tamanho)
print('Idade Harry: ', idade_harry)
