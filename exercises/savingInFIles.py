man = []
other = []

try:
    data = open("sketch.txt")
    for cada_linha in data:
        try:
            (role, line_spoken) = cada_linha.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    print(man)
    print("")
    print(other)

    data.close()
except IOError:
    print("O arquivo de dados não está na pasta")

    print(man)
    print(other)
