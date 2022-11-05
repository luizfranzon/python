soma = 0
count = 0 

file = open("inteiros.txt", "r")
S = file.readline()

while S != "":
    N = int(S)
    soma += N
    count += 1
    print("Elementos {0} = {1}".format(count, N))
    S = file.readline()

file.close()
print("Soma = {0}".format(soma))