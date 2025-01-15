# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda. Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

quantidade_bananas_vendidas = int(input('Digite a quantidade de bananas vendidas no mês passado: '))
quantidade_macas_vendidas = int(input('Digite a quantidade de maçãs vendidas no mês passado: '))

if quantidade_bananas_vendidas == quantidade_macas_vendidas:
    print('Houve um empate nas vendas de bananas e maçãs no mês passado!')
elif quantidade_bananas_vendidas > quantidade_macas_vendidas:
    print('As bananas foram a fruta mais vendida no mês passado!')
else: 
    print('As maçãs foram a fruta mais vendida no mês passado!')