alunos = {}

print("Leitura de dados")

while True:

    matr = int(input("Digite a matricula: "))

    if matr == 0:
        break
    elif matr in alunos:
        print("A matricula {} já existe no cadastro".format(matr))
        continue

    dicItem = {}
    dicItem['nome'] = input("Nome: ")
    dicItem['idade'] = int(input("Idade: "))
    dicItem['curso'] = input("Curso: ")
    alunos[matr] = dicItem

print("Fim da leitura dos dados\n")
print("Cadastro de alunos\n")

for matricula, dados in alunos.items():

    print("Aluno: {}".format(dados['nome']))
    print("Nr. Matricula: {}".format(matricula))
    print("Idade: {}".format(dados['idade']))
    print("Curso: {}\n".format(dados['curso']))
    
print("\nFIM DO PROGRAMA")
