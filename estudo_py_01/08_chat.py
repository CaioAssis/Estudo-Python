# os é usado para interagir com o sistema operacional.
import os

mensagens = []

nome = input('Nome: ')

while True:
    # Limpar terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])

    print('__________')

    # Obtendo texto
    texto = input('mensagem: ')
    if texto == 'fim':
        os.system('cls')
        break

    # adicionando mensagem na lista
    mensagens.append({
        'nome': nome,
        'texto': texto
    })