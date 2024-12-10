from consultar_cep import consultar_cep
from tkinter import *

resultados_exibidos = []

def botao_handler():
    global resultados_exibidos  # Usar a lista de forma global

    # Limpa os rótulos exibidos anteriormente
    for label in resultados_exibidos:
        label.destroy()
    resultados_exibidos = []  # Reseta a lista

    req = input_cep.get()
    dados = consultar_cep(req)

    if dados:
        i = 0
        for chave, valor in dados.items():
            res_cep = Label(janela, text=f'{chave}: {valor}')
            res_cep.grid(column=0, row=i+4)
            resultados_exibidos.append(res_cep)  # Armazena o rótulo
            i += 1
    else:
        res_cep = Label(janela, text='CEP Inválido!')
        res_cep.grid(column=0, row=4)
        resultados_exibidos.append(res_cep)  # Armazena o rótulo

def aplicar_mascara(arg):
    texto = input_cep.get()

    # Remove todos os caracteres não numéricos
    texto = ''.join(filter(str.isdigit, texto))

    # Aplica a máscara do CEP ('99999-999')
    if len(texto) > 5:
        texto = f"{texto[:5]}-{texto[5:8]}"
    input_cep.delete(0, END)
    input_cep.insert(0, texto)

# Criar janela principal
janela = Tk()
janela.title('Consultar CEP')

texto_orientacao = Label(janela, text='Escreva o CEP')
texto_orientacao.grid(column=0, row=0)

input_cep = Entry(janela, width=30)
input_cep.grid(column=0, row=1)

botao = Button(janela, text='Buscar CEP', command=botao_handler)
botao.grid(column=0, row=2)

texto_orientacao2 = Label(janela, text='')
texto_orientacao2.grid(column=0, row=3)

input_cep.bind("<KeyRelease>", aplicar_mascara)

# Mantém janela aberta
janela.mainloop()