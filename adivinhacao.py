import random

numero_secreto = random.randint(1, 100)

while True:
  numero_digitado = int(input("Digite um número entre 1 e 100: "))

  if numero_digitado == numero_secreto:
    print("Parabéns! Você adivinhou o número secreto!")
    break
  elif numero_digitado > numero_secreto:
    print("O número secreto é menor!")
  else:
    print("O número secreto é maior!")
