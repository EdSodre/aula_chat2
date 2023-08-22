import escrever as treina

questão=str(input("treinar ou conversar: "))
if questão.lower()=="treinar":
 sair = "n"
 while sair.lower!= "sair":
  pergunta = str(input("Escreva uma pergunta: "))
  resultado= conversa.buscar_resposta(pergunta)
  sair= str(input("enter para continuar, ou sair: "))
  treina.pergunta_resposta(pergunta,resposta)
elif questão.lower()== "conversar":
  sair = "n"
  while sair.lower!= "sair":
   pergunta = str(input("Escreva uma pergunta: "))
   # fução buscar a resposta
   sair= str(input("enter para continuar, ou sair: "))
  