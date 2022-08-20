entrada = int(input("Digite um número de 0 a 100"))

if numero < 0 or numero > 100:
    print("O número digitado for invalido.")

if numero % 2 == 0:
    print("O numero digitado foi par.")

if numero % 2 != 0:
    print("O número digitado for ímpar")