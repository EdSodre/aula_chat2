def buscar_resposta(pergunta):
    arquivo='bot.txt'
    respostas = {}
    # r = leitura
    # w = escrita
    # a = append = adicione no final
    try:
        with open(arquivo,'r',encoding="utf-8") as f:
            for linha in f:
                perg=linha.strip().split("=")[0]
                resp=linha.strip().split("=")[1]
                respostas[perg.lower()] = resp.lower()
    except FileNotFoundError:
        pass
    return respostas.get(pergunta.lower(), 'não entendi sua questão')           
