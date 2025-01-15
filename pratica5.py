# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

limite_orcamento = 3000

def controle_orcamento():
    total_despesas = float(input('Digite o total de despesas realizadas (R$): '))
    if total_despesas > limite_orcamento:
        print('\nAtenção! Você ultrapassou o limite de R$ 3.000,00 para despesas mensais.')
    elif total_despesas < limite_orcamento:
        print('\nVocê ainda está dentro do orçamento de R$ 3.000,00 para despesas mensais.')
    else:
        print('\nVocê atingiu exatamente o limite de R$ 3.000,00 para despesas mensais.')

controle_orcamento()