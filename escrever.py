print("hello word")

def pergunta_resposta(pergunta,resposta):
  arquivo='bot.txt'
  #r = leitura
  #w = escrita
  #a = append
  with open(arquivo,'a',encoding='utf-8') as f:
    f.write(f"{pergunta}={resposta}")