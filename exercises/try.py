try:
    arquivo = "./test/texto.txt"
    arq = open(arquivo, "r")
    texto = arq.read()
    print(texto)

except:
    print("Arquivo " + arquivo + " não foi encontrado.")

