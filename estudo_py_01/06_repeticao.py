# for

for x in range(5):
    print(x)
print('Fim do for\n')

nota = [5, 8, 7, 5, 6, 7, 10, 9, 9, 7]
notas = []

for n in range(len(nota)):
    aluno = n+1
    resultado = [aluno, nota[n]]
    notas.append(resultado)

for n in notas:
    cod_aluno = n[0]
    nota = n[1]
    print ('Aluno', cod_aluno, "tirou a nota:", nota)

print()
# while

x = 0
while x <= 5:
    y = 0
    while y <= x:
        print('*', end='')
        y = y+1
    print('\n', end='')
    x = x+1