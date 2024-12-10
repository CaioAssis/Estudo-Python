import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        # Fazendo a requisição
        resposta = requests.get(url)
        
        # Verificando se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            dados = resposta.json()
            
            # Verificando se o CEP é válido
            if "erro" in dados:
                return False
            else:
                return dados
        else:
            print("Erro na requisição:", resposta.status_code)
    except Exception as e:
        print("Erro ao consultar o CEP:", e)