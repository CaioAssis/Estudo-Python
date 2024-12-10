import os

player = { 'nome':'Player', 'x':0, 'y':0 }

def andar(direcao):
    if direcao == 'd':
        player['x'] += 1
    elif direcao == 'a':
        player['x'] -= 1
    elif direcao == 'w':
        player['y'] -= 1
    elif direcao == 's':
        player['y'] += 1

while True:
    os.system('cls')

    print("--------------------", end='')
    for y in range(5):
        print('\n', end='')
        for x in range(20):
            if player['x'] == x and player['y'] == y:
                print('@', end='')
            else:
                print('_', end='')
    print("\n--------------------")

    direcao = input('Proxima direcao([w],[a],[s],[d]): ')
    andar(direcao)