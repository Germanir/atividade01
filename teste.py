x = b"hello"

print(x)
print(type(x))

valor = int(input("digite o valor: "))

match valor:
    case valor if valor > 1 and valor < 4:
        print("Entre 1 e 3")
    case valor if valor > 4 and valor < 8:
        print("Entre 4 e 8")
    case _:
        print("Outro valor")