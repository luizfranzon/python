arquivo = open("relatorio.txt", 'w')

for num in range (1, 10):
    arquivo.write("*" * num + "\n")

