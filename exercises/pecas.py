pecas = {}

print("Leitura de peças")

while True:
    cod = input("Digite o nome da peça: ")

    if cod == "0":
        break
    elif cod in pecas:
        print("A peça {} já existe no cadastro".format(cod))
        continue

    qtde = int(input("Digite a quantidade: "))
    pecas[cod] = qtde

print("Fim da leitura dos dados\n")
print("Estoque de peças")

for c in pecas:
    print("{1:4} unidade da peças {0}".format(c, pecas[c]))

print("\nFIM DO PROGRAMA")

print(pecas)