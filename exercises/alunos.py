alunos = {}

print("Leitura de dados")
while True:
    matr = int(input("Digite a matricula: "))
    if matr == 0:
        break
    elif matr in alunos:
        print("A matricula {} já existe no cadastro".format(matr))
        continue
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    alunos[matr] = (nome, idade, curso)

print("Fim da leitura dos dados\n")
print("Cadastro de alunos")

for matricula, dados in alunos.items():
    print("Aluno {}".format(dados[0]))
    print("Nr. Matricula {}".format(matricula))
    print("Idade {}".format(dados[1]))
    print("Curso {}\n".format(dados[2]))
print("FIM DO PROGRAMA")
