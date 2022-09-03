def somar(num1, num2):
    return num1 + num2

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print("A soma de " + str(n1) + " e " + str(n2) + " é: " + str(somar(n1, n2)))
print("A soma de {n1} e {n2} é: ".format(n1 = n1, n2 = n2))
