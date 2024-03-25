#biblioteca para usar um número aleatório criado pelo programa
import random
#comando que cria um número aleatório criado pelo programa entre 1 e 100
numero_secreto = random.randint(1, 100)
#loop que solicita um número ao usuário enquanto estiver errando
while True:
  #solicita um número do usuário
  numero_digitado = int(input("Digite um número entre 1 e 100: "))
  #verifica se o número é igual -> o usuário acertou
  if numero_digitado == numero_secreto:
    print("Parabéns! Você adivinhou o número secreto!")
    break
  #verifica se o número digitado é maior
  elif numero_digitado > numero_secreto:
    print("O número secreto é menor!")
  #se nao for igual e nem maior o numero digitado eh menor
  else:
    print("O número secreto é maior!")