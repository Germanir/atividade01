
print("## Bem-vindo ao trem fantasma ##")
print(" ")

try:
    idade = int(input("Informe a sua idade: "))
    peso = float(input("Informe o seu peso: ").replace(",","."))

    if idade >= 10 and peso < 150:
        print(f"Você está liberado")
    else:
        print(f"Você tem menos de 10 anos ou mais de 150 kg")
    print(" ")
except:
    print("Ocorreu um erro")
