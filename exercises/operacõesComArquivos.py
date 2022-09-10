arquivo = open("relatorio.txt", "r")
linha = arquivo.readline()

while (linha != ""):
    print(linha)
    linha = arquivo.readline()

#-------------------------------------------------------#
print("Exemplo 2") 

linhas = arquivo.readlines()

cont = 0
while(cont < len(linhas)):
    print(linhas[cont])
    cont += 1