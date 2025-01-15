# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperatura_atual = float(input('Digite a temperatura atual da sala de servidores: '))
if temperatura_atual > 25:
    print('Atenção! A temperatura da sala de servidores está acima do limite permitido.')
elif temperatura_atual < 25:
    print('A temperatura da sala de servidores está dentro do limite permitido.')
else:
    print('A temperatura da sala de servidores está exatamente no limite permitido de 25ºC.')