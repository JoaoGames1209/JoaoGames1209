import time
print("Bem vindo a jogolegal.py !!!")
time.sleep(2)
print("Deseja jogar o jogo?")
resposta = str(input("y/n"))
time.sleep(1)
if resposta == 'y':
  print("O jogo vai começar!!")
  time.sleep(2)
  print("Aguarde 24 horas para a proxima rodada começar!!! (especificamente quando o contador chegar a 64200)")
  time.sleep(5)
  print("So vamos começar logo mesmo")
  time.sleep(2.9)
  print("As regras são, voce tera 3 chances, se errar todas você perde!")
  time.sleep(3)
  print("Adivinhe o numero certo e voce ganha!!!")
  time.sleep(4.6)
  print("1)")
  resposta1 = int(input("De um numero de 1 e 2 qual o certo?"))
  if resposta1 == 1:
    print("Parabens!!")
    time.sleep(3)
    print("2)")
    resposta2 = int(input("De um numero de 1 e 5 qual o certo?"))
    if resposta2 == 4:
  
      print("Parabens")
      time.sleep(2)
      print("ULTIMA QUESTÃO!!")
      time.sleep(1)
      print("3)")
      resposta3 = int(input("De um numero de 1 e 100000 qual o certo?"))
      if resposta3 == 2:
        time.sleep(4)
        print("PARABENS VOCÊ VENCEU!!!!")
        time.sleep(6)
        print("Se deseja tentar denovo de run novamente!")
      else:
        time.sleep(4)
        print("PARABENS VOCÊ VENCEU!!!!")
        time.sleep(6)
        print("Se deseja tentar denovo de run novamente!")
    else:
      print("você tem apenas mais 2 chance D:")
      time.sleep(4)
      print("ULTIMA QUESTÃO!!")
      time.sleep(1)
      print("3)")
      resposta3 = int(input("De um numero de 1 e 100000 qual o certo?"))
      if resposta3 == 2:
        time.sleep(4)
        print("PARABENS VOCÊ VENCEU!!!!")
        time.sleep(6)
        print("Se deseja tentar denovo de run novamente!")
      else:
        print("PARABENS VOCÊ VENCEU!!!!")
        time.sleep(6)
        print("Se deseja tentar denovo de run novamente!")
  else:
    print("Você so tem mais 2 chances D:")
    time.sleep(3)
    print("2)")
    resposta2 = int(input("De um numero de 1 e 5 qual o certo?"))
    if resposta2 == 4:
  
      print("Parabens")
      time.sleep(2)
      print("ULTIMA QUESTÃO!!")
      time.sleep(1)
      print("3)")
      resposta3 = int(input("De um numero de 1 e 100000 qual o certo?"))
      if resposta3 == 2:
        time.sleep(4)
        print("PARABENS VOCÊ VENCEU!!!!")
        time.sleep(6)
        print("Se deseja tentar denovo de run novamente!")
      else:
        print("Você perdeu")
        time.sleep(4)
        print("Se deseja tentar denovo de run novamente!")
    else:
      print("você tem apenas mais 1 chance D:")
      time.sleep(4)
      print("ULTIMA QUESTÃO!!")
      time.sleep(1)
      print("3)")
      resposta3 = int(input("De um numero de 1 e 100000 qual o certo?"))
      if resposta3 == 2:
        time.sleep(4)
        print("PARABENS VOCÊ VENCEU!!!!")
        time.sleep(6)
        print("Se deseja tentar denovo de run novamente!")
      else:
        print("Você perdeu")
        time.sleep(6)
        print("Se deseja tentar denovo de run novamente!")
    
else:
  print("Você disse não ou escreveu errado, apenas escreva y minusculo se quiser jogar")
  time.sleep(4)
  print("Se deseja tentar denovo de run novamente!")
