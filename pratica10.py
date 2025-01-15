# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

renda_mensal = float(input('Digite o valor da renda mensal: '))
valor_parcela = float(input('Digite o valor da parcela desejada: '))

if renda_mensal > 2000 and valor_parcela <= renda_mensal * 0.3:
    print('Empréstimo aprovado!')
else: 
    print('Empréstimo negado!')
    