# Variáveis não podem começar por números.
# Caracteres especiais não são aceitos, com exceção do underline.

nome = input("Digite um funcionário: ")
empresa = input("Digite a empresa: ")
qtDeFuncionarios = int(input("Digite a quantidade de funcionários: "))
mediaSalario = float(input("Digite a média do salário: "))

print("---------------------------------------------")
print(nome + " trabalha na empresa " + empresa)
print("Possui " + str(qtDeFuncionarios) + " funcionarios")
print("A média de salário é de: " + str(mediaSalario))
print("---------------------------------------------")
print(" ")
print("Tipos de dados:")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtDeFuncionario] é: ", type(qtDeFuncionarios))
print("O tipo de dado da variável [mediaSalario] é: ", type(mediaSalario))

print("---------------------------------------------")
input("Pressione enter...")




