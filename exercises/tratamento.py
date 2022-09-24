try:
    data = open("sketch.txt")
    for cada_linha in data:
        try:
            (role, line_spoken) = cada_linha.split(":"  ,1)
            print(role, end='')
            print(' disse: ', end='')
            print(line_spoken, end='')
        except:
            pass

    data.close()
except:
    print("O arquivo de dados não está na pasta")
