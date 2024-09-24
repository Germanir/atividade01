print ("Bem vindo a Calculadora de IMC")

pergunta_nome = input("Qual é o seu nome? " )
nome = ("Olá" , pergunta_nome)
idade = input (f"Qual sua idade? ")
peso = float(input("Qual seu peso (em KG)? "))
altura = float(input("Qual sua Altura (em metros e usando ponto)? "))

print("Vamos calcular seu IMC")

imc = (peso / (altura * altura))

print(pergunta_nome , (f"seu IMC é: {imc:.2f}"))