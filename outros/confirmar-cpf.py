cpf = input("Digite o CPF (apenas números): ")
num = []
m = 9
somaAux = 0
vrfAux = 0

if len(cpf) == 11:
    for n in range(9):
        num.append(int(cpf[n]))
    vrf = int(cpf[9]+cpf[10])

    for n in range(9):
        m = m-1
        somaAux = somaAux + (num[m] * (n+2))
    
    if somaAux%11 <= 1: #dezena = 0
        num.append(0)
        vrfAux = vrfAux + 0
    else:               #dezena = 11 - resto da soma / 11
        num.append(11-(somaAux%11))
        vrfAux = vrfAux + (11-(somaAux%11))*10
    somaAux=0
    m=10

    for n in range(10):
        m = m-1
        somaAux = somaAux + (num[m] * (n+2))

    if somaAux%11 <= 1: #unidade = 0
        num.append(0)
        vrfAux = vrfAux + (0)
    else:               #unidade = 11 - resto da soma / 11
        num.append(11-(somaAux%11))
        vrfAux = vrfAux + (11-(somaAux%11))
    
    if bool(vrfAux == vrf):
        print('O dígito verificador está correto.')
    else:
        print('O dígito verificador está incorreto.')
        print('Dígito expresso: ', vrf)
        print('Dígito esperado: ', vrfAux)
else:
    print('O CPF deve conter 11 digitos.')