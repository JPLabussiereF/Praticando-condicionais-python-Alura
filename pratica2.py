# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.
# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

atividade_a = int(input('Digite o número de dias necessários para concluir a atividade A: '))
atividade_b = int(input('Digite o número de dias necessários para concluir a atividade B: '))
atividade_c = int(input('Digite o número de dias necessários para concluir a atividade C: '))
total = atividade_a + atividade_b + atividade_c

if (atividade_a < 0 or atividade_b < 0 or atividade_c < 0):
    print('Os valores inseridos são inválidos!')
else: 
    print(f'O tempo total necessário para concluir o projeto é de {total} dias.')