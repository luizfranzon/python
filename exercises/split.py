data = open("sketch.txt")
for cada_linha in data:
    if not cada_linha.find(":") == -1:
        (role, line_spoken) = cada_linha.split(":"  ,1)
        print(role, end='')
        print(' disse: ', end='')
        print(line_spoken, end='')

data.close()