print("Inicio do programa")

#parte 1
texto = "Gravação e leitura de arquivo de texto"
arq = open("exemplo.txt", "w")
arq.write(texto)
arq.close()

#parte2
arq = open("exemplo.txt","r")
L = arq.readline()
arq.close()
print("String lido = {}".format(L))

print("Fim do programa")
