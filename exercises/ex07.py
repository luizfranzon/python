file = open("numerosReais.txt", "w")

while True:
    data = int(input("Digite um número: "))

    if data != 0:
        file.write("{:.3f}".format(data) + '\n')
    else:
        break

    file.close()