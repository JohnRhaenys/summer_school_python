"""
Ler do teclado um número inteiro com três dígitos (no formato CDU - centena, dezena e
unidade) e mostrar o número invertido (no formato UDC). O número invertido deve ser
armazenado em outra variável antes de ser mostrado
"""

number = 34534534534789

unidade = 789 % 10
dezena = (789 // 10) % 10
centena = ((789 // 10) // 10) % 10

print(unidade)
print(dezena)
print(centena)
